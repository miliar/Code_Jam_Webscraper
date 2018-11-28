#include "stdio.h"
#include "algorithm"

int t,n,k,i,j;
double ch;
double p[300];
bool isSe[300];

void select(int x, int c, int k){
    double f = 1.0;
    double li[2][205];
    int i,j,y;
    if(x==n){
        if(c!=k) return;
        for(i = 0; i <= k; i++){
            li[0][i] = 0.0;
        }
        li[0][0] = 1.0;
        for(i = 0, y = 1; i < n; i++){
            if(isSe[i]){
                for(j = 0; j <= k/2; j++){
                    li[y%2][j] = p[i]*li[(y-1)%2][j-1] + (1.0-p[i])*li[(y-1)%2][j];
                }
                y++;
            }
        }
        if(li[(y-1)%2][k/2]>ch){
            ch = li[(y-1)%2][k/2];
        }
    }else{
        isSe[x] = false;
        select(x+1,c,k);
        if(c<k){
            isSe[x] = true;
            select(x+1,c+1,k);
        }
    }
}

int main(){
    scanf("%d",&t);
    for(i = 1; i <= t; i++){
        scanf("%d%d",&n,&k);
        for(j = 0; j < n; j++){
            scanf("%lf",&p[j]);
        }
        //std::sort(p,p+n);
        ch = 0.0;
        select(0,0,k);
        /*for(j = 0; j < k/2; j++){
            ch *= (1.0-p[j])*(p[n-j-1]);
        }*/
        printf("Case #%d: %.10f\n",i,ch);
    }
}

