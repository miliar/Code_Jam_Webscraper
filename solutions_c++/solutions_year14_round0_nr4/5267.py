#include <iostream>
#include <cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int t,n,tc,i,j,c,a1,a2;
    cin>>t;
    for(tc=1;tc<=t;tc++)
    {
        cin>>n;
        double *a=new double[n];
        double *b=new double[n];
        for(i=1;i<=n;i++)
        {
            cin>>a[i-1];
        }
        for(i=1;i<=n;i++)
            cin>>b[i-1];
        sort(a,a+n);
        sort(b,b+n);
        i=j=1;
        c=0;
        while(i<n+1&&j<n+1)
        {
            if(a[i-1]>b[j-1])
                j++;
            else
            {
                i++;
                j++;
                c++;
            }
        }
        a1=n-c;
        i=j=n;
        c=0;
        while(i>0&&j>0)
        {
            if(a[i-1]<b[j-1])
                j--;
            else
            {
                i--;
                j--;
                c++;
            }
        }
        a2=c;
        printf("Case #%d: %d %d\n",tc,a2,a1);
    }
    return 0;
}
