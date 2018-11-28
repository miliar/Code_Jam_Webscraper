#include<iostream>
using namespace std;
int T,S;
char mem[1010];
int need=0;
int already=0;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int memnum=0;
	scanf("%d",&T);
	for(int k=1;k<=T;k++)
	{
		need=0;
		already=0;
		scanf("%d",&S);
		scanf("%s",mem);
		for(int i=0;i<=S;i++)
		{
			memnum=mem[i]-'0';
			if(already<i)
			{
				need+=i-already;
				already=i;
			}
			already+=memnum;
		}
		printf("Case #%d: %d\n",k,need);

	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}