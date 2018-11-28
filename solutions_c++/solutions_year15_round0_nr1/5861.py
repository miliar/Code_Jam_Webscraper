#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
int t;cin>>t;
for(int ss=1;ss<=t;ss++)
{
    int sm;string ch; int tab[1200];
    cin>>sm; cin>>ch;
    for(int i=0;i<=sm;i++)
        tab[i]=ch[i]-'0';
    int c=0,s=0;
    for(int i=0;i<=sm;i++)
    {
        if((c<i)&&tab[i]) {s+=(i-c);c+=(i-c);}
        c+=tab[i];
    }
    cout<<"Case #"<<ss<<": "<<s<<endl;
}
}
