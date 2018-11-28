#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int rec(int status,int a[],int siz,int sum);

int main()
{  freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
  int t,tt,n,i,ans,sum;int arr[100];
    cin>>t;
    tt=t;
    while(t)
    {

        cin>>n;
        sum=0;
        for(i=0;i<n;i++)
            {cin>>arr[i];
             sum+=arr[i];}
        ans=min(rec(0,arr,n,sum),rec(1,arr,n,sum));
        cout<<"Case #"<<tt-t+1<<": "<<ans<<endl;
        t--;
    }
    return 0;
}

int rec(int status,int a[],int siz,int sum)
{int b[100],c[100];int i,temp,ans,ctr,n;
    if(sum<=siz)return 1;
    if(siz<=0)return 0;
    if(status==0)
    {
       sort(a,a+siz);
       sum=0;
       ctr=0;
       for(i=0;i<siz;i++)
            {b[i]=a[i];
             }
       if(b[siz-1]==9)
       {
           b[siz-1]=6;b[siz]=3;siz++;
       }
       else{
       temp=b[siz-1];
       b[siz-1]/=2;
       b[siz]=temp-b[siz-1];
       siz++;}
       for(i=0;i<siz;i++)
       {
           if(b[i]>0)
           {
               b[ctr]=b[i];
               ctr++;
               sum+=b[i];
           }
       }siz=ctr;if(ctr==0)return 0;
       //cout<<"status = "<<status<<" : "<<"ans : "<<ans<<endl;
       //for(i=0;i<siz;i++)
        //cout<<b[i]<<" ";cout<<endl;
       ans=1+min(rec(0,b,siz,sum),rec(1,b,siz,sum));

       return ans;
    }
    else
    {
        sort(a,a+siz);
        sum=0;
        for(i=0;i<siz;i++)
            {c[i]=a[i]-1;
            }
        n=0;
        for(i=0;i<siz;i++)
            {if(c[i]>0){c[n]=c[i];sum+=c[i];n++;}}
        if(n==0)return 0;
        //cout<<"status = "<<status<<" : "<<"ans : "<<ans<<endl;
     // for(i=0;i<n;i++)
       // cout<<c[i]<<" ";cout<<endl;
        ans=1+min(rec(0,c,n,sum),rec(1,c,n,sum));
      // cout<<"ans : "<<ans<<endl<<endl;
        return ans;

    }

}
