#include "cstdio"
#include "string.h"
int main(int argc, char const *argv[])
{
	int t,s;
	char si[1001];
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&s);
		scanf("%s",si);
		int sum = 0, inv = 0;
		int len = strlen(si);
		for(int j=0;j<len;j++){
			sum+= si[j]-'0';
            while(sum<(j+1)){
                si[j]++;
                inv++;
                sum++;
			}
		}
		printf("Case #%d: %d\n",i,inv);
	}
	return 0;
}
