#include <bits/stdc++.h>

using namespace std;

typedef double D;
typedef long double LD;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<LD,LD> PLD;

#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define ALL(x) (x).begin(), (x).end()


int main()
{  
    int T;
    scanf("%d",&T);
    getchar();
    for(int i = 1; i<=T; ++i)
    {
        vector<char> ans;
        while(1)
        {
            char c;
            scanf("%c",&c);
            if( c == '\n' ) break;
            if( ans.empty() ) ans.PB(c);
            else
            {
                if( c >= ans[0] ) ans.insert(ans.begin(),c);
                else ans.PB(c);
            }
        }
        printf("Case #%d: ",i);
        for(int j = 0,n = ans.size(); j<n; ++j)
        {
            printf("%c",ans[j]);
        }
        printf("\n");
    }
}

