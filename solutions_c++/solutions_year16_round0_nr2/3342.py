#include<cstdio>
#include<cstdlib>
#include<time.h>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>

//#include<bits/c++std.h>

#define Size 1000005
#define inf 2e9
#define INF 2e18
#define LL long long int
#define i64 __int64
#define ULL unsigned long long
#define Mod 1000000007
#define pi 4*atan(1)
#define eps 1e-8
#define lson now*2,l,l+(r-l)/2
#define rson now*2+1,l+(r-l)/2+1,r
#define Max(a,b) (a)>(b)?(a):(b)
using namespace std;
int n,m,k;
int ql,qr,pos;

int main()
{
    #ifndef ONLINE_JUDGE
//        freopen("input.txt","r",stdin);
//        freopen("output.txt","w",stdout);
    #endif // ONLINE_JUDGE
    int t;
    int x,y,z;
    string s;
    int Case=0;
    cin>>t;
    while(t--)
//    while(scanf("%d",&n)==1)
    {
        s.clear();
        cin>>s;
        printf("Case #%d: ",++Case);
        int ans = 0;
        if(s[0] == '-')
        {
            ans++;
        }
        int st = 0;
        for(int i=0;i<s.size();++i)
        {
            if(s[i] == '+')
            {
                st = i;
                break;
            }
        }
        int flag1 = 0;
        for(int i=st;i<s.size();++i)
        {
            if(s[i] == '+')
                flag1 = 1;
            else if(s[i] = '-')
            {
                if(flag1)
                {
                    ans += 2;
                    flag1 = 0;
                }
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}

