nclude<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
int main()
{
        char filename[] = "a.out";
        ofstream fout(filename);
        int T;
        cin >> T;
        for (int i = 1; i <= T; i++)
        {
                int N, sum = 0, ans = 0;
                cin >> N;
                string S;
                cin >> S;
                for (int j = 0; j <= N; j++)
                {
                        if (S[j] != 0 && sum < j)
                        {
                                ans += (j - sum);
                                sum = j + S[j] - '0';
                        }
                        else
                                sum += S[j] - '0';
                }
                fout<<"Case #" << i << ": " << ans <<endl;
        } 
        return 0; 
}  
