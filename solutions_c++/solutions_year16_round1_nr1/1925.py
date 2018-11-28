#include <stdio.h>
#include <memory.h>

using namespace std;

char S[1005];
char res[1005];

void solve()
{
	char tmp[2005];
	int tpa=1001,tpb=1002;
	memset(tmp,0,sizeof(tmp));
	tmp[tpa]=S[0];
	for(int i=1;i<strlen(S);i++)
	{
		if(S[i] < tmp[tpa])
			tmp[tpb++] = S[i];
		else
			tmp[--tpa] = S[i];
	}
	int j=0;
	for(int i=tpa;i<tpb;i++)
	{
		res[j++] = tmp[i];
	}
	res[j] = '\0';
}

int main()
{
	int i, j, k;
	int T, x;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//freopen("A-large-practice.in","r",stdin);
	//freopen("A-large-practice.out","w",stdout);
	scanf("%d",&T);
	x=1;
	while(T--)
	{
		scanf("%s",&S);
		printf("Case #%d: ",x++);
		solve();
		printf("%s\n",res);

	}
}