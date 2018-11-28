#include<iostream>
#include<stdio.h>
using namespace std;
bool filetest=false;
int main()
{
    char s[1001],a[3000];
    int t,i,k,l=1500,r=1500;
    if(filetest)
    {
        freopen("A-large.in","r",stdin);
        freopen("outlastword2.txt","w",stdout);
    }
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>s;
        l=r=1500;
        for(i=0;s[i]!='\0';i++)
        {
            if(l==r)
            {
                a[l]=s[i];
                l--;
                r++;
            }
            else if(s[i]>=a[l+1])
            {
                a[l]=s[i];
                l--;
            }
            else
            {
                a[r]=s[i];
                r++;
            }
        }
        for(i=l+1;i<r;i++)
            s[i-l-1]=a[i];
        s[i]='\0';
        cout<<"Case #"<<k<<": "<<s<<endl;
    }
    return 0;
}
