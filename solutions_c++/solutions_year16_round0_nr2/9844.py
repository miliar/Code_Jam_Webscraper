#include <bits/stdc++.h>
using namespace std;

vector< char > v;
string s;

int main ()
{
    freopen("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);
    int t,cs = 1; cin>>t;
    while(t--)
    {
        cin>>s;
        v.clear();
        for(int i=0; i<s.size(); i++) v.push_back(s[i]);
        int ans = 0;
        int len = s.size();
        int id = len;
        for(int i = len-1; i>=0; )
        {
            if(i==0 && v[i]=='+'){
                    i--;
            }
            else if(i==0 && v[i]=='-'){
                    ans++;
                    i--;
            }
            else if(v[i]=='+') i--;
            else
            {
                int lst = -1;
                for(int j = i; j>=0; j--)
                {
                    if(v[j]=='+')
                    {
                        lst = j; break;
                    }
                }
                if(lst == -1) i = 0;
                else
                {
                    i = lst;
                    ans+=2;
                }
            }
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
        cs++;
    }
    return 0;
}
