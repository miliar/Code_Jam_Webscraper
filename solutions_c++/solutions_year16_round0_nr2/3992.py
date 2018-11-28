#include <cstdio>
#include <cstring>

#define MAXS 110

bool check(char s[MAXS])
{
	int len = strlen(s);

	for(int i = 0; i < len; ++i) {
		if(s[i] == '-') {
			return false;
		}
	}

	return true;
}

void reverse(char s[MAXS])
{
	char top= s[0];
	int len = strlen(s);
	int pos = len;

	for(int i = 1; i < len; ++i) {
		if(s[i] != top) {
			pos = i;
			break;
		}
	}

	for(int i = 0; i < pos; ++i) {
		if(s[i] == '-')
			s[i] = '+';
		else if(s[i] == '+')
			s[i] = '-';
	}
}

int main()
{
	int T;

	scanf(" %d", &T);
	for(int caseId = 1; caseId <= T; ++caseId) {
		char s[MAXS];
		int count = 0;

		scanf(" %s", s);		
		int len = strlen(s);

		while(check(s) == false) {
			reverse(s);			
			count++;	
		}

		printf("Case #%d: %d\n", caseId, count);
	}

	return 0;
}
