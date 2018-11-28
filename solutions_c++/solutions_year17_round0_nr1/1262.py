#include <bits/stdc++.h>

using namespace std;

int t,i,j;
char s[1005];

int main(){
	
	freopen("A-large (4).in", "r", stdin);
	freopen("judge.out", "w", stdout);
	
	scanf("%d", &t);
	
	for(int tc = 1; tc <= t; tc++){
		int k;
		scanf("%s%d", s, &k);
		int l = strlen(s);
		
		int res = 0;
		
		for(i = 0; i < l - k + 1; i++){
			if(s[i] == '-'){
				res++;
				for(j = 0; j < k; j++){
					if(s[i + j] == '-')
					s[i + j] = '+';
					else
					s[i + j] = '-';
				}
			}
		}
		
		bool flag = 1;
		
		for(i = 0; i < l; i++)
		flag &= (s[i] == '+');
		
		printf("Case #%d: ", tc);
		
		if(!flag)
		printf("IMPOSSIBLE\n");
		else
		printf("%d\n", res);
	}
}

