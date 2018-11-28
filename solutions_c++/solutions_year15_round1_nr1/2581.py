#include<bits/stdc++.h>
using namespace std;

int a[100001];

bool check(int speed, int n)
{
    for(int i=1;i<n;i++)
    {
        if(a[i]<=a[i-1])
        {
            int diff=a[i-1]-a[i];
            if(speed<diff)
            {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    int t,n,a1,a2,op1,op2,speed,diff;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        
        //ans1..
        a1=0;
        for(int i=1;i<n;i++)
        {
            if(a[i]<=a[i-1])
                a1+=min(a[i-1],a[i-1]-a[i]);
            else
            {
                a1+=0;
            }
        }
        
        //ans2..
        //finding the constant speed with which she eats..
        speed=0;
        for(speed=0;;speed++)
        {
            if(check(speed,n))
                break;
        }

        a2=0;
        for(int i=0;i<n-1;i++)
            a2+=min(speed,a[i]);
        
        printf("Case #%d: %d %d\n",tt,a1,a2);
    }
    return 0;
}

