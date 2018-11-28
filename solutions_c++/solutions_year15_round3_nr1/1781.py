#include <iostream>
#include <cstdio>
using namespace std;
int t,r,c,w;
int megoldas[100];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
    cin>>r>>c>>w;
    if(w==1 || w==c) megoldas[i]=c;
    else{
    if(c%w==0) megoldas[i]=c/w+w-1;
    else    megoldas[i]=c/w+w;
    }

    }
    freopen("output.txt","w",stdout);
    for(int i=1;i<=t;i++) cout<<"Case #"<<i<<": "<<megoldas[i]<<endl;
    return 0;
}
