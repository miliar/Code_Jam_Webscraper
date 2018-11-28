#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "memory.h"

char count[1000];

char inp[10000];

int ans[100];

int main()
{
	int n;
	scanf("%d",&n);
	int i,j,k;
	for (k=0;k<n;k++)
	{
	scanf("%s",inp);
	memset(ans,0,sizeof(ans));
	memset(count,0,sizeof(count));
	int len = strlen(inp);
	for (i=0;i<len;i++)
	{
		count[inp[i]] ++;
	}
	//0
	ans[0] += count['Z'];
	count['E'] -= count['Z'];
	count['R'] -= count['Z'];
	count['O'] -= count['Z'];
	count['Z'] = 0;
	//2
	ans[2] += count['W'];
	count['T'] -= count['W'];
	count['O'] -= count['W'];
	count['W'] = 0;
	//6
	ans[6] += count['X'];
	count['S'] -= count['X'];
	count['I'] -= count['X'];
	count['X'] = 0;
	//8
	ans[8] += count['G'];
	count['E'] -= count['G'];
	count['I'] -= count['G'];
	count['H'] -= count['G'];
	count['T'] -= count['G'];
	count['G'] = 0;
	//3
	ans[3] += count['H'];
	count['T'] -= count['H'];
	count['R'] -= count['H'];
	count['E'] -= 2*count['H'];
	count['H'] = 0;
	//4
	ans[4] += count['R'];
	count['F'] -= count['R'];
	count['U'] -= count['R'];
	count['O'] -= count['R'];
	count['R'] = 0;
	//5
	ans[5] += count['F'];
	count['I'] -= count['F'];
	count['V'] -= count['F'];
	count['E'] -= count['F'];
	count['F'] = 0;
	//7
	ans[7] += count['V'];
	count['S'] -= count['V'];
	count['E'] -= 2*count['V'];
	count['N'] -= count['V'];
	//1
	ans[1] += count['O'];
	count['N'] -= count['O'];
	count['E'] -= count['O'];
	count['O'] = 0;
	//9
	ans[9] = count['I'];
	printf("Case #%d: ",k+1);
	for (i=0;i<10;i++)
	{
		for (j=0;j<ans[i];j++)
		{
			printf("%d",i);
		}
	}
	printf("\n");
	}
	return 0;
}
