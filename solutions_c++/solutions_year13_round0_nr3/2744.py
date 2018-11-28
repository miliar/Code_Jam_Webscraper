#include <cstdio>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,1,n+1)
using namespace std;
int A,B;
int length(int n){
	return n?1+length(n/10):0;
}
bool isFair(int n){
	int len=length(n);
	int d[10];
	for(int i=0;i<len;i++){
		d[i]=n%10;
		n/=10;
	}
	for(int i=0;i<len;i++){
		if(d[len-1-i]!=d[i])return false;
	}
	return true;
}
bool isSquare(int n){
	for(int i=1;i*i<=n;i++){
		if(i*i==n)return isFair(i);
	}
	return false;
}

bool fairSquare(int n){
	return isSquare(n)&&isFair(n);
}

int main(){
	//freopen("input.txt","r",stdin);
	freopen("C-small.in","r",stdin);
	freopen("output.txt","w",stdout);
    int T;scanf("%d",&T);
	REP(t,T){
		scanf("%d %d",&A,&B);
		int ans=0;
		FOR(i,A,B+1){
			if(fairSquare(i))ans++;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	
}	