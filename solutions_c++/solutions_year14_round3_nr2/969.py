#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <string.h>
#include <queue>
#include <limits>
#include <map>
#include <string>
#include <iostream>

using namespace std;

int N;
string buf[10];

void solve();
int check();
int fact(int a);

int main(){
	int cases;
	scanf("%d", &cases);

	for(int i=1; i<=cases; i++){
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}

void solve(){
	scanf("%d", &N);
	int sum = 0;
	for(int i=0; i<N; i++){
		cin >> buf[i];
	}

	sort(buf, buf+N);

	int prod = 1;
	string scurr = buf[0];
	int count = 1;
	for(int i=1; i<N; i++){
		if(scurr.compare(buf[i])==0){
			count++;
		}else{
			scurr = buf[i];
			prod*=fact(count);
			count = 1;
		}
	}
	prod*=fact(count);


	do{
		sum += check();
	}while(next_permutation(buf, buf+N));

	printf("%d\n", sum*prod);
}

int check(){
	bool alfa[26];
	memset(alfa, 0, sizeof(alfa));
	char curr = '.';
	int sum = 1;

	for(int i=0; i<N; i++){
		for(int j=0; j<buf[i].length(); j++){
			if(buf[i][j]!=curr){
				curr = buf[i][j];
				if(alfa[curr-'a']){
					return 0;
				}else{
					alfa[curr-'a'] = true;
				}
			}
		}
	}
	return sum;
}

int fact(int a){
	int ret = 1;
	for(int i=2; i<=a; i++){
		ret*=i;
	}
	return ret;
}