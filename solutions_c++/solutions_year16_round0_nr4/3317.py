#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
using namespace std;
int t,k,c,s;;
int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    cin>>t;
    for(int o=1;o<=t;o++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<o<<": ";
        for(int i=1;i<=s;i++)
        cout<<i<<' ';
        cout<<endl;
    }
    return 0;
}
