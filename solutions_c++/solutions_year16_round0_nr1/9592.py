#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool prueba(long long int n, long long  int d){

	vector <bool> v(10,false);
	long long res;

	for (long long int i=1LL;i<=d;i++){
		res = i*n;
		while (res>0LL){
			v[res%10LL] = true;
			res/=10LL;
		}
	}
	for(int i=0;i<10;i++){
		if(v[i]==false) return false;
	}
	return true;
}


int main(){

	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);
	
	int T;
	long long int n, lo, hi, multp, sol;

	scanf("%d", &T);

	for(int i=0;i<T;i++){
		scanf("%lld", &n);
		if(n==0LL) printf("Case #%d: INSOMNIA\n", i+1);
		else{
			lo=1LL;hi=2LL;
			while(1){
				if( prueba(n,hi) ){
					break;
				}
				else {lo = lo*2LL; hi = hi*2LL;}
			}
			sol = hi;
			while( lo<=hi ){
				long long int md=(lo+hi)/2LL;
				if (prueba(n,md)){
					sol=min(sol,md);
					hi=md-1LL;
				}
				else lo = md+1LL;
			}
			printf("Case #%d: %lld\n", i+1,sol*n);
		}
	}
	return 0;
}

