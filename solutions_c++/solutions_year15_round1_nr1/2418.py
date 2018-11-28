#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,j=1;
    freopen ("A-large.in","r",stdin);
	freopen ("output1.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        int n,d=0;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
            cin>>a[i];
           long long int count_1=0,count_2=0;
        for(int i=1;i<n;i++)
        {
            if(a[i]<a[i-1])
                count_1+=a[i-1]-a[i];
                d=d>(a[i-1]-a[i])?d:(a[i-1]-a[i]);
        }
        //cout<<"d"<<d;
        if(d==0)
            count_2=0;
        else
        {
                   for(int i=0;i<n-1;i++)
                    {
                        if(d>=a[i])
                            count_2+=a[i];
                        else
                        count_2+=d;
                    }
        }

        //int d=a[n-2]-a[n-1];
        printf ("Case #%d: %lld %lld\n",j,count_1,count_2);
        j++;
    }
    return 0;
}
