#include<iostream>
#include<stdio.h>
using namespace std;
bool filetest=false;
int main()
{
    int n,t,i,j,k,a[200][200],m[2501];
    if(filetest)
    {
        freopen("B-large.in","r",stdin);
        freopen("outrank2.txt","w",stdout);
    }
    cin>>t;
    for(k=1;k<=t;k++)
    {
        for(i=0;i<=2500;i++)
            m[i]=0;
        cin>>n;
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>a[i][j];
                m[a[i][j]]++;
            }
        }
        cout<<"Case #"<<k<<": ";
        for(i=0;i<=2500;i++)
        {
            if(m[i]%2==1)
                cout<<i<<" ";
        }
        cout<<endl;
    }
    return 0;
}
