#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>

typedef long long ll;
using namespace std;

ifstream fin("B-large.in");
ofstream fout("B.out");

int A, B, K, T;
ll All[50], DP[50][2][2][2];

int main()
{
    fin >> T;

    All[0] = 4;

    for(int i = 1; i <= 30; i++)
        All[i] = All[i-1] * 4;

    for(int t = 1; t <= T; t++)
    {
        fin >> A >> B >> K;

        for(int i = 0; i < 50; i++)
            for(int j = 0; j < 2; j++)
                for(int k = 0; k < 2; k++)
                    for(int l = 0; l < 2; l++)
                        DP[i][j][k][l] = 0;

        DP[30][0][0][0] = 1;

        A--, B--, K--;

        for(int b = 29; b >= 0; b--)
            for(int ba = 0; ba <= 1; ba++)
                for(int bb = 0; bb <= 1; bb++)
                {
                    int bit = ba&bb;
                    int need_a = 0, need_b = 0, need_k = 0;

                    if(ba && !(A & (1 << b)))
                        need_a = 1;
                    if(bb && !(B & (1 << b)))
                        need_b = 1;
                    if(bit && !(K & (1 << b)))
                       need_k = 1;

                    int curr_a = 0, curr_b = 0, curr_k = 0;

                    if(ba == 0 && (A & (1 << b)))
                        curr_a = 1;
                    if(bb == 0 && (B & (1 << b)))
                        curr_b = 1;
                    if(bit == 0 && (K & (1 << b)))
                        curr_k = 1;

                    for(int prev_a = (curr_a || !need_a ? 0 : 1); prev_a <= 1; prev_a++)
                        for(int prev_b = (curr_b || !need_b ? 0 : 1); prev_b <= 1; prev_b++)
                            for(int prev_k = (curr_k || !need_k ? 0 : 1); prev_k <= 1; prev_k++)
                            {
                                DP[b][curr_a|prev_a][curr_b|prev_b][curr_k|prev_k] += DP[b+1][prev_a][prev_b][prev_k];
                                //cout << "DP[" << b << "][" << (curr_a|prev_a) << "][" << (curr_b|prev_b) << "] = " << DP[b][curr_a|prev_a][curr_b|prev_b] << "\n";
                            }

                    //getchar();
                }

        ll ans = 0;

        for(int i = 0; i < 2; i++)
            for(int j = 0; j < 2; j++)
                for(int k = 0; k < 2; k++)
                    ans += DP[0][i][j][k];

        cout << "Case #" << t << ": " << ans << "\n";
        fout << "Case #" << t << ": " << ans << "\n";
    }
}
