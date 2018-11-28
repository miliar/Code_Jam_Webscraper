#include <stdio.h>
#include <string.h>
int main()
{
	int n,num,length;
	char str[101];

	scanf("%d",&n);
	for(int i=0; i<n; i++)
	{
		scanf("%s",str);
		num=0;
		length = strlen(str);
		for(int i=0; i<length-1; i++)
			if(str[i] != str[i+1])
				num++;
		if(str[length-1] == '-')
			num++;
		printf("Case #%d: %d\n",i+1,num);
	}
	return 0;
}