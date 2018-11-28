#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <algorithm>
#define ll long long
using namespace std;

vector<string>f,s;

int main()
{
    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);

    int a,b,c,d,e,x,y,z,n;

    int t;

    cin>>t;

    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);

        cin>>n;

        string chi,chj;

        cin>>chi;
        cin>>chj;

        f.clear();
        s.clear();

        string st;
        st="";

        for(a=0;a<chi.size();a++)
        {
            if(st=="")
            {
                st=st+chi[a]; continue;
            }
            if(st[0]==chi[a])
            {
                st=st+chi[a];
                continue;
            }
            f.push_back(st);
            st=chi[a];
        }f.push_back(st);

        st="";

        for(a=0;a<chj.size();a++)
        {
            if(st=="")
            {
                st=st+chj[a]; continue;
            }
            if(st[0]==chj[a])
            {
                st=st+chj[a];
                continue;
            }
            s.push_back(st);
            st=chj[a];
        }s.push_back(st);

        if(f.size()!=s.size())
        {
            cout<<"Fegla Won"<<endl;
            continue;
        }

        int ans=0;

        for(a=0;a<f.size();a++)
        {
            if(f[a][0]!=s[a][0]) break;
            b=f[a].size();
            c=s[a].size();
            ans=ans+abs(b-c);
        }
        if(a==f.size()) cout<<ans<<endl;
        else cout<<"Fegla Won"<<endl;
    }

    return 0;
}
