#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const int MAX_LEN=35;
const int MAX_NUM=510;
const long long mod=(long long)(1e18);

int T,num,len,total,cases=0;
char s[MAX_LEN];

struct ANS{
	char str[MAX_LEN];
	long long data[15];
	long long res[15];
}ans[MAX_NUM];

inline int judge_prime(long long t,int b)//在b进制下得到t，判断t是否为素数
{
	for(long long i=2;i*i<=t;i++){
		if(t%i==0){//不是素数
			ans[total].data[b]=i;
			ans[total].res[b]=t;
			return 0;
		}
	}
	return 1;
}

inline long long base(int k)
{
	long long res=1,tmp=k;
	for(int i=len-2;i>=0;i--,tmp*=k){
		res+=(s[i]-'0')*tmp;
	}
	return res;
}

inline int check()
{
	for(int i=2;i<=10;i++){
		long long t=base(i); 
		if(judge_prime(t,i)) return 0;//只要在任意一进制下得到素数就返回0
	}
	return 1;
}

inline void dfs(int k)
{
	if(k==len-1) {
		if(check()) {
			strcpy(ans[total].str,s);
			total++;
		}
		return;
	}
	for(int i=0;i<=1;i++){
		s[k]=i+'0';
		dfs(k+1);
		if(total==num) return;
	}
}

int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("Cout.txt","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&len,&num);
		s[0]=s[len-1]='1';
		s[len]='\0';
		total=0;
		dfs(1);
		printf("Case #%d:\n",++cases);
		for(int i=0;i<total;i++){
			printf("%s",ans[i].str);
			for(int j=2;j<=10;j++){
				//printf(" res=%lld",ans[i].res[j]);
				printf(" %lld",ans[i].data[j]);
			}
			printf("\n");
		}
	}
	return 0;
}
