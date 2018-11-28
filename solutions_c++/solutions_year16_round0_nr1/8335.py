#include<bits/stdc++.h>
using namespace std;
int main()
{
//freopen("cj12.in","r",stdin);
//freopen("oj11.txt","w",stdout);
long long t,m;
cin>>t;
for(m=1;m<=t;m++)
{
    long long n;
    cin>>n;
    if(n==0)
    {
        cout<<"Case #"<<m<<": INSOMNIA"<<endl;
    }
    else
    {
        long long  track[10]={0};long long  p=0,k=1,temp,counter=0;
        while(1)
        {
            temp=n*k;
            long long number=temp;
            while(temp!=0)
            {
                if(track[temp%10]==0)
                {
                  track[temp%10]++;
                  counter++;
                }

                if(counter==10)
                {
                    cout<<"Case #"<<m<<": "<<number<<endl;
                    p=1;
                    break;
                }
                temp=temp/10;
            }
            if(p==1)
            {
                break;
            }
            k++;
        }
    }
}
return 0;
}
