/*
	GCJ - C - SMALL INPUT
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;
bool fairsquare[1000010];
bool palin(int p){
	if(p<10) return true;
	else{
		int p2=0;
		int p1=p;
		while(p>0){	
			int aux = p%10;
			p/=10;
			p2 = p2*10+aux;
		}
		if(p1==p2){
			return true;
		}
	}
	return false;
}
void sq(){
	memset(fairsquare, false, sizeof(fairsquare));
	fairsquare[1]=1;
	for(int i=2; i<=1000; i++){
		if(palin(i) && palin(i*i)) fairsquare[i*i]=true; 
	}
}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	sq();
	scanf("%d", &t);
	for(int ind=1; ind<=t; ind++){
		printf("Case #%d: ", ind);
		int a, b;
		scanf("%d %d", &a, &b);
		int cont=0;
		for(int i=a; i<=b; i++){
			if(fairsquare[i]) cont++;
		}
		printf("%d\n", cont);
	}
	return 0;
}
				