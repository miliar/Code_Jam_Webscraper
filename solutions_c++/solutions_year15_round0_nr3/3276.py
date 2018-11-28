#include <cstdio>
int state_table[4][4] = {{0, 1, 2, 3},
						{1, 0, 3, 2},
						{2, 3, 0, 1},
						{3, 2, 1, 0}};
int sign_table[4][4] = {{1, 1, 1, 1},
						{1, -1, 1, -1},
						{1, -1, -1, 1},
						{1, 1, -1, -1}};
bool find_i(int l, int x, char* str);
bool find_j(int l, int x, char* str, int sl, int sx);
bool find_k(int l, int x, char* str, int sl, int sx);
//#define __DEBUG__
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		int l, x;
		char str[10001];
		scanf("%d %d %s", &l, &x, str);
		if(find_i(l, x, str)) printf("Case #%d: YES\n", i);
		else printf("Case #%d: NO\n", i);
	}
	return 0;
}
bool find_i(int l, int x, char* str)
{
	int current_state = 0, current_sign = 1;
	for(int i=0; i<x; i++){
		for(int j=0; j<l; j++){
			int input = str[j] == 'i' ? 1 : str[j] == 'j' ? 2 : 3;
			#ifdef __DEBUG__
			printf("%dth character of %dth repeat: %d in find_i\n", j, i, input);
			#endif
			current_sign *= sign_table[current_state][input];
			current_state = state_table[current_state][input];
			if(current_state * current_sign == 1){
				#ifdef __DEBUG__
				printf("found i!\n");
				#endif
				if(find_j(l, x, str, j+1, i)){
					return true;
				}
				else return false;
			}
		}
	}
	return false;
}
bool find_j(int l, int x, char* str, int sl, int sx)
{
	int current_state = 0, current_sign = 1;
	for(int i=sx; i<x; i++){
		for(int j=0; j<l; j++){
			if(j == 0 && i == sx){
				if(sl >= l){
					i++;
					if(i >= x) return false;
				}
				else j = sl;
			}
			int input = str[j] == 'i' ? 1 : str[j] == 'j' ? 2 : 3;
			#ifdef __DEBUG__
			printf("%dth character of %dth repeat: %d in find_j\n", j, i, input);
			#endif
			current_sign *= sign_table[current_state][input];
			current_state = state_table[current_state][input];
			if(current_state * current_sign == 2){
				#ifdef __DEBUG__
				printf("found j!\n");
				#endif
				if(find_k(l, x, str, j+1, i)){
					return true;
				}
				else return false;
			}
		}
	}
	return false;
}
bool find_k(int l, int x, char* str, int sl, int sx)
{
	int current_state = 0, current_sign = 1;
	for(int i=sx; i<x; i++){
		for(int j=0; j<l; j++){
			if(j == 0 && i == sx){
				if(sl >= l){
					i++;
					if(i >= x) return false;
				}
				else j = sl;
			}
			int input = str[j] == 'i' ? 1 : str[j] == 'j' ? 2 : 3;
			#ifdef __DEBUG__
			printf("%dth character of %dth repeat: %d in find_k\n", j, i, input);
			#endif
			current_sign *= sign_table[current_state][input];
			current_state = state_table[current_state][input];
		}
	}
	if(current_state * current_sign == 3){
		#ifdef __DEBUG__
		printf("found k!\n");
		#endif
		return true;
	}
	return false;
}