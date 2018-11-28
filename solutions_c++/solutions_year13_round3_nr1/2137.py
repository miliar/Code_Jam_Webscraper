#include <iostream>
#include<string>
#include<stdio.h>
using namespace std;

int main()
{
    int t,n,i,j,k,l;
    string str;
    int a[100];
    cin>>t;
    int p=1;
    while(t--)
    {
        cin>>str>>n;
        int len=str.length();


        for(i=0;i<len;i++)
        {
            if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
            a[i]=0;
            else
            a[i]=1;
        }
        int cnt=0,c;
        if(n>1)
        for(i=0;i<=len-n+1;i++)
        for(j=i+n;j<=len;j++)
        {
            c=1;
            for(k=i+1;k<j;k++)
        {

            if(a[k]==a[k-1]&&a[k]==1)
            c++;
            if(c>=n)
            {
            cnt++;break;}
            if(a[k]!=a[k-1]&&a[k]==0)
            c=1;
        }

        }
        if(n==1)
        for(i=0;i<len;i++)
        if(a[i]==1)
        cnt++;
      //Case #1: 4
      printf("Case #%d: %d\n",p,cnt);
      p++;




    }
    return 0;
}
