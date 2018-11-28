#include "cstdio"
#include "cstring"
int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	char pancake[105];
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int count = 0;
		scanf("%s",pancake);
		int size = strlen(pancake);
		for(int j=1;j<size;j++){
			if(pancake[j-1] != pancake[j]){
				for(int k=0;k<j;k++){
					if(pancake[k] == '+'){
						pancake[k] = '-';
					}
					else if(pancake[k] == '-'){
						pancake[k] = '+';
					}
				}
				j = 1;
				count++;
			}
		}
		if(pancake[0] == '-'){
			count++;
		}
		printf("Case #%d: %d\n",i+1, count);
	}
	return 0;
}