#include<cstdio>

#define N 1005
using namespace std;

int tc,n,m,cnt;
int t[N];
int p(int a){
	int d[10],c=0;
	int k=a;
	while(a){
		d[c++]=a%10;
		a/=10;
	}
	for(int i=0;i<c/2;i++){
		if (d[i]!=d[c-i-1]) return false;
	}
	return true;
}
int f(int a,int b){
	int i;
	int ret = 0;
	for(i=0;i<cnt;i++){
		if (t[i]>=a && t[i]<=b)
			ret++;
	}
	return ret;
}
int main(){
	int i,j,k;
	freopen("c.in", "r", stdin);
	freopen("c.out","w",stdout);
	int s=0;
	for(i=1;i*i<=1000;i++){
		if (!p(i)) continue;
		j=i*i;
		if (p(j)){
			t[cnt++]=j;
		}
	}
	scanf("%d",&tc);
	for(int tcc=1;tcc<=tc;tcc++){
		scanf("%d %d",&n,&m);
		printf("Case #%d: %d\n",tcc,f(n,m));
	}
	return 0;
}

/*
Input 
 	
Output 
 
3
1 4
10 120
100 1000
Case #1: 2
Case #2: 0
Case #3: 2
*/