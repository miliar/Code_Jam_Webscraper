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

set<int> s;

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
	
	for(int i = 1;i<=1000;i++){
		if(isPal(i)){
			int aux = i*i;
			if(isPal(aux)){
				s.insert(aux);
			}
		}
	}
	
	for(int kk = 1;kk<=tt;kk++){
		printf("Case #%d: ",kk);
		
		int a,b,cont=0;
		scanf("%d %d",&a,&b);
		
		for(int i = a;i<=b;i++){
			if(s.find(i)!=s.end())
				cont++;
		}
		printf("%d\n",cont);
	}

	return 0;
}
