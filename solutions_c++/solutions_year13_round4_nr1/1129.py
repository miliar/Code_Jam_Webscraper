#include<stdio.h>
#include<string.h>
int s[20000][105];
int main(){
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A-small-attempt4.out","w",stdout);
    int t,n,m,a,b,p,i,j,k,l,ans,top,w,pp;
    scanf("%d",&t);
            pp=1;
        while(t--){
            ans=0;
            top=0;
            memset(s,0,sizeof(s));
            scanf("%d%d",&n,&m);
            for(i=0;i<m;i++){
                scanf("%d%d%d",&a,&b,&p);
                for(j=a+1;j<=b;j++){
                    for(k=top;k<top+p;k++){
                        s[k][j]=n-(j-a-1);
                    }
                }
                top+=p;
            }

            for(i=1;i<=n;i++){
                for(j=0;j<top;j++){
                    if(s[j][i]==0 && s[j][i-1]>1){
                        for(k=0;k<top;k++){
                            if(s[k][i]>s[j][i-1]-1){
                                for(l=i;s[k][l]!=0;l++){
                                    w=s[j][l-1]-1;
                                    s[j][l]=w;
                                    ans+=s[k][l]-w;
                                    s[k][l]=0;
                                }
                                if(k<j) j=k-1;
                                break;
                            }
                        }
                    }
                }
            }
            printf("Case #%d: %d\n",pp++,ans);

    }
}
