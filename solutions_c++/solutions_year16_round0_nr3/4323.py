#include <cstdio>
#include <cmath>
#include <vector>
#include <iostream>
using namespace std;

long long changeBase(long long num,int base){
	long long i=0,a=1;
	while(num>a){
		++i;
		a*=10;
	}
	long long ans=0;
	while(i--){
		a/=10;
		ans*=base;
		ans+=(num/a)%10;
	}
	return ans;
}

long long tenToTwo(long long num){
	long long ans=0,a=1;
	while(num){
		ans+=(num%2)*a;
		num/=2;
		a*=10;
	}
	return ans;
}

long long findFactor(long long num){
	long long root=sqrt(num);
	for(long long i=2;i<root;++i)
		if(!(num%i))
			return i;
	return 0;
}

long long pow2(long long a){
	int ans=1,i=0;
	while(i<a){
		ans*=2;
		++i;
	}
	return ans;
}

void solve(int x){
	int n,j;
	vector<long long> v(11,0);
	scanf("%d %d",&n,&j);
	printf("Case #%d:\n",x);
	long long start,stop=pow2(n),bi;
	int cou=0,k;
	bool chk;
	for(start=pow2(n-1)+1;start<stop;start+=2){
		chk=true;
		if(cou==j){
			return;
		}
		bi=tenToTwo(start);
		for(k=2;k<=10;++k){
			v[k]=findFactor(changeBase(bi,k));
			if(v[k]==0)
				chk=false;
		}
		if(chk){
			printf("%lld ",bi);
			for(k=2;k<=10;++k)
				printf("%lld ",v[k]);
			printf("\n");
			++cou;
		}
	}
}

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;++i)
		solve(i);
	return 0;
}