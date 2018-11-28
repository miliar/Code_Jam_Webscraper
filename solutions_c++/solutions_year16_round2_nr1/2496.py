#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>

enum alphabet {A = 0, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z};


void zero (int * digits, int * letters) {
	int count = letters[Z];
	digits[0] += count;
	if (count) {
		letters[Z] -= count;
		letters[E] -= count;
		letters[R] -= count;
		letters[O] -= count;
	}
}

void one (int * digits, int * letters) {
	int count = letters[O];
	digits[1] += count;
	if (count) {
		letters[O] -= count;
		letters[N] -= count;
		letters[E] -= count;
	}
}

void two (int * digits, int * letters) {
	int count = letters[W];
	digits[2] += count;
	if (count) {
		letters[T] -= count;
		letters[W] -= count;
		letters[O] -= count;

	}
}

void three (int * digits, int * letters) {
	int count = letters[H];
	digits[3] += count;
	if (count) {
		letters[T] -= count;
		letters[H] -= count;
		letters[R] -= count;
		letters[E] -= count;
		letters[E] -= count;
	}
}

void four (int * digits, int * letters) {
	int count = letters[U];
	digits[4] += count;
	if (count) {
		letters[F] -= count;
		letters[O] -= count;
		letters[U] -= count;
		letters[R] -= count;

	}
}

void five (int * digits, int * letters) {
	int count = letters[F];
	digits[5] += count;
	if (count) {
		letters[F] -= count;
		letters[I] -= count;
		letters[V] -= count;
		letters[E] -= count;

	}
}

void six (int * digits, int * letters) {
	int count = letters[X];
	digits[6] += count;
	if (count) {
		letters[S] -= count;
		letters[I] -= count;
		letters[X] -= count;

	}
}

void seven (int * digits, int * letters) {
	int count = letters[V];
	digits[7] += count;
	if (count) {
		letters[S] -= count;
		letters[E] -= count;
		letters[V] -= count;
		letters[E] -= count;
		letters[N] -= count;

	}
}

void eight (int * digits, int * letters) {
	int count = letters[G];
	digits[8] += count;
	if (count) {
		letters[E] -= count;
		letters[I] -= count;
		letters[G] -= count;
		letters[H] -= count;
		letters[T] -= count;

	}
}

void nine (int * digits, int * letters) {
	int count = letters[I];
	digits[9] += count;
	if (count) {
		letters[N] -= count;
		letters[I] -= count;
		letters[N] -= count;
		letters[E] -= count;

	}
}

using namespace std;

int main(int argc, char const *argv[])
{

	int t;
	scanf("%d", &t);

	char s[2001];

	for (int i = 0; i < t; ++i) {

		int letters[26] = {0};
		int digits[10] = {0};
		scanf("%2000s", s);
		printf("Case #%d: ", i+1);

		int l = strlen(s);
		for (int i = 0; i < l; ++i)
		{
			int idx = s[i] - 'A';
			++letters[idx];
		}

		zero(digits, letters);
		two(digits, letters);
		four(digits, letters);
		five(digits, letters);
		six(digits, letters);
		seven(digits, letters);
		eight(digits, letters);
		nine(digits, letters);
		one(digits, letters);
		three(digits, letters);

		for (int i = 0; i < 10; ++i)
		{
			for (int j = 0; j < digits[i]; ++j)
			{
				printf("%c", '0'+i);
			}
		}

		printf("\n");
	}
}