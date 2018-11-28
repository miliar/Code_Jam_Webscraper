#include <bits/stdc++.h>

using namespace std;
int a[1010];
int n;
bool check(int val,int cuts)
{
    int cutret=0;
    for(int i=0; i<n; i++)
        cutret+=(a[i]-1)/val;
    if(cutret<=cuts)return true;
    else return false;
}
int main()
{
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int l=0; l<t; l++)
    {
        int sol=99999;
        scanf("%d",&n);
        for(int i=0; i<n; i++)
            scanf("%d",&a[i]);
        for(int i=0; i<=1000; i++)
        {
            int lo=1,hi=1000;
            while(hi>lo)
            {
                int mid=(hi+lo)/2;
                if(check(mid,i))hi=mid;
                else lo=mid+1;
            }
            if(!check(lo,i)==true)lo--;
            sol=min(sol,i+lo);
        }
        printf("Case #%d: %d\n",l+1,sol);
    }
    return 0;
}
