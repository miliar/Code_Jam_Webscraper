// User :: lovelotus ( Prem Kamal )

//#include<bits/stdc++.h>
//#define _ ios_base::sync_with_stdio(0);cin.tie(0);

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<cassert>
#include<iostream>
#include<algorithm>
#include<string>
#include<utility>
#include<cctype>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#include<set>
#include<deque>

#define lli long long int
#define ulli unsigned long long int
#define F first
#define S second
#define pii pair<int,int>
#define pip pair<int,pii>
#define pis pair<int,string>
#define pll pair<lli,lli>

using namespace std;

int n;
char s[1001];

int main()
{
    freopen("C:\\Users\\lovelotus\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\lovelotus\\Desktop\\output.txt","w",stdout);
    int i,j,t;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %s",&n,s);
        int cnt=0,ans=0;
        for(j=0;j<=n;j++)
        {
            cnt+=(s[j]-48);
            if(cnt<=j)
            {
                ans++;
                cnt++;
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
