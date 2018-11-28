#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

map<string,int> reg;

int multiply(int a, int b);

int calc(string sub) {
    if (sub.size() == 0) return 0;
    if (reg.count(sub) == 0) {
        if (sub.size() > 1) {
            int ertek = multiply(calc(sub.substr(0,sub.size()-1)),sub[sub.size()-1]-'i' + 2);
            if (sub.size() < 1000) reg[sub] = ertek;
            return ertek;
        }
        else {
            reg[sub] = sub[0] - 'i' + 2;
            return reg[sub];
        }
    }
   else {
            return reg[sub];
    }
}

int multiply(int a, int b) {
    int elojel = ((a < 0 && b > 0) || (a > 0 && b < 0) ? -1 : 1);
    if (a < 0) a*= -1;
    if (b < 0) b*= -1;
    switch (a) {
        case 1:
            switch (b) {
                case 1: return elojel*1; break;
                case 2: return elojel*2; break;
                case 3: return elojel*3; break;
                case 4: return elojel*4; break;
            }
            break;
        case 2:
            switch (b) {
                case 1: return elojel*2; break;
                case 2: return elojel*-1; break;
                case 3: return elojel*4; break;
                case 4: return elojel*-3; break;
            } break;
        case 3:
            switch (b) {
                case 1: return elojel*3; break;
                case 2: return elojel*-4; break;
                case 3: return elojel*-1; break;
                case 4: return elojel*2; break;
            } break;
        case 4:
            switch (b) {
                case 1: return elojel*4; break;
                case 2: return elojel*3; break;
                case 3: return elojel*-2; break;
                case 4: return elojel*-1; break;
            } break;
    }
    return 1;
}

int main()
{
    ifstream f("C-small-attempt2.in");
    //ifstream f("input.txt");
    ofstream g("output.txt");

    int T;
    f >> T;
    for (int i=0;i<T;++i) {
            cout << i << endl;
        reg.clear();
        int L, X;
        f >> L >> X; //L character repeated X times;
        string tmp;
        tmp.resize(L*X);
        char c;
        for (int j=0;j<L;++j){
            f >> c;
            tmp[j] = c; // - 'i' + 2;
        }
        for (int j=L;j<L*X;++j) tmp[j] = tmp[j%L];

        vector<int> iplaces, kplaces;
        int reszeredmeny = 1;
        for (int j=0;j<L*X-2;++j) {
            reszeredmeny = multiply(reszeredmeny, tmp[j]-'i'+2);
            if (reszeredmeny == 2) {
                iplaces.push_back(j+1);
            }
        }
        if (iplaces.size() == 0){
            g << "Case #" << i+1 << ": NO" << endl;
            continue;
        }

        reszeredmeny = 1;
        for (int k=L*X-1;k>=2;--k) {
            reszeredmeny = multiply(tmp[k]-'i'+2, reszeredmeny);
            if (reszeredmeny == 4) {
                kplaces.push_back(k-1);
            }
        }

        g << "Case #" << i+1 << ": ";
        if (iplaces.size() > 0 && kplaces.size() > 0 )
        {
            bool megoldas = false;
            for (int j=0;j<iplaces.size() && !megoldas;++j) {
                reszeredmeny = 1;
                int tmppoz = iplaces[j];
                for (int k=0;k<kplaces.size() && !megoldas;++k) {
                    if (kplaces[k] < iplaces[j]) continue;
                    while (tmppoz <= kplaces[k]) {
                        reszeredmeny = multiply(reszeredmeny, tmp[tmppoz]-'i'+2);
                        ++tmppoz;
                    }
                    megoldas = reszeredmeny == 3;
                }
            }

            if (megoldas) g << "YES" << endl;
            else g << "NO" << endl;
        }
        else
        {
            g << "NO" << endl;
        }

//        bool megoldas = false;
//        int reszeredmeny = 1;
//        int j,k,l;
//        for (j=0;j<L*X && !megoldas;++j) {
//            while (reszeredmeny != 2 && j < L*X) {
//                reszeredmeny = multiply(reszeredmeny, tmp[j]);
//                ++j;
//            }
//            if (reszeredmeny != 2) break;
//            reszeredmeny = 1;
//            k = j;
//            while (k<L*X && !megoldas) {
//                while (reszeredmeny != 3 && k < L*X) {
//                    reszeredmeny = multiply(reszeredmeny, tmp[k]);
//                    ++k;
//                }
//                if (reszeredmeny != 3) break;
//                reszeredmeny = 1;
//                l = k;
//                while (l < L*X) { reszeredmeny = multiply(reszeredmeny,tmp[l]); ++l; }
//                megoldas = reszeredmeny == 4;
//                reszeredmeny = 3;
//            }
//            reszeredmeny = 2;
//        }
//

    }
    return 0;
}
