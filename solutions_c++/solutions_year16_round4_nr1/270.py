#include <bits/stdc++.h>
typedef long long LL;
const int N = 1e5 + 10;
const int MAXN = 1e9 + 8;

using namespace std;

int n,p,r,s;
bool sign;
char f[N];
char g[N];
char ans[N];

bool mycmp(int x,int y)
{
    for(int i = x;i < y;i++)
    {
        if(f[i] < f[y + i - x]) return false;
        if(f[i] > f[y + i - x]) return true;
    }
    return false;
}

void solve(char S)
{
    f[1] = S;
    for(int i = 1;i <= n;i++)
    {
        for(int j = 2;j <= (1 << i);j += 2)
        {
            if(f[j >> 1] == 'R') g[j] = 'R',g[j - 1] = 'S';
            if(f[j >> 1] == 'S') g[j] = 'S',g[j - 1] = 'P';
            if(f[j >> 1] == 'P') g[j] = 'P',g[j - 1] = 'R';
        }
        for(int j = 1;j <= (1 << i);j++)
          f[j] = g[j];
    }

    int c1 = 0,c2 = 0,c3 = 0;
    for(int j = 1;j <= (1 << n);j++)
    {
        if(f[j] == 'R') c1++;
        if(f[j] == 'P') c2++;
        if(f[j] == 'S') c3++;
    }

    f[(1 << n) + 1] = '\0';
   // printf("%s\n",f + 1);cout<<r<<" "<<p<<" "<<s<<endl;
//cout<<c1<<" "<<c2<<" "<<c3<<endl;

    if(c1 == r && c2 == p && c3 == s)
    {
        for(int i = 1;i <= n;i++)
        { //
            for(int j = 1;j <= (1 << n);j += (1 << i))
            {
                if(mycmp(j , j + (1 << (i - 1)) ) )
                {
                    for(int k = 0;k < (1 << (i - 1));k++)
                      swap(f[j + k] , f[j + k + (1 << (i - 1) )]);
                }
            }
        }
     //   printf("%s\n",f + 1);
        if(sign == false)
        {
            sign = true;
            strcpy(ans + 1,f + 1);
        }
        else
        if(strcmp(f + 1,ans + 1) < 0)
        {
            strcpy(ans + 1,f + 1);
        }
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    for(int i = 1;i <= T;i++)
    {
        cin>>n>>r>>p>>s;
        sign = false;
        solve('R');
        solve('P');
        solve('S');
        printf("Case #%d: ",i);
        if(sign) printf("%s\n",ans + 1);
        else printf("IMPOSSIBLE\n");
    }

    return 0;
}

