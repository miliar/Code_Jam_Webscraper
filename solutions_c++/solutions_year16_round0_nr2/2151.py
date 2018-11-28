#include <cstdio>
#include <cstring>
using namespace std;
const int MAXS = 112;

char S[MAXS];

void inverte( int limite )
{
	for ( int i = 0; i <= limite; i++ ) {
		if ( S[i] == '-' ) S[i] = '+';
		else S[i] = '-';
	}
}

int main()
{
	int T, tc = 1;
	int count = 0;
	scanf("%d ", &T);
	while ( T-- ) {
		gets(S);
		int tam = strlen(S);
		count = 0;
		for ( int i = tam-1; i >= 0; i-- ) {
			if ( S[i] == '-' ) {
				inverte(i);
				count++;
			}
		}
		printf("Case #%d: %d\n", tc++, count);
	}
	return 0;
}