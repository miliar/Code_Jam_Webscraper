#include <stdio.h>
#include <stdbool.h>

#define r 0
#define p 1
#define s 2

int R, P, S, N, E;
int dummy;

int pole[10000];

struct tri {
	int a, b, c;
};

bool ismatch(int a, int w)
{
	return (a == w) || (((a + 1) % 3) == w);
}

struct tri win(int w, int lvl, int elvl, int pos)
{
	if (lvl == N - 1){
		pole[pos] = w;
		pole[pos + 1] = (w + 2) % 3;
		return {.a = ismatch(r, w), .b = ismatch(p, w), .c = ismatch(s, w)};
	}

	struct tri a = win(w, lvl + 1, elvl / 2, pos);
	struct tri b = win((w + 2) % 3, lvl + 1, elvl / 2, pos + elvl);
	return {.a = a.a + b.a, .b = a.b + b.b, .c = a.c + b.c};
}

bool vetsi(int bs, int a, int b){
	int m = b + bs;
	while (b < m && pole[a] == pole[b]){
		a++; b++;
	}

	int mapa[3] = {1, 0, 2};
	return mapa[pole[a]] > mapa[pole[b]];
}

void serad(void)
{
	for (int bs = 1; bs < E; bs *= 2){
		for (int i = 0; i < E; i += 2 * bs){
			if (!vetsi(bs, i, i + bs))
				continue;

			for (int j = i; j < i + bs; j++){
				int t = pole[j]; pole[j] = pole[j + bs]; pole[j + bs] = t;
			}
		}
	}
}

bool zkus(int w)
{
	struct tri a = win(w, 0, E / 2, 0);
	if (!(a.a == R && a.b == P && a.c == S))
		return false;

	char c[3] = {'R', 'P', 'S'};
	serad();
	for (int i=0; i<E; i++)
		printf("%c", c[pole[i]]);

	printf("\n");
	return true;
}

void vyres(void)
{
	dummy = scanf("%d %d %d %d", &N, &R, &P, &S);
	E = 1;
	for (int i=0; i<N; i++)
		E *= 2;

	if (zkus(r))
		return;
	else if (zkus(p))
		return;
	else if (zkus(s))
		return;
	else
		printf("IMPOSSIBLE\n");
}

int main(void)
{
	int T;
	dummy = scanf("%d", &T);
	for (int i=0; i<T; i++){
		printf("Case #%d: ", i + 1);
		vyres();
	}
}
