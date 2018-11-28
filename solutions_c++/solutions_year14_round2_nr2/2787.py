#include<iostream>
using namespace std;
#include<stdio.h>
int main()
{
    int t,o;
    cin>>t;
    for(o=1;o<=t;o++)
    {
        long long int a,b,k;
        cin>>a>>b>>k;
        int i,j,temp,flag=0,count=0;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                temp=(i&j);
                if(temp<k)
                {

                    count++;
                }
            }
        }
       cout<<"Case #"<<o<<":"<<" "<<count<<"\n";

    }

}
