#include <cstdio>
#include <cstring>
using namespace std;
char S[105];
bool check()
{
	int i,len = strlen(S);
	for (i = 0; i < len; ++i)
	{
		if (S[i] == '-')
			return false;
	}
	return true;
}
char change(char ch)
{
	char ret;
	if (ch == '+')
		ret = '-';
	else
		ret = '+';
	return ret;
}
int main()
{
	int T,i,step;
	scanf("%d",&T);
	for (int cas = 1; cas <= T; ++cas)
	{
		scanf("%s",S);
		int len = strlen(S);
		printf("Case #%d: ",cas);
		for (step = 0; ; ++step)
		{
			if (check())
				break;
			for (i = 1; i < len && S[i] == S[0]; ++i)
				S[i] = change(S[i]);
			S[0] = change(S[0]);
		}
		printf("%d\n",step);
	}
	return 0;
}