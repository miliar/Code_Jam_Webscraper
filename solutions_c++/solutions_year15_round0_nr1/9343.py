#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int main(){
	int T, t;
	cin >> T;

	for(t=0; t<T; t++){
		int smax;
		cin >> smax;

		int cur = 0;
		int req = 0;

		int i, j, k;

		char a;
		scanf("%c", &a);

		for(i=0; i<=smax; i++){
			scanf("%c", &a);
			int n = (int)a - (int)'0';

			if(cur < i){
				int dif = i - cur;
				req += dif;
				cur += dif;
			}

			cur += n;
		}

		printf("Case #%d: %d\n", t+1, req);
	}

	return 0;
}