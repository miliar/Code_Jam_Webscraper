#include <iostream>
#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;

int main(){
	int tests;
	scanf("%d", &tests);
	char *s = (char *) malloc(sizeof(2000));
	for (int test = 1; test <= tests; ++test){
		int sMax;
		scanf("%d %s", &sMax, s);
		int now = 0, need = 0;
		for (int i = 0; i <= sMax; ++i){
			if (s[i] == '0') continue;
			if (now < i){ 
				need += i - now;
				now = i + s[i] - '0';
			}
			else
				now += s[i] - '0';
		}	
		printf("Case #%d: %d\n", test, need);
	}
	free(s);
	return 0;
}
