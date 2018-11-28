	// #CodeLikeTheMartian
#include <bits/stdc++.h>

#define     MOD       1000000007
#define     mp(a,b)   make_pair(a,b)
#define     pb        push_back
#define     lb        lower_bound
#define     ub        upper_bound
#define     SIZE      1000001
#define     MAX       INT_MAX
#define     fi        first
#define     se        second
#define     fastInput ios::sync_with_stdio(false); cin.tie(0);
using namespace std;

typedef long long int  ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long int ull;
int main()
{
    int T;
    FILE *fp=fopen("A_smallOutput.txt","w");
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        string  s;
        cin>>s;
        int l=s.length();
        string ans;
        char maxa=s[0];
        ans+=s[0];
        for(int i=1;i<l;++i)
            if(s[i]>=maxa)
             {
                 ans=s[i]+ans;
                 maxa=s[i];
             }
            else
                ans+=s[i];
        cout<<"Case #"<<t<<": "<<ans<<endl;
        //fprintf(fp,"Case #%d: %d\n",t,ans);

    }
	return 0;
}

