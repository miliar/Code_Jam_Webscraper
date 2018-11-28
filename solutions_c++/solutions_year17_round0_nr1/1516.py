#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	int n;
	scanf("%d", &n);
	
	int i = 0;
	while(i < n){
		char s[1001];
		int k;
		scanf(" %s %d", s, &k); 
		//printf("%s", s);
		int j = 0;
		int l = strlen(s);
		int result = 0;
		while(j < l){
			//printf("%s\n", s);
			if(s[j] == '-')	{
				if(j > (l-k)){
					result = -1;
					break;
				}
				//flip pancakes
				int h = j;
				//printf("%d %d %d\n", h, j, k);
				while (h < j + k){
					if(s[h] == '-') {
						s[h] = '+'; 
					} else { 
						s[h] = '-';
					}
					h++;
				}
				result++;
			}
			j++;
		}
		printf("Case #%d: ", i+1);
		if(result == -1){
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", result);
		}
		
		i++;
	}

	return 0;
}