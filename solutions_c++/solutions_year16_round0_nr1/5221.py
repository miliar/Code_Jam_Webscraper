#include <stdio.h>
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t;
	scanf("%d", &t);
	int n[t];
	for(int i=0; i < t; i++){
		scanf("%d",&n[i]);
	}
	for(int i=0; i < t; i++){
		int c[10] = {0}, b;
		if(n[i] == 0){
			printf("Case #%d: INSOMNIA\n", i + 1);
			continue;
		}
		int j = 1;
		while(c[0] == 0 || c[1] == 0 || c[2] == 0 || c[3] == 0 || c[4] == 0 || c[5] == 0 || c[6] == 0 || c[7] == 0 || c[8] == 0 || c[9] == 0){
			int a = n[i] * j;
			while (a > 0){
				int s = a % 10;
				a = a/ 10;
				c[s] = 1;
			}
			b = n[i] * j;
			j++;
		}
	printf("Case #%d: %d\n", i + 1, b);
	
	}
}
