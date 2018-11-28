#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <stdlib.h>
#include <set>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <unistd.h>
#include <stack>
#include <sstream>
#include <iomanip>
#include <bitset>
#define ff first
#define ss second

using namespace std;

typedef long long ll;

int main() {
	int t,n,tc=1,i;
	char s[105];

	scanf("%d", &t);
	while(t--){
		scanf("%s", s);
		n = strlen(s);
		
		int ans = 0, happy = 0;
		for(i = 0; i < n; i++){
			if(s[i] == '+') happy++;
		}
		while(happy < n){
			int last = -1;
			for(i = 0; i < n; i++)
				if(s[i] == '-') last = i;
			//flip
			for(i = 0; i <= last; i++){
				if(s[i] == '+'){happy--; s[i] = '-';}
				else{happy++; s[i] = '+';}
			}
			ans++;
		}
		printf("Case #%d: %d\n", tc++, ans);
	}

	return 0;
}
