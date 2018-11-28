# include <bits/stdc++.h>
using namespace std;
# define ll long long int
ll arr[70000000];
# define MAX 10000000000
//int compare(const void *a,const vid *b)
//{
//    return *(int*)a-*(int*)b;
//}

int length(ll x)
{
    int c=0;
    while(x!=0){x/=10;c++;}
    return c;
}

ll rev(ll x)
{
    ll a=0;
    while(x!=0)
    {
        a=10*a+(x%10);
        x/=10;
    }
    return a;
}


main()
{
    int t,T,len;
    ll n,ans,x,ten,r;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    x=1;
    ll count=0;
    while(1)
    {
        arr[count++]=x;
        r=rev(x);
        if(r>x){x=r;}
        else x++;
        if(x>MAX)break;
    }
//    cout<<count<<endl;
//for(int i=0;i<25;i++)cout<<arr[i]<<" ";
//cout<<endl;
    for(t=1;t<=T;t++)
    {
        cin>>n;
        int low,high,mid;
        low=0;high=count-1;
        ll pos=-1;
        while(low<=high)
        {
            mid=(low+high)/2;
            if(n<arr[mid]){high=mid-1;}
            else if(n>=arr[mid]){pos=mid;low=mid+1;}
//            cout<<arr[low]<<" "<<arr[pos]<<" "<<arr[high]<<endl;
        }

        ans=pos+1+(n-arr[pos]);

        ans=pos+1;
        ll v=arr[pos];
        while(v!=n)
        {
            r=rev(v);
            if(r>v && r<=n)v=r;
            else v++;
            ans++;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;


        }
}
