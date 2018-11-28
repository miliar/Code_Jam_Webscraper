#include<iostream>
using namespace std;
int main()
{
    int k,t,c,s,i;
    cin>>t;
    for(i=1;i<=t;++i)
    {
    cin>>k>>c>>s;
    if(k==s)
    {
            cout<<"Case #"<<i<<": ";
            for(i=1;i<=s;++k)
            cout<<i<<" ";
            cout<<endl;
            }
            }
    return 0;
}
