#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#define maxn 200010
#define ll long long
using namespace std;
int a[maxn];
ll sum[maxn];
struct node{
    ll zi,mu;
    node(){}
    node(ll a,ll b){
        ll x=a>0?a:-a;
        ll gcd=__gcd(x,b);
        zi=a/gcd,mu=b/gcd;
    }
    bool operator <(const node &ot)const{
        return zi*ot.mu<mu*ot.zi;
    }
};
node solve(int po,int num,int n){
    ll zi=sum[po]-sum[po-num-1]+sum[n]-sum[n-num];
    ll mu=2*num+1;
    return node(zi-mu*a[po],mu);
}
int main()
{
    freopen("dd.txt","r",stdin);
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&a[i]);
    }
    sort(a+1,a+n+1);
    for(int i=1;i<=n;i++)
        sum[i]=sum[i-1]+a[i];
    node ma=node(0,1);
    int po=1,num=0;
    for(int i=2;i<n;i++){
        int l=0,r=min(i-1,n-i),mid,midmid,nn;//Èý·Ö
        node tmp=node(0,1);
        while(l<=r){
            mid=(l+r)/2;
            midmid=min(mid+1,r);
            node left=solve(i,mid,n);
            node right=solve(i,midmid,n);
            node tt=left<right?right:left;
            if(right<left){
                if(tmp<tt){
                    nn=mid;
                    tmp=tt;
                }
                r=midmid-1;
            }
            else{
                if(tmp<tt){
                    nn=midmid;
                    tmp=tt;
                }
                l=mid+1;
            }
        }
        if(ma<tmp){
            ma=tmp;
            po=i;
            num=nn;
        }
    }
    printf("%d\n",num*2+1);
    for(int i=num;i>0;i--)
        printf("%d ",a[po-i]);
    printf("%d ",a[po]);
    for(int i=num-1;i>=0;i--)
        printf("%d ",a[n-i]);
    printf("\n");
    return 0;
}
