#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tc;
	scanf("%d", &tc);


	for(int i = 1; i <= tc; i++){

		int x,p = 1,temp,kount = 0,ans;
		scanf("%d", &x);

		if(x == 0){  printf("Case #%d: INSOMNIA\n",i); }

		else{
			int ara[11] = {0};

			temp = x;

			while(1){
				kount = 0;
				temp = x*p;
				while(temp != 0){
					int y = temp%10;
					ara[y]++;
					temp /= 10;
				}
				for(int j = 0; j <= 9; j++){
					if(ara[j] > 0) kount++;
				}
				ans = x*p;
				//printf("%d\n", ans);
				p++;
				if(kount == 10) break;

			}
			printf("Case #%d: %d\n", i,ans);
		}
	}

	return 0;
}
