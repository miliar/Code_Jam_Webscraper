#include <cstdio>
#include <cstring>

const int MAXC = 105;
char buffer[MAXC]{ };
int A, L, T;
bool mode;

int main()
{
	scanf(" %d", &T);
	for(int _T = 1; _T <= T; ++_T)
	{
		A = 0;
		scanf(" %s", &buffer);
		printf("Case #%d: ", _T);
		L = strlen(buffer); mode = (buffer[0] == '+');
		for(int i = 0; i < L; ++i)
		{
			if(buffer[i] == '+')
			{
				if(!mode) A++;
				mode = true;
			}
			else
			{
				if( mode) A++;
				mode = false;
			}
		}
		if(buffer[L-1] == '-') A++;
		printf("%d\n", A);
	}
	return 0;
}