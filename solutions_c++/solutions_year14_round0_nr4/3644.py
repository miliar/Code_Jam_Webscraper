#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.in","w",stdout);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int x;
        cin>>x;
        double a[1001],b[1001],d[1001],e[1001];
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        memset(d,0,sizeof(d));
        memset(e,0,sizeof(e));
        for(int j=0; j<x; j++)
        {
            cin>>a[j];
        }
        for(int j=0; j<x; j++)
        {
            cin>>b[j];
        }
        sort(a,a+x);
        sort(b,b+x);
//        cout<<x<<endl;
//        for(int j=0; j<x; j++)
//        {
//            cout<<a[j]<<" ";
//            //cout<<b[j];
//        }
//        cout<<endl;
//        for(int j=0; j<x; j++)
//        {
//            //cout<<a[j];
//            cout<<b[j]<<" ";
//        }
//        cout<<endl;
        int flag=0,cnt1=0,cnt2=0;
        if(a[0]>b[x-1])
        {
            //cout<<"1"<<endl;
            cnt2=0;
        }
        else if(b[0]<a[x-1])
        {
            for(int j=0,l=x-1,m=0; j<x; j++)
            {
                if(a[j]>b[m]&&e[m]==0)
                {
                    //cout<<a[j]<<" ";
                    e[m]=1;
                    m++;
                }
                else if(a[j]<b[l]&&e[l]==0)
                {
                    //cout<<a[j]<<endl;
                    e[l]=1;
                    l--;
                    cnt1++;
                }
                else{
                    //cout<<j<<" "<<l<<" ";
                }
                for(int k=0; k<x; k++)
                {
                    if(b[k]>a[j]&&d[k]==0)
                    {
                        cnt2++;
                        d[k]=1;
                        break;
                    }
                }
            }
        }
        else
        {
            //cout<<"2"<<endl;
            cnt1=x;
            cnt2=x;
        }
        printf("Case #%d: %d %d\n",i,x-cnt1,x-cnt2);
    }
    return 0;
}
