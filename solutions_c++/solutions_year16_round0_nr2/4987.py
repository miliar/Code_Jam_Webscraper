#include<stdio.h>
#include<string.h>
int main()
{
    int zes;
    scanf("%d",&zes);
    for (int z=0;z<zes;z++)
    {
	char buf[105];
	scanf("%s",buf);
	char prev = buf[0];
	int res = (prev =='-') ? 1  : 0;
	for (int i =1;i<strlen(buf);i++)
	{
	    if(buf[i] != prev)
	    {
		prev = buf[i];
		if(prev=='-') res+=2;
	    }
	}
	printf("Case #%d: %d\n",z+1,res);

    }
}
