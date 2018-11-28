#include<bits/stdc++.h>
#define pb push_back
#define read freopen("input.txt","r",stdin)
#define write freopen("output.txt","w",stdout)
#define rev(s) std::reverse(s.begin(), s.end())
//#define up std::transform(s.begin(), s.end(), s.begin(), ::toupper);
///string sb=s.substr(1,3);

#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*b)/gcd(a,b)

#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max4(a,b,c,d) max(max(a,b),max(c,d))

#define INF (1<<28)
#define mod 1000000007

#define tbeg clock_t _t=clock();
#define tend cout << "\n\nTime: " << (double)(clock()-_t)/CLOCKS_PER_SEC;

#define PI 2*acos(0.0)
#define low std::transform(s.begin(), s.end(), s.begin(), ::tolower);
#define n2s(n) stringstream ss; ss<<n; string Get=ss.str()
#define CC(x) cout<<(x)<<endl
#define srt sort(a,a+n)
#define rep(i,n) for(int i=0;i<n;i++)
#define per(i,n) for(int i=n-1;i>=0;i--)

typedef long long LL;

using namespace std;

int main()
{
    read;
    write;
    LL T, tc = 0, l, ans;
    string s;
    cin>>T;
    while(T--)
    {
        cin>>s;
        l = s.size();
        ans = 1;
        rep(i,l-1) { if(s[i]!=s[i+1]){ans++;} }
        if(s[l-1]=='+'){ans = ans - 1;}
        cout<<"Case #"<<++tc<<": "<<ans<<endl;
    }
    return 0;
}

