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
    ifstream IF;
    ofstream OF;
    IF.open("input.txt");
    OF.open("output.txt");

    int t,i,j,k,w,ans1,ans2,d,mx; IF >> t;
    for(w=1;w<=t;w++)
    {
        OF << "Case #" << w << ": ";
        int n; IF >> n;
        int a[n];
        for(i=0;i<n;i++)
            IF >> a[i];
        ans1=0;ans2=0;mx=0;d=0;
        for(i=1;i<n;i++)
        {
            if(a[i]<a[i-1])
                ans1+=a[i-1]-a[i];
        }
        for(i=1;i<n;i++)
        {
            if(a[i]<a[i-1])
                d=a[i-1]-a[i];
            mx=max(mx,d);
        }
        for(i=0;i<n-1;i++)
        {
            ans2+=min(a[i],mx);
        }
        OF << ans1 << " " << ans2 << endl;
    }
    return 0;
}



