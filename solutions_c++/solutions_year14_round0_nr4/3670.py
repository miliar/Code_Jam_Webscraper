#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
    fstream input("input.in",ios::in);
    fstream output("output.out",ios::out);
    int t,n,i,j,k,l,c=0,c1=0;
    input>>t;
    for(i=0;i<t;i++)
    {
        c=0;
        c1=0;
        input>>n;
        double a[n],b[n],a1[n],b1[n];
        for(j=0;j<n;j++)
        {
            input>>a[j];
            a1[j]=a[j];
        }
        for(j=0;j<n;j++)
        {
            input>>b[j];
            b1[j]=b[j];
        }
        sort(a,a+n);
        sort(a1,a1+n);
        sort(b,b+n);
        sort(b1,b1+n);
        for(j=0;j<n;j++)
        {
            for(k=0;k<n;k++)
            {
                if(b[k]>a[j])
                {
                    b[k]=0;
                    a[j]=0;
                    break;
                }
            }
            if(k==n)
            {
                c=n-j;
                break;
            }
        }
        for(j=0;j<n;j++)
        {
            for(k=0;k<n;k++)
            {
                if(b1[n-k-1]!=0)
                {
                    if(b1[n-k-1]>a1[n-1])
                    {
                        a1[j]=0;
                        b1[n-k-1]=0;
                        break;
                    }
                    for(l=0;l<n;l++)
                    {
                        if(b1[l]!=0)
                        {
                            break;
                        }
                    }
                    if(a1[j]>b1[l])
                    {
                        a1[j]=0;
                        b1[l]=0;
                        c1++;
                        break;
                    }
                }
            }
        }
        output<<"Case #"<<i+1<<": "<<c1<<" "<<c<<endl;
    }
    return 0;
}
