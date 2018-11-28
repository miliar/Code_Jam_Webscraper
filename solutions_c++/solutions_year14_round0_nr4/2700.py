/*Deceitful War*/
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out4_large.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {   int n;
        cin>>n;
        double a[n],b[n];
        int c[n],d[n];
        int i;
        for(i=0;i<n;i++)
        {   cin>>a[i];
            c[i]=a[i]*1000000;
        }
        for(i=0;i<n;i++)
        {   cin>>b[i];
            d[i]=b[i]*1000000;
        }
        sort(c,c+n);
        sort(d,d+n);
        /*for(i=0;i<n;i++)
            cout<<c[i]<<" ";
        cout<<endl;
        for(i=0;i<n;i++)
            cout<<d[i]<<" ";
        cout<<endl;*/
        int temp,j,ans1=0,ans2=0,count1[2000]={0};
        for(i=0;i<n;i++)
        {   temp=c[i];
            for(j=0;j<n;j++)
            {   if(d[j]>c[i]&&count1[j]==0)
                {   count1[j]++;
                    break;
                }
            }
            if(j==n)
                ans2++;
        }
        int count2[2000]={0};
        for(i=0;i<n;i++)
        {   temp=c[i];
            for(j=0;j<n;j++)
            {   if(c[i]>d[j]&&count2[j]==0)
                {   ans1++;
                    count2[j]++;
                    break;
                }
            }
        }
        cout<<"Case #"<<cas<<": ";
        cout<<ans1<<" "<<ans2<<endl;
        cas++;
    }
    return 0;
}
