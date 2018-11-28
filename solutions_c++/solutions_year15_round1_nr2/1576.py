#include <cstdio>
#include <cstring>
int m[1001],bar[10001],cus[4000001];
int gcd(int a,int b){
    return b==0?a:gcd(b,a%b);
}
int lcm(int m,int n){
	if((0==m)||(0==n))
		return 0;
	return ((m/gcd(m,n))*n);
}
int main(){
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("B-small-attempt1.out","w",stdout);
    int t,k=0,b,n,i,j,l,sum,max,ind;
    scanf("%d",&t);
    while(t--){
        scanf("%d %d",&b,&n);
        for(l=1,i=0;i<b;i++){
            scanf("%d",&m[i]);
            l=lcm(l,m[i]);
        }
        for(sum=i=0;i<b;i++){
            sum+=(l/m[i]);
        }
        memset(bar,0,sizeof(bar));
        for(ind=max=0,i=1;i<=sum;i++){
            for(j=0;j<b;j++){
                if(bar[j]<max) max=bar[j],ind=j;
            }
            cus[i]=ind;
            bar[ind]+=m[ind];
            max=bar[ind]+1;
        }
        n=(n-1)%sum+1;
        printf("Case #%d: %d\n",++k,cus[n]+1);
    }
}
