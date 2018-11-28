#include<stdio.h>
#include<string.h>

#define maxm 2050
#define ii int

ii tot;
int bad[maxm][20],good[maxm][20],n,p;
bool fl[20];
ii dp[20];

void gen_bad(int n);
void gen_good(int n);
ii poww(ii b,ii p){
    if(!p) return 1; return b*poww(b,p-1);
}

ii cal_tot(int round);
int cal_good(int round,int now,int now1,int rem);
int cal_bad(int round,int now,int now1,int rem);

int main(){

    int i,j,k,l,test,t=1;

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&test);

    while(test--){

        scanf("%d %d",&n,&p);

        gen_bad(n);
        gen_good(n);

        memset(fl,0,sizeof(fl));
        printf("Case #%d: ",t++);
        printf("%d ",cal_bad(1,0,tot-1,p));
        printf("%d\n",cal_good(1,0,tot-1,p));
    }

    return 0;
}

ii cal_tot(int round){

    if(round>=n) return 1;

    if(fl[round]) return dp[round];
    fl[round]=1;

    return dp[round]=(ii)2*cal_tot(round+1);
}

int cal_good(int round,int now,int now1,int rem){

	if(now>=now1) return now;
    if(now>=tot) return tot-1;
    if(round>n) return now1;

    if(cal_tot(round)>=rem){
		while(good[now1][round]==0){
			now1--;
			if(now1<=now) break;
		}
        return cal_good(round+1,now,now1,rem);
    }

    rem-=cal_tot(round);
	while(good[now+1][round]==1){
		now++;
		if(now>=now1) break;
	}

    return cal_good(round+1,now,now1,rem);
}

int cal_bad(int round,int now,int now1,int rem){

    if(now>=tot) return tot-1;
	if(now>=now1) return now;
    if(round>n) return now1;

    if(cal_tot(round)>=rem){
		while(bad[now1][round]==0){
			now1--;
			if(now1<=now) break;
		}
        return cal_bad(round+1,now,now1,rem);
    }
    rem-=cal_tot(round);

	while(bad[now+1][round]==1){
		now++;
		if(now>=now1) break;
	}

    return cal_bad(round+1,now,now1,rem);

}

void gen_bad(int n){

    int i,j,k,l;
    tot=poww(2,n);
    int lim=0,next=1,now=1;
    for(i=0;i<tot;i++,next--){
        if(!next){
            now*=2;
            lim++; next=now;
        }
        for(j=1;j<=lim;j++){
            bad[i][j]=0;
        }
        for(j=lim+1;j<=n;j++){
            bad[i][j]=1;
        }
    }
	/*
    for(i=0;i<tot;i++){
        printf("%d ",i);
        for(j=1;j<=n;j++){
            printf("%d ",bad[i][j]);
        }
        puts("");
    }
	*/

}
void gen_good(int n){


    int i,j,k,l;
    tot=poww(2,n);
    int lim=0,next=1,now=1;
    for(i=tot-1;i>=0;i--,next--){
        if(!next){
            now*=2;
            lim++; next=now;
        }
        for(j=1;j<=lim;j++){
            good[i][j]=1;
        }
        for(j=lim+1;j<=n;j++){
            good[i][j]=0;
        }
    }

	/*
	printf(" Good : \n");
	for(i=0;i<tot;i++){
        printf("%d ",i);
        for(j=1;j<=n;j++){
            printf("%d ",good[i][j]);
        }
        puts("");
    }
	*/

}

