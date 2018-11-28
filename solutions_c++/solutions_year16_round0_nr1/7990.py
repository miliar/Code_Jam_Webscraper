#include <iostream>
#include<stdio.h>
#include<math.h>
#include <algorithm>  
#include<string.h>
long long x[1000000]={0};
//char l[20000000]={'r'},p[20000000]={'r'};
 
 
using namespace std;
 
int main()
{
    long long t,n,i,j,k,l,m,flag,num,sum,u,a[100],r;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        for(r=0;r<=9;r++)
        {
            a[r]=0;
        }
        flag=0;
        cin>>n;
        cout<<"Case #"<<i<<": ";
        if(n==0)
        {
            cout<<"INSOMNIA";
        }
        else
        {
            //cout<<"here";
        j=1;
        k=1;
        l=1;
        while(flag!=1)
        {
            num=j*n;
            l=1;
            //cout<<"num="<<num;
            u=num;
            while(l!=0)
            {
                k=num%10;
                l=num/10;
                a[k]=1;
                num=l;
            }
            
            sum=0;
            for(m=0;m<=9;m++)
            {
                //cout<<a[m]<<" ";
                sum=sum+a[m];
                
            }
            if(sum==10)
                {
                    flag=1;
                }
            //cout<<"sum="<<sum<<"\n";
            j=j+1;
            
        }
        if(flag==1)
        {
            cout<<u;
        }
        }
        
        cout<<"\n";
        
    }

return 0;
}