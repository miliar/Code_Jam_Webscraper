#include<iostream>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    int i,t,s,k,p,j;
    char a[1000];
    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>s;
        for(i=0;i<=s;i++)
            cin>>a[i];
        k=a[0]-'0';
        p=0;
        for(i=1;i<=s;i++)
        {
            if(k<i)
            {
                p+=i-k;
               // cout<<p<<" ";
                k=i;
            }
            k+=a[i]-'0';
        }
        cout<<"Case #"<<j<<": "<<p<<"\n";
    }
    return 0;
}
