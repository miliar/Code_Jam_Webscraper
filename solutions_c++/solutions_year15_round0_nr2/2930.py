#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int d,arr[1005];

bool possible(int val,int mov)
{
    int cnt=0;
    for(int i=0;i<d;i++)
    {
        int x=arr[i];
        int y=x/val+ (x%val?1:0);
        cnt+=y-1;
    }
    if(cnt<=mov) return true;
    return false;
}

int calc_min(int i)
{
    int lo=1,hi=1000,mid;
    while(hi-lo>1)
    {
        mid=(hi+lo)/2;
        if(possible(mid,i)) hi=mid;
        else lo=mid;
    }
    if(possible(lo,i)) return lo;
    return hi;
}

int main()
{
    freopen("b_in.txt","r",stdin);
    freopen("b_out.txt","w",stdout);
    int t,cs=1;
    cin>>t;
    while(t--)
    {
        cin>>d;
        for(int i=0;i<d;i++) cin>>arr[i];
        int out=1000000;
        for(int i=0;i<=1000;i++)
        {
            int x=calc_min(i);
            out=min(out,i+x);
        }
        printf("Case #%d: %d\n",cs++,out);
    }
    return 0;
}
