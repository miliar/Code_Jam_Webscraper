#include <stdio.h>
#include <string.h>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#define PI acos(-1.0)
#define M 1000005  //10^6
#define eps 1e-8
#define LL long long
#define moo 1000000007
#define INF -999999999
using namespace std;
char s[2000];

int main()
{
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);
    int T;
    scanf("%d",&T);
    int dd=T;
    while(T--)
    {
        int n;
        scanf("%d",&n);
        int ans=0;
        int sum=0;
        scanf("%s",s);
        for(int i=0;i<=n;i++)
        {
            if(s[i]=='0')
                continue;
            if(sum<i)
            {
                ans+=(i-sum);
                sum=i;
            }
            sum+=(s[i]-'0');
        }
        cout<<"Case #"<<dd-T<<": ";
        cout<<ans<<endl;
    }
}
