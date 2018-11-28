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
inline int segments(string s)
{
    int l=s.length();
    int res=1;
    for(int i=0;i<l;++i)
        if(s[i]!=s[i+1])
            ++res;
    return res-1;
}

int main()
{
    int T;
  cin>>T;
    for(int t=1;t<=T;++t)
    {
        string s;
        cin>>s;
        int ans=segments(s);
        if(s[0]=='+'&&s[s.length()-1]=='+')
            ans--;
        else if(s[0]=='-'&&s[s.length()-1]=='+')
            --ans;
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
	return 0;
}

