#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <string>
#include <iostream>
#include <algorithm>

#include <vector>
#include <map>
#include <queue>

#define dbg(a) cout << a << endl

using namespace std;

typedef long long ll;
char num[20];

bool isPalindrome(char str[]){
	int size = strlen(str);
	for(int i = 0, j = size-1; i < j; i++, j--){
		if(str[i] != str[j])
			return false;
	}
	return true;
}

ll fs(ll n){
	ll raiz = sqrt(n)+1, temp, resp = 0;

	for(ll i = 0; i <= raiz; i++){
		sprintf(num, "%d", i);
		if(isPalindrome(num)){
			temp = i*i;
			sprintf(num, "%d", temp);

			if(temp <= n && isPalindrome(num)){
				resp++;
			}
		}
	}

	return resp;
}

int main(){

	int t;
	ll a, b;
	scanf("%d", &t);

	for(int caso = 1; caso <= t; caso++){
		scanf("%lld %lld", &a, &b);

		printf("Case #%d: %lld\n", caso, fs(b)-fs(a-1));
	}

	return 0;
}
