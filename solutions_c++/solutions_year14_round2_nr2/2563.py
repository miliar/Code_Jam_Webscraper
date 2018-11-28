#include<iostream>
#include<stdio.h>
using namespace std;
int t,a,b,k;bool visited[1000];
int main()
{
    freopen("a.txt","r",stdin);
    freopen("test.txt","w",stdout);
    cin>>t;
    int i,ii,j,c;
    for(ii=1;ii<=t;ii++)
    {
        cin>>a>>b>>k;
        int count=0;
        for(i=0;i<a;i++)
        for(j=0;j<b;j++)
        {
            c=i;c&=j;if(c<k)count++;
        }
        cout<<"Case #"<<ii<<": "<<count<<endl;
    }
}
