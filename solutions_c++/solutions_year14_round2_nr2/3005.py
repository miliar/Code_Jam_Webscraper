#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    long long int t,i,j,k;
    long long int n1,n2,cnt=0,a;
    cin>>t;
    for(k=0;k<t;k++)
    {
        cin>>n1>>n2>>a;
        for(i=0;i<n1;i++)
        {

            for(j=0;j<n2;j++)
            {
                if((j&i)<a)
                    cnt++;

            }
        }

       cout<<"Case #"<<k+1<<": "<<cnt<<"\n";
       cnt=0;
      }


    return 0;
}
