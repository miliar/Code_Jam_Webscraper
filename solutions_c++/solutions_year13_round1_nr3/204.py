#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;

#define inf (1<<29)
#define maxm 110010

#define ii int

ii gcd(ii a,ii b){
    if(!a) return b;
    if(!b) return a;
    return gcd(b,a%b);
}
ii mini(ii a,ii b){
    if(a<b) return a; return b;
}
ii maxi(ii a,ii b){
    if(a>b) return a; return b;
}

int r,n,m,K,a[10],p[10];
bool flag[10];

int main(){

    int i,j,k,l,test,t=1;

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&test);

    while(test--){

        scanf("%d %d %d %d",&r,&n,&m,&K);

        printf("Case #%d:\n",t++);

		int i1;
        for(i1=1;i1<=r;i1++){
            for(j=1;j<=K;j++){
                scanf("%d",&a[j]);
            }
            sort(a+1,a+1+K);
            memset(flag,0,sizeof(flag));
            memset(p,0,sizeof(p));
            for(j=K;j>=1;j--){
                if(a[j]%5==0){
                    flag[5]=1;
					k=0;
                    while(a[j]%5==0){
                        a[j]/=5;
                        k++;
                    }
					p[5]=maxi(p[5],k);
                }
                if(a[j]%3==0){
                    flag[3]=1;
					k=0;
                    while(a[j]%3==0){
                        a[j]/=3;
						k++;
                    }
					p[3]=maxi(p[3],k);
                }
                if(a[j]%2==0){
                    flag[2]=1;
					k=0;
                    while(a[j]%2==0){
                        a[j]/=2;
                        k++;
                    }
					p[2]=maxi(p[2],k);
                }
            }
            int now=0;

            if(p[5]){
                for(i=1;i<=p[5];i++){
                    if(now==3) break;
                    printf("5"); now++;
                }
            }
            if(p[3]){
                for(i=1;i<=p[3];i++){
                    if(now==3) break;
                    printf("3"); now++;
                }
            }
            if(p[2]){
                if(p[2]==1&&now<3){
                    printf("2");  now++;
                }
                if(p[2]==2){
                    if(now==1){ printf("22"); now+=2; }
                    else if(now==2){ printf("4"); now++; }
                }
                if(p[2]==3){
                    if(now==0){ printf("222"); now+=3; }
                    else if(now==1){ printf("24"); now+=2; }
                    else if(now==2){ printf("4"); now++; }
                }
            }
            if(now<3){
                printf("2"); now++;
            }
            if(now<3){
                printf("2"); now++;
            }
            if(now<3){
                printf("2"); now++;
            }
            printf("\n");

        }

    }

    return 0;
}
