#include<iostream>
#include<cstring>
#include<string>
using namespace std;
int main()
{
    int t,l,k,j,p,sum;
    char s[100];
    cin>>t;
    p=1;
    while(t--)
    {
    sum=0;
    cin>>s;
    l=strlen(s);   
    if(s[l-1]=='-')
    k=1;
    else
    k=0;
    for(j=0;j<l-1;++j)
    if(s[j]!=s[j+1])
    ++sum;             
    sum+=k;
    cout<<"Case #"<<p<<": "<<sum<<endl;
    p++;
    }
    return 0;
}
