#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<vector>
#include<iostream>
#include<map>
#include<set>

using namespace std;

set<unsigned long long int> s;

int isPal(int num){
	int n = num;
	int rev = 0;
	while(num>0){
		int dig = num%10;
		rev = rev*10 + dig;
		num /= 10;
	}
	if(n == rev) return 1;
	return 0;
}

int main(){

	int tt;
	scanf("%d",&tt);
	
	for(unsigned long long int i = 1;i<=10000000;i++){
		if(isPal(i)){
			unsigned long long int aux = i*i;
			if(isPal(aux)){
				s.insert(aux);
			}
		}
	}
	
	for(int kk = 1;kk<=tt;kk++){
		printf("Case #%d: ",kk);
		
		unsigned long long int a,b,cont=0;
		scanf("%lld %lld",&a,&b);
		
		for(set<unsigned long long int>::iterator it = s.begin();it!=s.end();it++){
			if((*it)>=a && (*it)<=b)
				cont++;
		}
		
		printf("%lld\n",cont);
	}

	return 0;
}
