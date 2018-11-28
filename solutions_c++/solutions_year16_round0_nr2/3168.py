#include <bits/stdc++.h>
using namespace std;
string st ;

void solve(int tt)
{
    string s;
    cin >> s;
    st = s[0] ;
    for(int  i = 1 ; i < (int)s.size() ; i++) if( s[i] != s[i-1]) st += s[i];
    int ans=0;
    while(st.size())
    {
        while(st.size()&&st[st.size()-1]== '+' ) st.erase(st.size()-1);
        if(!st.size()) break;
        if(st[0]=='-')
        {
            ans++;
            reverse(st.begin(),st.end());
            for(int i = 0 ; i < (int)st.size() ; i++) if(st[i]=='+') st[i] = '-' ;else st[i] = '+';
        }
        else
        {
         st[0]='-';
         ans++;
        }
    }


    cout<<"Case #"<<tt<<": "<<ans<<endl;



}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tt = 1 ; tt <= t ; tt++)
        solve(tt);

    return 0;
}
