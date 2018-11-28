#include<iostream>
#include<stdio.h>
using namespace std;
bool a[10]= {false};
bool test=true;
void checknum(long long n)
{
    char s[10];
    int i;
    sprintf(s,"%lld",n);
    for(i=0; s[i]!='\0'; i++)
        a[s[i]-48]=true;
}
int main()
{
    long long n,i,t,j,k;
    if(!test)
    {
        freopen("A-large.in","r",stdin);
        freopen("outgooglelarge.txt","w",stdout);
    }
    cin>>t;
    for(k=1; k<=t; k++)
    {
        j=1;
        cin>>n;
        for(i=0; i<10; i++)
            a[i]=false;
        if(n!=0)
        {
            while(!(a[0]&&a[1]&&a[2]&&a[3]&&a[4]&&a[5]&&a[6]&&a[7]&&a[8]&&a[9]))
            {
                checknum(n*j);
                j++;
            }
            j--;
            cout<<"Case #"<<k<<": "<<n*j<<endl;
        }
        else
            cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
    }
    return 0;
}
