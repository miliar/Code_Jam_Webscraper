
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm> 
using namespace std;
int main(){
		
	
	//freopen("B-large.in", "r", stdin) ;
	//freopen("Blarge.out", "w", stdout);
	int tcase;
	cin >> tcase;
	for(int tca = 1;tca <= tcase; ++tca){
		
		char s[105];
		scanf("%s", s);
		int len = strlen(s);
		int ans = 0;
		
		while(true){
			
			int pos = -1;
			for(int i = len - 1;i >= 0; --i){
				if(s[i] == '-'){
					pos = i;
					break;
				}
			}
			//cout << pos << endl;
			if(pos == -1) break;
			
			if(s[0] == '+'){
				for(int i = 0;i < pos; ++i){
					if(s[i] == '+') s[i] = '-';
					else break;
				}
				ans ++;
			}
			else{
				
			}
			ans ++;
			for(int i = 0, j = pos;i <= j; ++i, --j){
				swap(s[i], s[j]);
				if(s[i] == '-') s[i] = '+';
				else s[i] = '-';
				if(i == j) break;
				if(s[j] == '-') s[j] = '+';
				else s[j] = '-';
				
			}
		}
		printf("Case #%d: %d\n", tca, ans);
		
		
		
	}
	return 0;
}
