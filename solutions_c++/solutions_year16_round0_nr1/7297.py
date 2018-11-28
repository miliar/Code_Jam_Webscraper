#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

bool vis[15];

bool check(int x){
	
	do{
		vis[x % 10] = true;
	}while(x /= 10);
	for(int i = 0;i <= 9; ++i) if(!vis[i]) return false;
	return true;
	
}

int main(){
	
	//freopen("A-large.in", "r", stdin) ;
	//freopen("Alarge.out", "w", stdout);
	int tcase;
	cin >> tcase;
	for(int tca = 1;tca <= tcase; ++tca){
		int n;
		scanf("%d", &n);
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", tca);
			continue;
		}
		//n = tca;
		int cnt = 0;
		memset(vis, false, sizeof(vis));
		while(++cnt <= 100){
			if(check(cnt * n)) break;
		}
		printf("Case #%d: %d\n", tca, cnt * n);
		
	}
	
	return 0;
	
} 
