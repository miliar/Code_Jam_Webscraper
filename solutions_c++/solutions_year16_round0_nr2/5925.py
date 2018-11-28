#include <cstdio>
#include <cstring>

char invert(char c)
{
	if(c == '+') return '-';
	else if (c == '-') return '+';
	else return c;
}

void flip(char* st, int n)
{
	int i = 0;
	while(n > i)
	{
		char temp = st[i];
		st[i] = invert(st[n]);
		st[n] = invert(temp);
		n--;
		i++;
	}
	if(n == i)
	{
		st[n] = invert(st[n]);
	}
}

char S[101];

int func(char* S)
{
	int last_minus = -1, pos = 0, steps = 0;
	while(S[pos])
	{
		if(S[pos] == '-') last_minus = pos;
		pos++;
	}
	while(last_minus != -1)
	{
		if(S[last_minus] == '+')
		{
			last_minus--;
			continue;
		}
		if(S[0] == '-')
		{
			flip(S, last_minus);
			steps++;
		}
		else
		{
			int last_non_commited_plus = last_minus - 1;
			while(last_non_commited_plus && S[last_non_commited_plus] != '+') 
				last_non_commited_plus--;
			flip(S, last_non_commited_plus);
			steps++;
			flip(S, last_minus);
			steps++;
			last_minus--;
		}
	}
	return steps;
}
int main()
{
	int T;
	scanf("%d", &T);
	for(int caseno = 1; caseno <= T; caseno++)
	{
		scanf("%s", S);
		printf("Case #%d: %d\n", caseno, func(S));
	}
	return 0;
}
