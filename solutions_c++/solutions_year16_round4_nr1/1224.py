#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <queue>
#include <stdlib.h>
#include <string>
#include <math.h>
#define SQ(a) ((a)*(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
const int INF = 2000000000;
const int mod = 1000000007;

int TT;
char a[10000];
void f(int n, int l,int t,int p,int r,int s){
	//printf(".");
	if(n==0){
		if(p)a[l]='P';
		else if(r)a[l]='R';
		else a[l]='S';
		return;
	}
	int x=1<<n;
	int q=x;
	q/=2;
	x/=3;
	int k=(1<<n)-x*3;
	int y=(1<<(n-1));
	y/=3;
	if(k==1){
		if(p==x+1){
			f(n-1,l,l+(1<<(n-1)),y+1,y+1,y);
			f(n-1,l+(1<<(n-1)),t,y+1,y,y+1);
		}
		else if(r==x+1){
			f(n-1,l,l+(1<<(n-1)),y+1,y+1,y);
			f(n-1,l+(1<<(n-1)),t,y,y+1,y+1);	
		}
		else{
			f(n-1,l,l+(1<<(n-1)),y+1,y,y+1);
			f(n-1,l+(1<<(n-1)),t,y,y+1,y+1);
		}
	}
	else {
		if(p==x){
			f(n-1,l,l+(1<<(n-1)),y,y+1,y);
			f(n-1,l+(1<<(n-1)),t,y,y,y+1);
		}
		else if(r==x){
			f(n-1,l,l+(1<<(n-1)),y+1,y,y);
			f(n-1,l+(1<<(n-1)),t,y,y,y+1);
		}
		else{
			f(n-1,l,l+(1<<(n-1)),y+1,y,y);
			f(n-1,l+(1<<(n-1)),t,y,y+1,y);
		}
	}

}
int main(){
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++){
		printf("Case #%d: ",T);
		int n,r,p,s;
		int b[3];
		scanf("%d%d%d%d",&n,&r,&p,&s);

		b[0]=r;b[1]=p;b[2]=s;
		sort(b,b+3);
		
		int x=1<<n;
		x/=3;
		if(b[0]!=x||b[2]!=x+1){
			printf("IMPOSSIBLE\n");
			continue;
		}
		f(n,0,1<<n,p,r,s);
		a[1<<n]=0;
		printf("%s\n",a);


	}
}