#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#define MAXN 10000001
using namespace std;
typedef unsigned long long int ull;
int S[MAXN];
char aux[15];
bool _palin(ull n){
	ltoa(n,aux,10);
	int l = strlen(aux);
	for(int i=0;i<l/2;i++){
		if(aux[i]!=aux[l-i-1])
			return false;
	}
	return true;
}
int main(){
	int t=0,cas,diff;
	ull i,j,a,b;
	S[0]=0;
	for(i=1;i<MAXN;i++){
		if(_palin(i) && _palin(i*i)) t++;
		S[i]=t;
	}
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%lld%lld",&i,&j);
		a=(ull)sqrt(i);
		b=(ull)sqrt(j);
		if(a*a<i) a++;
		j=b*b;
		diff = S[b]-S[a]+((_palin(a) && _palin(a*a))?1:0);//((b*b==j)?1:0);
		printf("Case #%d: %d\n",cas,diff);//);
	}
	return 0;
}
