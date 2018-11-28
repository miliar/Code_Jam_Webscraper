#include<bits/stdc++.h>
typedef long long ll;
using namespace std;

void algo1()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output1.txt", "w", stdout);
    int T;
    cin >> T;
    for(int CNO = 1; CNO <= T; CNO++)
    {
        string S;
        int K;
        cin >> S >> K;
        int n = S.length();
        int flips = 0;
        bool notps = false; 
        for(int i = 0; i < n; i++)
            if (S[i] == '-')
            {
                bool f = true;
                int cnt = 0, fno = i;
                for(int j = i; j < i+K; j++)
                    if(S[j] == '-' && f)
                        cnt++;
                    else
                    {
                        if (f)
                        {
                            f = false;
                            fno = j;
                            
                        }    
                        if (S[j] == '+')
                            cnt++;
                    }
                if (cnt != K || fno+K > n)
                {
                    notps = true;
                    break;
                }
                for(int j = i; j < max(i, fno)+K; j++)
                    S[j] = '+';
                flips++;
                if (i != fno)
                    flips++;
            }
        if (notps)
            printf("Case #%d: IMPOSSIBLE\n", CNO);
        else
            printf("Case #%d: %d\n", CNO, flips);
    }
}
void algo2()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int CNO = 1; CNO <= T; CNO++)
    {
        string S;
        int K;
        cin >> S >> K;
        int N = S.length();
        bool not_possible = false;
        int flips = 0;
        for(int i = 0; i < N; i++)
        {
            if(S[i] == '-')
            {
                for(int j = i; j < min(N, i+K); j++)
                    if (S[j] == '-')
                        S[j] = '+';
                    else
                        S[j] = '-';
                if (i+K > N)
                {
                    not_possible = true;
                    break;
                }    
                flips++;
            }
        }
        if (not_possible)
            printf("Case #%d: IMPOSSIBLE\n", CNO);
        else
            printf("Case #%d: %d\n", CNO, flips);
    }
}

int main()
{
    //algo1();
    algo2();
    return 0;
}