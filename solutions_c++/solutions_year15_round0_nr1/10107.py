#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long t;
    long long count;
    while (cin>>t)
    {
        for (int i=1; i<=t; i++)
        {
            long long n;
            string s;

            count = 0;
            cin>>n;
            long long a[n+1];
            cin>>s;
            int k=0;
            for (int j=0; j<s.size(); j++)
            {
                a[k]=s[j]-48;
                k++;
            }

            //cout<<n<<" "<<s<<endl;
            if (n==0)
            {
                cout<<"Case #"<<i<<": "<<count<<endl;
            }
            else
            {
                int sum=a[0];
                int sum1=0;
                int x,y;
                for (int l=1; l<n+1; l++)
                {
                    sum+=a[l];
                    if (a[l]!=0)
                    {
                        x=l;
                        y=a[l];
                        sum1=sum-a[l];
                        if (sum1<x)
                        {
                            count+=(x-sum1);
                            sum+=count;
                        }
                    }
                }
                cout<<"Case #"<<i<<": "<<count<<endl;
            }

        }
    }
}

