#include <cstdio>
using namespace std;
const int MAXN = 1123456;
bool mark[9];
int lidos;

void contar( int x )
{
	int dig;
	while ( x != 0 ) {
		dig = x % 10;
		if ( mark[dig] == false ) {
			mark[dig] = true; lidos++;
		}
		x = x/10;
	}
}

int main()
{
	int T, tc = 1;
	scanf("%d", &T);
	while ( T-- ) {
		int N;
		scanf("%d", &N);
		lidos = 0;
		for ( int i = 0; i <= 9; i++ ) {
			mark[i] = false;		
		}
		int aux = 0;
		while ( lidos <= 9 && N != 0 ) {
			aux += N;
			contar(aux);
		}
		if ( aux != 0)
			printf("Case #%d: %d\n", tc++, aux);
		else
			printf("Case #%d: INSOMNIA\n", tc++);
	}
	return 0;
}
