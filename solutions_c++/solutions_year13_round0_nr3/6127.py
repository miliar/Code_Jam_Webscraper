#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int main()
{
    long long int t;
    double low,high;
    cin>>t;
    int flag=0;

    for(long long int i=0;i<t;i++)
    {
        cin>>low;
        cin>>high;
        flag=0;long long int count=0;

        for(long long int j=(long long int) sqrt(low); j<=(long long int) sqrt(high);j++)
        {
            if((j*j)<low)continue;

            long long int pal=j*j;
            string s;
            flag=0;
            while(pal!=0)
            {
                long long int rem=pal%10;
                pal=pal/10;
                s=s+char(rem+48);
            }

            for(int k=0;k<s.length()/2; k++)
            {
                if(s[k]!=s[s.length()-k-1])flag=1;
            }

            string s1;
            int m=j;
            while(m!=0)
            {
                long long int rem=m%10;
                m=m/10;
                s1=s1+char(rem+48);
            }

            for(int k=0;k<s1.length()/2; k++)
            {
                if(s1[k]!=s1[s1.length()-k-1])flag=1;
            }


            if(flag==0)count++;

        }

        cout<<"Case #"<<i+1<<": "<<count<<endl;
    }
}
