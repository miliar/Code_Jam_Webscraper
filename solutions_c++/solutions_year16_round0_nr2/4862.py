#include<cstdio>
#include<cstring>
int main()
{
	int t;
	scanf("%d",&t);
	char str[101],shrunk[101];
	int i,j,k,z;
	for(z=0;z<t;z++)
	{
		scanf("%s",str);
		k=0;
		shrunk[k++]=str[0];
		for(i=1;i<strlen(str);i++)
		{
			if(str[i]==shrunk[k-1])
				continue;
			else
			{
				shrunk[k++]=str[i];
			}
		}
		shrunk[k]='\0';
		if(strlen(shrunk)%2)
		{
			if(shrunk[0]=='+')
				printf("Case #%d:\t%d\n",z+1,strlen(shrunk)-1);
			else
				printf("Case #%d:\t%d\n",z+1,strlen(shrunk));
		}
		else
		{
			if(shrunk[0]=='-')
				printf("Case #%d:\t%d\n",z+1,strlen(shrunk)-1);
			else
				printf("Case #%d:\t%d\n",z+1,strlen(shrunk));
		}
	}
	return 0;
}
