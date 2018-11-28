#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int rekursija(vector<int> v, int D) {
    //cout << D << endl;
    sort(v.begin(), v.end());
    if (v[D - 1] <= 1) {
        return 1;
    }
    else {



        vector<int> naujas = v;
        //naujas[D - 1] = (naujas[D - 1] + 1) / 2;
        if (naujas[D - 1] % 2 == 1) {
            naujas.push_back(naujas[D - 1]/2 + 1);
        }
        else {
            naujas.push_back(naujas[D - 1]/2);
        }
        naujas[D - 1] /= 2;

        if (v[D - 1] == 9) {
            vector<int> kitas = v;
            kitas[D - 1] = 3;
            kitas.push_back(6);
            return min(v[D - 1], 1 + min(rekursija(naujas, D + 1), rekursija(kitas, D + 1)));

        }

        else return min(v[D - 1], 1 + rekursija(naujas, D + 1));
    }
}

int main()
{
    freopen("pancakes.in", "r", stdin);
    freopen("pancakes.out", "w", stdout);

    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int D;
        cin >> D;
        int masyvas[D];
        for (int d = 0; d < D; d++) {
            cin >> masyvas[d];
        }
        sort(masyvas, masyvas + D);




        vector<int> esmes;

        int masyviuks[D];
        for (int d = 0; d < D; d++) {
            masyviuks[d] = masyvas[d];
            esmes.push_back(masyvas[d]);
        }



        /*
        int minites = 100000;
        for (int m = 0; m < 9; m++) {






            int sk = m;
            while (sk > 0) {
                masyviuks[D - 1]++;
                masyviuks[D - 1] /= 2;
                sort(masyviuks, masyviuks + D);
                sk--;
            }
            minites = min(minites, m + masyviuks[D - 1]);
        }


        /*
        while (true) {

            if (masyvas[D - 1] < 3) {
                minutes += masyvas[D - 1];
                break;
            }

            minutes++;

            int paskmr = masyvas[D - 1] / 2;
            if (masyvas[D - 1] % 2 == 1)
                paskmr++;


            if (max(paskmr, masyvas[D - 2]) + 1 > masyvas[D - 1]) {
                masyvas[D - 1] = paskmr;
                sort(masyvas, masyvas + D);
            }
            else {
                for (int u = 0; u < D; u++) {
                    masyvas[u]--;
                }


            }

        }
        */

        cout << "Case #" << t + 1 << ": " << rekursija(esmes, D) << endl;
    }

    return 0;
}
