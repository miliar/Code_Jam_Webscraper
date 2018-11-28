#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
void sortit(double a[], int n)
{
    int i, j;
    double temp;
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
}
int war(double a[], double b[], int n)
{
    sortit(a,n);
    sortit(b,n);
    int i, j, ken=0, x=0;
    double md;
    for(i=0;i<n;i++)
    {
        for(j=x;j<n;j++)
        {
            if(a[i]<b[j] &&b[j]!=0)
            {
                ken++;
  //              cout<<a[i]<<" "<<b[j]<<endl;
                b[j]=0;
                x=j;
                break;
            }
        }
    }
    //cout<<ken;
    return (n-ken);
}
int dwar(double a[], double b[], int n)
{
    sortit(a,n);
    sortit(b,n);
    int i, j, naomi=0, x;
    double md;
    for(i=0;i<n;i++)
    {
        x=-1;
        for(j=0;j<n;j++)
        {
            if(a[i]>b[j]&&b[j]!=0)
                x=j;
        }
        if(x!=-1)
        {
            naomi++;
            b[x]=0;
            a[i]=0;
        }
    }
    return naomi;
}
int main(void)
{
    int t, c=1;
    freopen("output.txt","w",stdout);
    freopen("D-large.in","r",stdin);
    cin>>t;
    //cout<<t<<" ";
    while(c<=t)
    {
        int n;
        cin>>n;
        double a[n], b[n],q[n],p[n];
        int i;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            q[i]=a[i];
                    //    cout<<"here";
        }
        for(i=0;i<n;i++)
        {
            cin>>b[i];
            p[i]=b[i];
          //  cout<<"here2";
        }

        int x=dwar(a,b,n);
        int y=war(q,p,n);
        cout<<"Case #"<<c<<": "<<x<<" "<<y<<endl;
        c++;
    }
    fclose(stdout);
    fclose(stdin);
}
