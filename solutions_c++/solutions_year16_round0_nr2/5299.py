#include <stdio.h>
int main(void){
	freopen("B-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int n;
	scanf("%d", &n);
	char s[n][101];
	for(int i = 0; i < n; i++){
		scanf("%s", &s[i]);
	}
	for(int i = 0; i < n; i++){
		int j = 0, count = 0;
		if(s[i][1] == NULL){
			if(s[i][0] == '-'){
				s[i][0] = '+';
				count++;
			}
		}
		while(s[i][j+1] != NULL){
			if(s[i][j] != s[i][j+1]){
				for(int k = 0; k <= j ; k++){
					if(s[i][k] == '+'){
						s[i][k] = '-';
					}
					else{
						s[i][k] = '+';
					}
				}
				count++;
			}
			j++;
		}
		if(s[i][j-1] == '-'){
			count++;
		}
		printf("Case #%d: %d\n", i+1, count);
	}
}
