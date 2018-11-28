#include <cstdio>
#include <cstring>
inline char Flip(char ch)
{
	if('+' == ch)
		return '-';
	return '+';
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for(int i = 1; i <= T; ++i)
	{
		char S[101];
		scanf("%s", S);

		int lastblank = strlen(S)-1, count = 0;
		while(lastblank >= 0  && '+' == S[lastblank])
			--lastblank;

		while(lastblank >= 0)
		{
			if('+' == S[0])
			{
					//Flip top +
				int j = 0;
				while(j < lastblank && '+' == S[j])
				{
					S[j] = '-';
					++j;
				}

				++count;
			}

				//flip
			int start = 0, end = lastblank;
			while(start < end)
			{
				char temp = S[start];
				S[start] = Flip(S[end]);
				S[end] = Flip(temp);

				++start;
				--end;
			}
			if(start == end)
				S[start] = Flip(S[start]);
			++count;

				//Update lastblank
			while(lastblank >= 0  && '+' == S[lastblank])
				--lastblank;
		}
		
		printf("Case #%d: %d\n", i, count);
	}
	
	return 0;
}
