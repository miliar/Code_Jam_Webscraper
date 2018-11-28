#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#define LL long long
using namespace std;
bool submit=true;
LL n,q,pow[55];
LL f1(LL id){//worst ranking
	LL l_l=id,r_r=pow[n]-id-1,rk=0,factor=pow[n-1];
	while(factor>0){
		if(l_l==0) return rk;
		else{
			l_l--;
			l_l/=2;
			r_r=factor-l_l-1;
			rk+=factor;
			factor/=2;
		}
	}
	return rk;
}
LL f2(LL id){//best ranking
	LL l_l=id,r_r=pow[n]-id-1,rk=0,factor=pow[n-1];
	while(factor>0){
		if(r_r==0) return rk+factor*2-1;
		else{
			r_r--;
			r_r/=2;
			l_l=factor-r_r-1;
			factor/=2;
		}
	}
	return rk;
}
int main(){
	if(submit){
		freopen("B-large.in.txt","r",stdin);
		freopen("B-large.out","w",stdout);
	}
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		cin >> n >> q;
		pow[0]=1;
		for(int i=1;i<=n;i++) pow[i]=pow[i-1]*2;
		LL lt=-1,rt=pow[n];
		while(rt-lt>1){
			LL m=(lt+rt)/2;
			if(f1(m)<q) lt=m;
			else rt=m;
		}
		printf("Case #%d: ",i);
		cout << lt;
		lt=-1,rt=pow[n];
		while(rt-lt>1){
			LL m=(lt+rt)/2;
			if(f2(m)<q) lt=m;
			else rt=m;
		}
		cout << " " << lt << endl;
	}
	return 0;
}
	
