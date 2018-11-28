#include <iostream>
#include <cstdio>
using namespace std;

int emberek[2000],valaszok[2000];
int t,s,szaml,k;
string str;
int main()
{
    //freopen("A-large.in","r",stdin);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
    k=0;
    cin>>s;
    cin>>str;
    for(int i=0;i<=s;i++)
    {
        emberek[i]=str[i]-48;
    }
    szaml=emberek[0];
    for(int i=1;i<=s;i++)
    {
        if(szaml<i)
        {
            k+=i-szaml;
            szaml+=i-szaml;
        }
        szaml+=emberek[i];
    }
    valaszok[i]=k;
    }
    //freopen("output.in","w",stdout);
    for(int i=1;i<=t;i++)
    {
    cout<<"Case #"<<i<<": "<<valaszok[i]<<endl;
    }

    return 0;
}
