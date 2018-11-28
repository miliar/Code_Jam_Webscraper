#include <stdio.h>
#include <vector>
#include <algorithm>

int motes[100];

using namespace std;

int min(int a, int b){
	return a<b? a : b;
}

int conta(int a, int n, int begin){
	if(a==1)	return n;
	if(a==100){
		int i=begin;
		while(motes[i]<100 && i<begin+n){
			i++;
		}
		return n - i;
	}
	if(motes[begin]>=a){
		if(n==1)	return 1;
		
		return min(n, 1+conta(a+a-1, n, begin));
	}
	
	
	int t=0;
	
	int i=begin;
	while(motes[i] < a && i<begin+n){
		a += motes[i];
		i++;
		t++;
	}
	
	if(i == begin+n)	return 0;
	
	return conta(a, n-t, begin+t);
	
}

int main(){
	int t, n, a, k=1;
	
	scanf("%d", &t);
	
	for(int i=0; i<t; i++){
		scanf("%d%d", &a,&n);
		for(int j=0; j<n; j++){
			scanf("%d", &motes[j]);
		}
		
		sort(motes, motes+n);
		
		printf("Case #%d: %d\n", k, conta(a,n,0));
		
		
		k++;
	}
	
	
	
	return 0;
}
