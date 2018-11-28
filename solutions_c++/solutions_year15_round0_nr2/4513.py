#include<iostream>
#include<algorithm>
using namespace std;

#define N 9

int func(int b[])
{
    int a[N+1];
    for(int i=1;i<=N;i++)
        a[i]=b[i];
    int mv;
    for(mv=N;mv>0;mv--)
        if(a[mv])
            break;
    if(mv==1)
    {
        if(a[1])
            return 1;
        else 
            return 0;
    }
    int x=a[mv];
    a[mv]=0;

    if(mv <=  2*x)
        return mv;
    
    int ans=9;
    if(mv==9)
    {a[3]+=x;
     a[6]+=x;
     ans=min(ans,func(a)+x);
     a[3]-=x;
     a[6]-=x;
    }

    
    
    {
    a[mv/2]+=x;
    a[mv-mv/2]+=x;
    //cout<<x<<" "<<mv<<endl;    
    ans=min(ans,min(mv,func(a)+x));
    return ans;
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    int M;
    cin>>M;
    for(int i=0;i<M;i++)
    {
    int n,t;
    int a[N+1]={0};
    cin>>n;
    while(n--)
    {
        cin>>t;
        a[t]++;
    }
    /*
    for(int j=1;j<N+1;j++)
        if(a[j])
            cout<<j<<"("<<a[j]<<")"<<endl;
*/
    cout<<"Case #"<<i+1<<": "<<func(a)<<endl;
    }
}
