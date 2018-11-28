#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

const int maxn = 100+8;

int T;
char P[maxn];

bool OK(int& bottom)//////////////////////////////////
{
	while(bottom>=0 && P[bottom]=='+')bottom--;

	return bottom < 0;
}

char opsit(char c)///////////////////////////////////
{
	char ans;
	if(c=='-')ans = '+';
	else ans = '-';

	return ans;
}

void flip(int bottom)////////////////////////////////
{
	for(int i=0;i<=bottom/2;i++)
	{
		int j = bottom-i;
		if(i==j)
			P[i] = opsit(P[i]);
		else
		{
			char tmp = P[i];
			P[i] = opsit(P[j]);
			P[j] = opsit(tmp);
		}
	}
}

int solve()//////////////////////////////////////////
{
	int ans = 0;
	int n = strlen(P);
	int top = 0,bottom = n-1;

	while(true)
	{
		if(OK(bottom))return ans;

		int j = top;

		while(P[j]=='+')j++;

		j--;

		if(j>=0){flip(j);ans++;}

		if(OK(bottom))return ans;

		flip(bottom);ans++;
	}

}

int main()///////////////////////////////////////////
{
//	freopen("..\\input.txt","r",stdin);
//	freopen("..\\B-small-attempt2.in","r",stdin);
//	freopen("..\\B-small-attempt2.out","w",stdout);

	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B-large.out","w",stdout);

	scanf("%d",&T);

	for(int kase=1;kase<=T;kase++)
	{
		scanf("%s",P);
		printf("Case #%d: %d\n",kase,solve());
	}
	return 0;
}