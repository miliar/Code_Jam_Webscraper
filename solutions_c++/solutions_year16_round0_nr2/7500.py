#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int output[101],out[101],num;
char flag[101];

int calc(int len)
{
	int counter = 1, last = output[0];
	for(int i = 1; i<len;i++)
	{
		if(output[i] != last)
		{
			last = output[i];
			counter++;
		}
	}
	if(last == 1)
		counter--;
	return counter;
}
int main()
{
	scanf("%d",&num);
	for(int i=0;i<num;i++)
	{
		scanf("%s",flag);
		int length = strlen(flag);
		for(int j=0;j<length;j++)
		{
				if(flag[j]=='+')
					output[j]=1;
				else
					output[j]=0;
		}
		out[i]=calc(length);
	}
	for(int i=0;i<num;i++)
		printf("Case #%d: %d\n",i+1,out[i]);
}
