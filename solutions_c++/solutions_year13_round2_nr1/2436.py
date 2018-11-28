#include<stdio.h>
#include<algorithm>

using namespace std;


int N,inp[109];

int mini(int a,int b)
{ if(a>b) return b; return a; }

int calc(int p, int val)
{
    int ret=0;
    if(p==N-1) {if(inp[p]<val) return 0; else return 1;}

    if(inp[p]<val) ret+=calc(p+1,val+inp[p]);
    else ret=mini(ret+calc(p+1,val)+1,ret+calc(p,val+val-1)+1);

    return ret;
}

int main()
{
    int T,c=0,i,j,k,A;

    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);

    scanf("%d",&T);
    while(c++<T)
    {
        scanf("%d%d",&A,&N);
        for(i=0;i<N;i++) scanf("%d",&inp[i]);
        sort(inp,inp+N);
        if(A==1) printf("Case #%d: %d\n",c,N);
        else printf("Case #%d: %d\n",c,calc(0,A));
    }
    return 0;
}
