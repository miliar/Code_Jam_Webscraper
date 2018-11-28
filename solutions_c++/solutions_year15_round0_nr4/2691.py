#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
int t;cin>>t;
for(int ss=1;ss<=t;ss++)
{
    int x,r,c;
    cin>>x>>r>>c;
    string s;
    if((r*c)%x) s="RICHARD";
    else
    {
        if (x==1||x==2) s="GABRIEL";
        else
        {
            int m=min (r,c);int mx=max(r,c);
            if (m==1) s="RICHARD";
            else
            {
                switch(x)
                {
                case 3: s="GABRIEL"; break;
                case 4:
                    if(m==2) s="RICHARD";
                    else s="GABRIEL";
                    break;
                }
            }
        }
    }
    cout<<"Case #"<<ss<<": "<<s<<endl;
}
}
