#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>

using namespace std;
typedef long long int ll;

void update(ll k, vector<bool> &b){
	if(k==0) b[0]=true;
	else{
		while(k){
			b[k%10]=true;
			k/=10;
		}
	}
}
	
ll lastNum(int n){
	vector<bool> dgt(10,false);
	int dcnt=log10(n)+2;
	ll tmp=n;
	dcnt=pow(10,dcnt);
	while(dcnt--){
		update(tmp,dgt);
		bool f=true;
		for(int i=0; i<10; i++) f=f&&dgt[i];
		if(f) return tmp;
		tmp+=n;
	}
	return -1;
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		int n;
		scanf("%d",&n);
		if(n==0) printf("INSOMNIA\n");
		else{
			ll k=lastNum(n);
			if(k==-1) printf("INSOMNIA\n");
			else printf("%lld\n",k);
		}
	}
}
