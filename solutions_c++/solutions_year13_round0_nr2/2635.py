#include<stdio.h>
#define max(a,b) ((a)>(b)?(a):(b))
const int maxn=100;
const char inf[]="B-small-attempt2.in";
const char ouf[]="B-small-attempt2.out";

int T,n,m;
int map[maxn+10][maxn+10];

int fl[maxn+10][maxn+10],fr[maxn+10][maxn+10],ft[maxn+10][maxn+10],fb[maxn+10][maxn+10];

int ans;

void input(){
    int i,j;
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++)
	for(j=1;j<=m;j++)
	    scanf("%d",&map[i][j]);
}

void work(){
    int i,j;
    for(i=1;i<=n;i++)
	for(j=1;j<=m;j++)
	    fl[i][j]=fr[i][j]=ft[i][j]=fb[i][j]=0;
    for(i=1;i<=n;i++){
	fl[i][0]=0;
	for(j=1;j<=m;j++)
	    fl[i][j]=max(fl[i][j-1],map[i][j]);
	fr[i][m+1]=0;
	for(j=m;j>=1;j--)
	    fr[i][j]=max(fr[i][j+1],map[i][j]);
    }
    for(i=1;i<=m;i++){
	ft[0][i]=0;
	for(j=1;j<=n;j++)
	    ft[j][i]=max(ft[j-1][i],map[j][i]);
	fb[n+1][i]=0;
	for(j=n;j>=1;j--)
	    fb[j][i]=max(fb[j+1][i],map[j][i]);
    }
    ans=1;
    for(i=1;i<=n;i++){
	for(j=1;j<=m;j++){
	    if((map[i][j]<fl[i][j] || map[i][j]<fr[i][j]) && 
               (map[i][j]<ft[i][j] || map[i][j]<fb[i][j])){
		ans=0;
		return;
	    }       
	}
    }
}

void output(){
    printf("Case #%d: ",T);
    if(ans)
	printf("YES\n");
    else
	printf("NO\n");
}

int main(){
    freopen(inf,"r",stdin);
    freopen(ouf,"w",stdout);
    int totT;
    scanf("%ld",&totT);    
    for(T=1;T<=totT;T++){
	input();
	work();
	output();
    }
    return 0;
}
