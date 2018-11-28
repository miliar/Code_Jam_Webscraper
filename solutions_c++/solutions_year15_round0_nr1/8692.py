#include <stdio.h>

char s [1005];

int main()
{
	int tc,n,i,counter,result,c=1;
	scanf("%d\n",&tc);

	while(tc--)
	{
		counter=0;
		result=0;
		scanf("%d ",&n);
		for(i=0;i<=n;i++){
			scanf("%c",&s[i]);
			if(counter<i){
				result=result+(i-counter);
				counter+=(i-counter);
			}
			counter=counter+(s[i]-'0');
			//printf("%d %d ",counter,result);
		}
		printf("Case #%d: %d\n",c++,result);

	}
}