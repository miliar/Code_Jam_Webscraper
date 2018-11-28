#include <bits/stdc++.h>
using namespace std;
int T,cnt,los,pt;
string asdf;
char curr,first;
char oppos(char f)
{
    if(f=='+')
        return '-';
        return '+';
}
int main()
{
    freopen("output.out","w",stdout);
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>asdf;
        los=0;
        while(true)
{
        pt=0;
        first=asdf[0];
        while(asdf[pt]==first && pt<asdf.size())
        pt++;
        if(pt==asdf.size())
        {
        if(asdf[0]=='-')
        los++;
        break;
        }
        for(int j=0;j<pt;j++)
        asdf[j]=oppos(first);
        los++;
        //cout<<asdf<<endl;
        }
        cout<<"Case #"<<i<<": "<<los<<endl;
        }





    return 0;
}
