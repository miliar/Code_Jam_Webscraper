#include <iostream>
#include <c++/fstream>
#include <c++/sstream>

using namespace std;

template <typename T1, typename T2>
T1 ipow(T1 a, T2 exp){
    if(0 == exp)
        return 1;
    else {
        T1 multiplier = a;
        T2 ret = 1;
        for(;;) {
            if(exp & 1)
                ret *= multiplier;

            exp >>= 1; // division by 2

            if(exp == 0)
                break;

            multiplier *= multiplier;
        }

        return ret;
    }
};

/**
 * The caller owns the returned array of size K-1.
 */
template <typename Int>
Int * positionOfGuys(Int K, Int C) {
    Int K_minus_1 = K-1,
        K_pow_C = ipow(K, C),
        K_pow_C_plus_1 = K_pow_C + 1,
        orig_factor = (K_pow_C - 1) / K_minus_1,
        factor = orig_factor;


    Int * positions= new Int[K_minus_1];
    for(Int i = 1, array_index = 0;
        i < K;
        ++i, ++array_index, factor += orig_factor)
    {
        positions[array_index] = K_pow_C_plus_1 - factor;
    }

    return positions;
}


template <typename Int>
void answer(Int K, Int C, Int S, ostringstream & oss) {
    if(S < K-1)
        oss << "IMPOSSIBLE";
    else if(K==1)
        oss << "1";
    else if(C==1) {
        if(S < K)
            oss << "IMPOSSIBLE";
        else {
            for(Int i=1; i<K; ++i)
                oss << i << ' ';
            oss << K;
        }
    }
    else {
        Int * positions = positionOfGuys(K,C);

        for(Int i=0; i<K-2; ++i)
            oss << positions[i] << ' ';
        oss << positions[K-2];

        delete[] positions;
    }
}

int main() {
    ofstream ofs("output.txt");
    ifstream fs("input.txt");

    string line;
    ostringstream outline;

    std::getline(fs, line); // consumes number.

    string emptyStr = "";
    int64_t T, K, C, S;

    T = std::stoll(line);
    //string K_as_str, C_as_str;
    for (uint64_t i = 1; i <= T;
         ++i,
         outline.str(emptyStr))
    {

        if(line.size() == 0) {
            cout << "WTF line with no input !";
            return -1;
        }

        /*
        for(digits = 0;
            line_index < line.size() && line[line_index] != ' ';
            ++line_index, ++digits) {}
        //*/

        getline(fs, line, ' ');
        K = std::stoll(line);
        getline(fs, line, ' ');
        C = std::stoll(line);
        getline(fs, line);
        S = std::stoll(line);

        cout << "K:" << K << " C:" << C << " S:" << S << endl;

        outline << "Case #" << i << ": ";
        answer(K,C,S, outline);
        outline << endl;
        outline.flush();

        cout << outline.str();
        ofs << outline.str();
    }

    fs.close();
    ofs.close();

    return 0;
}