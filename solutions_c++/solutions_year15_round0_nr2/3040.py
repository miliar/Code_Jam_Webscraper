#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll is,ipt[2009];
ll rs,ra[2009];


bool solve(ll val,ll middle)
{
    ll diff;
    rs=0;
    int index;
    for(int i=1;i<=is;i++)
    {
        if(ipt[i]>middle)
        {
            diff=ipt[i]-middle;
            rs++;
            ra[rs]=diff;
        }
    }
    index=1;
    while(index<=rs)
    {
        if(ra[index]>0&&val==0)
        {
            return false;
        }
        if(middle>=ra[index])
        {
            index++;
            val--;
        }
        else
        {
            ra[index]-=middle;
            val--;
        }
    }
    return true;
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);

    ios_base::sync_with_stdio(false);
    int cases;
    cin>>cases;
    int t = 0;
    ll num,r,p;
    while(cases--)
    {
        t++;
        bool c;
        is=0;
        cin>>r;
        for(int i=1; i<=r; i++)
        {
            cin>>num;
            is++;
            ipt[is]=num;
        }
        ll result=INT_MAX;
        for(int k=0; k<=1000; k++)
        {
            ll low=1,high=1000,mid;
            while(low<high)
            {
                mid=(low+high)/2;
                c=solve(k,mid);
                if(c==false)
                {
                    low=mid+1;
                }
                else
                {
                    high=mid;
                }
            }
            if(k+low<result)
            {
                result=k+low;
            }
        }
        printf("Case #%d: %ld\n",t,result);
    }


    return 0;
}
