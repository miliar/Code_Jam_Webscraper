#include <stdio.h>
#include <string.h>
int main(void){
	freopen("A-large (2).in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t;
	scanf("%d", &t);
	char s[t][1001];
	for(int i=0; i<t; i++){
		scanf("%s",s[i]);
	}
	for(int i=0; i<t; i++){
		int l = strlen(s[i]);
		char a[l+1];
		a[l] = NULL;
		a[0] = s[i][0];
		for(int j=1; j<l; j++){
			if(s[i][j] >=a[0]){
				for(int k=j; k>0; k--){
					a[k] = a[k-1];
				}
				a[0] = s[i][j];
			}
			else{
				a[j] = s[i][j];
			}
		}
		printf("Case #%d: %s\n", i+1, a);
	}
	return 0;
}
