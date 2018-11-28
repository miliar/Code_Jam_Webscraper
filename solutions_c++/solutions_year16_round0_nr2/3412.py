#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    int t,n,i,j,k,ans;
    char s[100];
    cin>>t;
    for(i=1;i<=t;++i)
    {
    ans=0;
    cin>>s; 
    n=strlen(s);   
    if(s[n-1]=='-')
    k=1;
    else
    k=0;
    for(j=0;j<n-1;++j)
    if(s[j]!=s[j+1])
    ++ans;             
    ans=ans+k;
    cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
