#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

void SolveCase(int caseId);
int GetResult(int len);

char s[103];
char* S = s+1; 

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
		SolveCase(i);
	return 0;
}

void SolveCase(int caseId)
{
	scanf("%s", S);
	int len = strlen(S);
	printf("Case #%d: %d\n", caseId, GetResult(len));
}

int GetResult(int len)
{
	int result = 0;
	auto change = [](char &c)->void
	{
		c = c == '+' ? '-' : '+';
	};
	auto reduce = [&len]()->bool
	{
		while(s[len] == '+')
			--len;
		return len == 0;
	};
	while(true)
	{
		if(reduce())
			break;
		if(s[1] == '+')
		{
			int d = 1;
			while(S[d] == '+')
				++d;
			reverse(S, S+d);
			for_each(S, S+d, change);
			++result;
		}
		if(reduce())
			break;
		reverse(S, S+len);
		for_each(S, S+len, change);
		++result;
	}
	
	return result;
}


