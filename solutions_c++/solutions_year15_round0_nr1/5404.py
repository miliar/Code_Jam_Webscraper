#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<map>
#include<list>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<set>




#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define all(s) s.begin(),s.end()
#define pb push_back
#define mp make_pair
#define sd(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define pd(x) printf("%d",x)
#define ll long long
const int mod = ((1E9)+7);
const int intmax = ((1E9)+7);




#ifndef ONLINE_JUDGE
#define TRACE
#endif
#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
#endif

using namespace std;







string s;


int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    int test,a,b,c;
    sd(test);

    int case_=1;
    while(test--)
    {

        sd(c);
        cin>>s;
        ll count=0;
        ll ans=0;

        for(ll i=0;i<(ll)s.size();i++)
        {
            if(s[i]=='0') continue;

            if(count>=i)
                count+=(ll)(s[i]-'0');
            else
            {
                ans+=i-count;
                count=i+(s[i]-'0');
            }

        }

        cout<<"Case #"<<case_<<": "<<ans<<endl;
        case_++;

    }

    return 0;


}
