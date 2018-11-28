#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,sum1=0,sum2=0,max1;
    scanf("%d",&t);
    int k=1;
    while(k<=t){
        int n;
        sum1=0;sum2=0,max1=0;
        scanf("%d",&n);
        int i,m[n];
        for(i=0;i<n;i++)
            scanf("%d",&m[i]);
        for(i=0;i<n-1;i++)
        {
            if(m[i]-m[i+1]>max1)
                max1=m[i]-m[i+1];
        }
        for(i=0;i<n-1;i++)
        {
            if(m[i]>m[i+1])
                sum1+=(m[i]-m[i+1]);
            if(m[i]<=max1)
                sum2+=m[i];
            else if (m[i]>max1)
                sum2+=max1;
        }
        cout<<"Case #"<<k<<": "<<sum1<<" "<<sum2<<endl;
        k++;
    }
}
