#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
using namespace std;
bool is_pa(int x){
	if(x/1000) return 0;
	if(x/100){
		if(x/100 == x%10){
			return 1;
		}
		else{
			return 0;
		}
	}
	if(x/10){
		if(x/10 == x%10){
			return 1;
		}
		else{
			return 0;
		}
	}
	return 1;
}
int is_sqrt(int x){
	for(int i=1;i*i<=x;i++){
		if(i*i==x) return i;
	}
	return 0;
}
int main(){
	freopen("C-small-attempt3.in","r",stdin);
	freopen("C-small-attempt3.out","w",stdout);
	int n;
	cin >> n;
	for(int i=1;i<=n;i++){
		int a,b;
		cin >> a >> b;
		int num = 0;
		for(int j=a;j<=b;j++){
			if(is_pa(j) && is_sqrt(j) && is_pa(is_sqrt(j)) )
				num++;
				
		}
		printf("Case #%d: %d\n",i,num);
	}
	return 0;
}
