#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <string.h>

using namespace std;
bool s[101];
int size;

bool check(){
	for(int i=0;i<size;i++) if(!s[i]) return false;
	return true;
}

int count(){
	int  i = 1; bool f = s[0];
	while(i<size && s[i] == f) i++;
	return i;
}

void flip(int n){
	int b=0, e=n-1; bool aux;
	while(b<=e){
		aux = s[b];
		s[b] = !s[e]; s[e] = !aux;
		b++; e--;
	}
}

int solve(){
	int res = 0;
	while(!check()){
		flip(count());
		res++;
	}
	return res;
}

int main(){
	int t;
	cin >> t;

	for(int test=1; test <= t; test++){
		string l; cin >> l; size = (int)l.size();
		for(int i=0;i<size;i++) s[i] = (l[i] == '+' ?true :  false);

		printf("Case #%d: %d\n", test, solve());
	}

	return 0;
}