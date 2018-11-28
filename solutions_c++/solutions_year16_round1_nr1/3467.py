
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm> 
using namespace std;

char str[1007], ans[1007];

int main(){
		
	
	//freopen("A-large.in", "r", stdin) ;
	//freopen("Alarge.out", "w", stdout);
	int tcase;
	cin >> tcase;
	for(int tca = 1;tca <= tcase; ++tca){
		
		scanf("%s", str);
		int len = strlen(str);
		ans[0] = str[0];
		for(int i = 1;i < len; ++i){
			if(str[i] >= ans[0]){
				for(int j = i - 1;j >= 0; --j){
					ans[j + 1]= ans[j];
				}
				ans[0] = str[i];
			}
			else{
				ans[i] = str[i];
			}
		}
		ans[len] = '\0';
		printf("Case #%d: %s\n", tca, ans);
	} 
	
	return 0;
}
