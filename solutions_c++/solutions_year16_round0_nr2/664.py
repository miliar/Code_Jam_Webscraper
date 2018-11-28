#include <fstream>
#include <queue>
#include <vector>

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

const int INF = 0x3f3f3f3f;

/*const int CM = 20;

int dp10[(1 << CM) + 20];
void solve10()
{
    memset(dp10, INF, sizeof(dp10));
    queue<int> Q;
    Q.push(0);
    dp10[0] = 0;
    
    int now[CM];
    int flip[CM];
    
    while (!Q.empty()) // LSB is top
    {
        int conf = Q.front();
        Q.pop();
        
        for (int i=0; i<CM; i++)
            if ((conf & (1 << i)) != 0)
                now[i] = 1;
            else
                now[i] = 0;
        
        for (int i=1; i<=CM; i++)
        {
            for (int j=0; j<i; j++)
                flip[j] = 1 - now[i - j - 1];
            for (int j=i; j<CM; j++)
                flip[j] = now[j];
            int vec = 0;
            for (int j=0; j<CM; j++)
                vec += (1 << j) * flip[j];
            
            if (dp10[vec] > dp10[conf] + 1)
            {
                dp10[vec] = dp10[conf] + 1;
                Q.push(vec);
            }
        }
    }
}*/

int solve(const string& s)
{
    int n = s.size();
    vector<int> dp(n, 0);
    
    dp[0] = (s[0] == '-' ? 1 : 0);
    for (int i=1; i<n; i++)
        if (s[i] == '+')
            dp[i] = dp[i-1];
        else
            if (s[i-1] == '-')
                dp[i] = dp[i-1];
            else // +-
                dp[i] = dp[i-1] + 2;
    return dp[n-1];
}

int main()
{
    //solve10();
    
    int T;
    f >> T;
    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";
        string s;
        f >> s;
        g << solve(s) << '\n';
    }
    
    f.close();
    g.close();
    return 0;
}