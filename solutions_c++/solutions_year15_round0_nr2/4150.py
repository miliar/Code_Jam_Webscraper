#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
#define ll long long
#define LL long long

int pack[1010],n;
int movenum(int x)
{
    int i,res=0;
    for(i=0;i<n;i++)
    {
        res+=(pack[i]-1)/x;
    }
    return res+x;
}

int trediv(int l,int r)
{
    int m=(l+r)/2;
    int mm=(m+r)/2;
    int ym=movenum(m);
    int ymm=movenum(mm);
    if(r-l<=1)return min(movenum(l),movenum(r));
    if(ym>ymm)
    {
        return trediv(m,r);
    }
    else if(ym<ymm)
    {
        return trediv(l,mm);
    }
    else
    {
        return min(trediv(l,mm),trediv(m,r));
    }
}
int main()
{
    int tt;
    cin>>tt;
    int ii=1;
    while(tt--)
    {
        scanf("%d",&n);
        int i,j;
        int ma=-1;
        for(i=0;i<n;i++)
        {
            scanf("%d",&pack[i]);
            ma=max(pack[i],ma);
        }
        printf("Case #%d: %d\n",ii++,min(ma,trediv(1,ma)));
    }
    return 0;
}
