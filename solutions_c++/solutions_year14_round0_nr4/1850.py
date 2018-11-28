#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
double a[2000],b[2000];
bool used[2000];
using namespace std;
int main()
{
    int r,i,j,k,n,t,ans1,ans2;
    freopen("D-large.in","r",stdin);
    //freopen("D-small-attempt0.in","r",stdin);
    freopen("dout.txt","w",stdout);
    cin>>t;
    r=1;

    while(t--)
    {
        cin>>n;
        for(i=0; i<n; i++)
        {
            cin>>a[i];
        }
        for(i=0; i<n; i++)
        {
            cin>>b[i];
        }
        sort(a,a+n);
        sort(b,b+n);
        ans1=0;
        ans2=0;
//        for(i=0; i<n; i++)
//        {
//            cout<<a[i]<<' ';
//        }
//        cout<<endl;
//        for(i=0; i<n; i++)
//        {
//            cout<<b[i]<<' ';
//        }
//        cout<<endl;
        cout<<"Case #"<<r<<": ";
        r++;
        memset(used,0,sizeof(used));
        for(i=0;i<n;i++)
        {
            k=-1;
            for(j=0;j<n;j++)
            {
                if(used[j]==0)
                {
                    if(k==-1)k=j;
                    if(a[i]<b[j])
                    {
                        k=j;
                        break;
                    }
                }
            }
            //cout<<a[i]<<' '<<b[k]<<endl;
            if(a[i]>b[k])ans1++;
            used[k]=1;
        }
        memset(used,0,sizeof(used));
        for(i=0;i<n;i++)
        {
            k=-1;
            for(j=n-1;j>=0;j--)
            {
                if(used[j]==0)
                {
                    if(k==-1)k=j;

                    if(a[i]>b[j])
                    {
                        k=j;
                        break;
                    }
                }
            }

            if(a[i]>b[k])ans2++;
            used[k]=1;
        }
        cout<<ans2<<' '<<ans1<<endl;

    }
}
