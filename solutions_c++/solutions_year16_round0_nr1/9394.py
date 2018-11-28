#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include <cassert>
#include<map>
#include<queue>
#include<stack>
#include<time.h>
#include<math.h>
#include<set>
#include<complex>
using namespace std;
#define INF 0x3f3f3f3f
#define DINF 1e10
#define EPS 1e-15
#define PII acos(-1)
#define LL long long
#define Pii pair<int,int>
#define For(i,n) for(int i=0;i<n;i++)
#define ileer(n) scanf("%d",&n)
#define i2leer(n,m) scanf("%d %d",&n,&m)
#define fleer(n) scanf("%lf",&n)
#define f2leer(n,m) scanf("%Lf %Lf",&n,&m)
#define MK make_pair
#define PB push_back
#define llenar(arr,val) memset(arr,val,sizeof(arr))
#define VLL vector< LL >
#define matrix vector<VI >
#define F first
#define S second
#define MAXN 2001
bool marca[11];
int can;
void digi(int n){
	while(n!=0){
		int div=n/10;
		int mod=n%10;
		can+=marca[mod]?0:1;
		marca[mod]=true;
		n=div;
	}
	

}



int main(){
	int t;
	ileer(t);
	for(int c=0;c<t;c++){
		int n;
		ileer(n);
		printf("Case #%d: ",c+1);
		if(n==0){
			printf("INSOMNIA\n");
			continue;
		}
		llenar(marca,false);
		can=0;
		int vez=1;
		
		while(can<10){
			digi(n*vez);
			vez++;
		}
		printf("%d\n",n*(vez-1));
		
		
		
	}
}