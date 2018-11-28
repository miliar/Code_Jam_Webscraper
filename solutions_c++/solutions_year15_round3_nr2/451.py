#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
string s1,s2;
int K,L,S;
double ans;
int maxn;


void dfs(string s,int t)
{
    if(t == S)
    {
        int cnt = 0;
        for(int i=0;i<s.size();i++)
        {
            bool flag = true;
            for(int j=0;j<s2.size();j++)
                if(s[i+j] != s2[j])
                {
                    flag = false;
                    break;
                }
            if(flag)
                cnt++;
        }
        maxn = max(maxn,cnt);
        ans += 1.0*cnt/pow(1.0*K,1.0*(S));
    }
    else
    {
        for(int i=0;i<s1.size();i++)
        {
            dfs(s+s1[i],t+1);
        }
    }
}

int main()
{
    freopen("C:\\codejam15\\B-small-attempt0.in","r",stdin);
    freopen("C:\\codejam15\\B-small-attempt0.out","w",stdout);
    int T,cas=1;
    int n,m;
    scanf("%d",&T);
    while(T--)
    {
        ans = 0;
        maxn = 0;
        scanf("%d %d %d",&K,&L,&S);
        cin>>s1>>s2;
        dfs("",0);
        printf("Case #%d: %.8lf\n",cas++,1.0*maxn - ans);
    }
    return 0;
}
