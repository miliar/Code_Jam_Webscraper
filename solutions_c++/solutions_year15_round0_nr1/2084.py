#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;  cin>>t;
    for( int tt=1; tt<=t; ++tt ) {
        int smax;   string s;   cin>>smax>>s;
        assert(s.length()==smax+1);
        int cnt=s[0]-'0',ans=0;
        for( int shyness=1; shyness<=smax; ++shyness ) {
            if( cnt < shyness ) {
                cnt++;
                ans++;
                shyness--;
            } else {
                cnt+=s[shyness]-'0';
            }
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
