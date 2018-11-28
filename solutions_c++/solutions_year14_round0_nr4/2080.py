#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

bool compare(double a,double b)
{
    return a>b;
}

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);

    int T,t;
    int i,j,k;

    int n,p1,p2;
    double a[1001],b[1001],c[1001];

    cin>>t;
    T=t;
    while(t--)
    {
        p1=p2=0;
        cin>>n;
        for (i=0;i<n;i++)
            cin>>a[i];
        for (i=0;i<n;i++)
        {
            cin>>b[i];
            c[i]=b[i];
        }


        sort(a,a+n);
        sort(b,b+n);
        sort(c,c+n);

        for (i=0;i<n;i++)
        {
            for (j=0;j<n;j++)
                if (a[i]<b[j])
                {
                    b[j]=0;
                    break;
                }

            if (j==n) break;
        }
        p1=n-i;

        p2=0;
        for (i=0;i<n;i++)
        {
            for (j=0;j<n;j++)
                if (a[i]>c[j] && c[j]!=0)
                {
                    c[j]=0;
                    p2++;
                    break;
                }
        }


        cout<<"Case #"<<T-t<<": "<<p2<<" "<<p1<<endl;
    }
    return 0;
}
