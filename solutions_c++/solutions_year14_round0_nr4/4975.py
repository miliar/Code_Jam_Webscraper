#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    double a[100],b[100];
    int i,j,tc,a1,a2,n,k;
    cin>>tc;
    for(k=1;k<=tc;k++)
    {
        cin>>n;
        for(i=0;i<n;i++)
            cin>>a[i];
        for(i=0;i<n;i++)
            cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        j=i=0;
        a1=a2=0;
        while(i!=n)
        {
            if(a[i]>b[j])
            {
                a1++;
                i++;
                j++;
            }
            else
                i++;
        }
        j=i=0;
        while(j!=n)
        {
            if(a[i]<b[j])
            {
                a2++;
                i++;
                j++;
            }
            else
                j++;
        }
        cout<<"Case #"<<k<<": "<<a1<<" "<<n-a2<<endl;
    }
    return 0;
}
