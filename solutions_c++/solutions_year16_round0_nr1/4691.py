#include<bits/stdc++.h>
using namespace std;

bool arr[10];
bool check(long long n)
{
    int i;
    while(n!=0)
    {
        arr[n%10]=1;
        n/=10;
    }
    for(i=0;i<10;i++)
    {
        if(arr[i]==0)break;
    }
    if(i==10)return 1;
    else return 0;
}
int main()
{
    int t,i;int k=1;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        long long n,x;
        for(i=0;i<10;i++)arr[i]=0;
        cin>>n;
           
            x=n;i=2;
        cout<<"Case #"<<k++<<": ";
        if(n==0){cout<<"INSOMNIA\n";continue;}
        while(1)
        {
            if(check(x)==1){cout<<x<<endl;break;}
            x=n*i;
            i++;
        }
        
        
    }
    return 0;
}
