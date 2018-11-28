#include <bits/stdc++.h>
#define rep(I, N) for (int I = 0; I < (N); ++I)
using namespace std;
int main()
{

    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
int t;
cin>>t;
for(int z=1;z<=t;z++)
{
    int l,tot=0,ans=0;
    string s;
    cin>>l>>s;
    rep(i,s.size()-1)
    {
        tot+=s[i]-'0';
        if(s[i+1]-'0') if(tot<i+1) {ans+=i+1-tot;tot+=i+1-tot;}

    }
    cout<<"Case #"<<z<<": "<<ans<<endl;

}
return 0;
}
