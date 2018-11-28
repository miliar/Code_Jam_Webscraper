#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <set>

using namespace std;

int T;
long long L, X;
int D;
string S, SS;
int P[200100], NP[200100];

int Product[4][4] = {{0,1,2,3}, {1,0,3,2}, {2,3,0,1}, {3,2,1,0}};
int NegProduct[4][4] = {{1,1,1,1}, {1,-1,1,-1}, {1,-1,-1,1}, {1,1,-1,-1}};
int NegQuotient[4][4] = {{1,-1,-1,-1}, {1,1,1,-1}, {1,-1,1,1}, {1,1,-1,1}};

int main()
{
    //freopen("input_large.txt", "r", stdin);
    //freopen("output_large.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> L >> X >> S;
        for (int i = 0; i < S.length(); ++i)
        {
            if (S[i] == 'i') S[i] = '1';
            else if (S[i] == 'j') S[i] = '2';
            else S[i] = '3';
        }
        SS = S;

        if (X <= 12LL) D = (int)X;
        else D = 12 + (int)(X % 4LL);

        for (int i = 1; i < D; ++i)
            S = S + SS;

        P[0] = S[0] - '0';
        NP[0] = 1;
        //cout << D << " " << S.length() << endl;
        //cout << "RES: " << NP[0] << " " << P[0] << endl;
        for (int i = 1; i < S.length(); ++i)
        {
            NP[i] = NP[i-1] * NegProduct[P[i-1]][S[i] - '0'];
            P[i] = Product[P[i-1]][S[i] - '0'];
            //cout << "RES: " << NP[i] << " " << P[i] << endl;
        }

        bool OK = false;
        for (int i = 1; i <= S.length() - 2; ++i)
        {
            if (OK) break;
            if (NP[i-1] != 1 || P[i-1] != 1) continue;
            //cout << "OK" << endl;
            for (int j = i+1; j <= S.length() - 1; ++j)
            {
                if (OK) break;
                //cout << Product[P[j-1]][P[i-1]] << " " << NP[j-1]*NegQuotient[P[j-1]][P[i-1]] << endl;
                if (Product[P[j-1]][P[i-1]] != 2 || NP[j-1]*NegQuotient[P[j-1]][P[i-1]] != 1) continue;
                OK = Product[P[S.length()-1]][P[j-1]] == 3 && NP[S.length()-1]*NegQuotient[P[S.length()-1]][P[j-1]] == 1;
            }
        }

        if (OK)
            cout << "Case #" << t << ": YES" << endl;
        else
        cout << "Case #" << t << ": NO" << endl;
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
