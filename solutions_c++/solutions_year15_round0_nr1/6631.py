#include<bits/stdc++.h>
#define D 1000000007
#define gcd __gcd
#define getcx getchar
#define pc putchar
#define get(x) scanf("%d",&x)
#define getl(x) scanf("%lld",&x)
#define print(x) printf("%d\n",x)
#define printl(x) printf("%lld\n",x)
#define bitcount __builtin_popcount
using namespace std;
typedef long long ll;
int main()
{
    int t,i,j; get(t);
    for(j=1;j<=t;j++)
    {
        int Smax; get(Smax);
        string s; cin >> s;
        int ans=0,sum=0;
        for(i=0;i<=Smax;i++)
        {
            if(sum<i && s[i]!='0')
            {
                ans+=i-sum;
                sum+=i-sum;
            }
            sum+=s[i]-'0';
        }
        cout << "Case #" << j << ": " << ans << endl;
    }
    return 0;
}

