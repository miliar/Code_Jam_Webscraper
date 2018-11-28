#include <iostream>
#include <cstdio>
#define LL __int64
#define MAXN 10000005
#define MAX 10000007
using namespace std;

LL squ[MAXN];
int snum;
bool par(LL val){
    int bit[10],bnum=0;
    while(val){
        bit[bnum++]=val%10;
        val/=10;
    }
    for(int i=0;i<bnum/2;i++){
        if(bit[i]!=bit[bnum-i-1]) return false;
    }
    return true;
}
int loc(LL val){
    int l=0,r=snum-1;
    while(l<=r){
        int mid=(l+r)>>1;
        if(squ[mid]*squ[mid]==val)return mid;
        LL tmp=squ[mid]*squ[mid];
        if(tmp<val) l=mid+1;
        else r=mid-1;
    }
    return l;
}
int main()
{
  //  freopen("test.txt","r",stdin);
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    snum=0;
    for(LL i=1;i<MAXN;i++){
        if(par(i)&&par(i*i)) squ[snum++]=i;
    }
    int test,t=1;
    cin>>test;
    while(t<=test){
        LL A,B;
        cin>>A>>B;
        int ans=0;
        for(int i=0;i<snum;i++){
            if(squ[i]*squ[i]>B) break;
        //    if(squ[i]*squ[i]>=A) ans=1;
            if(squ[i]*squ[i]>=A&&squ[i]*squ[i]<=B) ans++;
        }
  //      int pa=loc(A);
  //      int pb=loc(B);
  //      if(squ[pa]*squ[pa]==A) pa--;
        printf("Case #%d: %d\n",t++,ans);
    }
    return 0;
}
