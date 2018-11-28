#include<cstdio>
#include<iostream>
#define MAX 1005
using namespace std;
void msort(double a[],int start,int end)
{
    int mid,i,j,k=0;
    double temp[end-start+1];
    if(start<end)
    {
        mid=(start+end)/2;
        msort(a,start,mid);
        msort(a,mid+1,end);
    }
    mid=(start+end)/2;
    i=start;
    j=mid+1;
    while((i<=mid)&&(j<=end))
    {
        if(a[i]<=a[j])temp[k++]=a[i++];
        if(a[i]>a[j])temp[k++]=a[j++];
    }
    while(i<=mid)temp[k++]=a[i++];
    while(j<=end)temp[k++]=a[j++];
    for(i=0;i<k;i++)a[i+start]=temp[i];
}
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif // ONLINE_JUDGE
    double neo[MAX],kao[MAX];
    int i,j,t,T,n;
    int start,end,ans2,x,ans1;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>n;
        for(i=0;i<n;i++)cin>>neo[i];
        for(i=0;i<n;i++)cin>>kao[i];
        msort(neo,0,n-1);
        msort(kao,0,n-1);

        start=0;
        end=n;
        while(start<n)
        {
            for(i=0;i<end;i++)
            {
                if(neo[i+start]<kao[i])break;
            }
            if(i==end)break;
            else
            {
                start++;
                end--;
            }
        }
        ans1=n-start;
        x=0;
        for(i=0;i<n;i++)
        {
            for(j=x;j<n;j++)
            {
                if(kao[j]>neo[i])
                {
                    x=j+1;
                    break;
                }


            }
            if(j==n)break;



        }
        ans2=n-i;
        cout<<"Case #"<<t<<": ";
        cout << ans1 << " " << ans2 << endl;
    }
    return 0;
}
