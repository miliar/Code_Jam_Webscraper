#include <algorithm>
#include <iostream>
#include <cassert>

enum Quat
{
    OneQuat = 0,
    IQuat = 1,
    JQuat = 2,
    KQuat = 3,
    NegOneQuat = 4,
    NegIQuat = 5,
    NegJQuat = 6,
    NegKQuat = 7,
};

std::string squats[] = {
    "1",
    "i",
    "j",
    "k",
    "-1",
    "-i",
    "-j",
    "-k",
};

Quat mult[8][8] = {
    {OneQuat, IQuat, JQuat, KQuat, NegOneQuat, NegIQuat, NegJQuat, NegKQuat},
    {IQuat, NegOneQuat, KQuat, NegJQuat, NegIQuat, OneQuat, NegKQuat, JQuat},
    {JQuat, NegKQuat, NegOneQuat, IQuat, NegJQuat, KQuat, OneQuat, NegIQuat},
    {KQuat, JQuat, NegIQuat, NegOneQuat, NegKQuat, NegJQuat, IQuat, OneQuat},
    {NegOneQuat, NegIQuat, NegJQuat, NegKQuat, OneQuat, IQuat, JQuat, KQuat},
    {NegIQuat, OneQuat, NegKQuat, JQuat, IQuat, NegOneQuat, KQuat, NegJQuat},
    {NegJQuat, KQuat, OneQuat, NegIQuat, JQuat, NegKQuat, NegOneQuat, IQuat},
    {NegKQuat, NegJQuat, IQuat, OneQuat, KQuat, JQuat, NegIQuat, NegOneQuat},
};

Quat inverses[8][8]; /// x*y = z gives x left_inverses[z][y] = x

void gen_tables()
{
//     Quat basic[4][4] = {
//         {OneQuat, IQuat, JQuat, KQuat},
//         {IQuat, OneQuat, KQuat, JQuat},
//         {JQuat, KQuat, OneQuat, IQuat},
//         {KQuat, JQuat, IQuat, OneQuat},
//     };
//     
//     bool is_negative[4][4] = {
//         {false, false, false, false},
//         {false, true, false, true},
//         {false, true, true, false},
//         {false, false, true, true},
//     };
//     
//     for(int first_negative = 0; first_negative < 2; ++first_negative)
//     {
//         for(int second_negative = 0; second_negative < 2; ++second_negative)
//         {
//             for(int first = 0; first < 4; ++first)
//             {
//                 for(int second = 0; second < 4; ++second)
//                 {
//                     Quat f = Quat(4*first_negative + first);
//                     Quat s = Quat(4*second_negative + second);
//                     
//                     bool sign = is_negative[first][second] ^ (first_negative == 1) ^ (second_negative == 1);
//                     Quat unsigned_value = basic[first][second];
//                     Quat signed_value = Quat(4*sign + int(unsigned_value));
//                     
//                     if(mult[f][s] != signed_value)
//                     {
//                         printf("mult[%d][%d] === %d == %d\n", f, s, mult[f][s], signed_value);
//                         assert(mult[f][s] == signed_value);
//                     }
//                 }
//             }
//         }
//     }
    
    for(int f = 0; f < 8; ++f)
        for(int s = 0; s < 8; ++s)
        {
            std::cout << squats[mult[f][s]] << "/" << squats[s] << " = " << squats[f] << std::endl;
            inverses[mult[f][s]][s] = Quat(f);
        }
}

std::vector<Quat> ltor;
std::vector<Quat> rtol;

// inline Quat prefix(int end)
// {
//     return (end == 0) ? OneQuat : quats[end - 1];
// }
// 
// inline Quat range(int beg, int end) /// [beg, end)
// {
//     Quat unincluded = prefix(beg);
//     Quat full = prefix(end);
//     
//     std::cout << "\t\t" << "[0, " << end - 1 << "], = " << squats[full] << " [0, " << beg - 1 << "], = " << squats[unincluded] << " " << squats[inverses[full][unincluded]] << " vs " << squats[inverses[unincluded][full]] << std::endl;
//     
//     return inverses[unincluded][full];
// }

int main(int argc, char** argv)
{
//     gen_tables();
    
    int T = 0;
    std::cin >> T;
    
    for(int t = 1; t <= T; ++t)
    {
        ltor.clear();
        rtol.clear();
        
        long long X, L;
        std::string base;
        std::cin >> L >> X >> std::ws >> base;
//         std::cout << X << " " << L << " " << base << std::endl;
        
        bool can_do = false;
        
        Quat previous_ltor_quat = OneQuat;
        ltor.reserve(X*L);
        for(int x = 0; x < X; ++x)
        {
            for(int l = 0; l < L; ++l)
            {
                Quat new_quat = OneQuat;
                
                switch(base[l])
                {
                    case 'i':
                        new_quat = mult[previous_ltor_quat][IQuat];
                        break;
                    case 'j':
                        new_quat = mult[previous_ltor_quat][JQuat];
                        break;
                    case 'k':
                        new_quat = mult[previous_ltor_quat][KQuat];
                        break;
                    default:
//                         printf("derp %d '%c'\n", l, base[l]);
                        assert(false);
                        break;
                }
                ltor.push_back(new_quat);
                previous_ltor_quat = new_quat;
//                 std::cout << squats[previous_ltor_quat];
            }
        }
//         std::cout << std::endl;
        
        Quat previous_rtol_quat = OneQuat;
        rtol.reserve(X*L);
        for(int x = 0; x < X; ++x)
        {
            for(int l = L - 1; l >= 0; --l)
            {
                Quat new_quat = OneQuat;
                
                switch(base[l])
                {
                    case 'i':
                        new_quat = mult[IQuat][previous_rtol_quat];
                        break;
                    case 'j':
                        new_quat = mult[JQuat][previous_rtol_quat];
                        break;
                    case 'k':
                        new_quat = mult[KQuat][previous_rtol_quat];
                        break;
                    default:
//                         printf("derp %d '%c'\n", l, base[l]);
                        assert(false);
                        break;
                }
                rtol.push_back(new_quat);
                previous_rtol_quat = new_quat;
//                 std::cout << squats[previous_rtol_quat];
            }
        }
//         std::cout << std::endl;
        std::reverse(rtol.begin(), rtol.end());
        
        if(ltor.back() == NegOneQuat)
        {
            for(int b = 0; b < int(ltor.size()); ++b)
            {
                if(ltor[b] == IQuat)
                {
                    for(int e = b + 2; e < int(rtol.size()); ++e)
                    {
                        if(rtol[e] == KQuat)
                        {
                            can_do = true;
                        }
                    }
                }
                else
                {
//                     std::cout << "ltor[" << b << "] = " << ltor[b] << " instead of 1" << std::endl;
                }
            }
        }
        else
        {
//             std::cout << "No because entire sequence" << std::endl;
        }
        std::cout << "Case #" << t << ": " << (can_do ? "YES" : "NO") << std::endl;
    }
}