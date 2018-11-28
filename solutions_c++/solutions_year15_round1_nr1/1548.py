#include <cstdio>
int m[10001]={0};
int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,k=0,n,y,z,i,j,r;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        for(r=y=0,i=1;i<=n;i++){
            scanf("%d",&m[i]);
            if(m[i]<m[i-1]) y+=(m[i-1]-m[i]);
            if(m[i-1]-m[i]>r) r=m[i-1]-m[i];
        }
        for(z=0,i=1;i<n;i++){
            z+=(m[i]<r?m[i]:r);
        }
        printf("Case #%d: %d %d\n",++k,y,z);
    }
}
