#include <cstdio>
#include <cstdlib>
#include <cstring>

int other_forward(char* S, char sign, int start, int end) {
	for (; start < end; ++start)
		if (S[start] != sign)
			break;
	return start;
}
int other_backward(char* S, char sign, int start, int end) {
	for (; start < end; --end)
		if (S[end-1] != sign)
			break;
	return end;
}

int flips_opt(char* S, int L) {
	
	int start = 0, end = L, flips = 0;
	end = other_backward(S, '+', start, end);
	if (S[0] == '-')
		flips = -1;

	while (1) {
		start = other_forward(S, '+', start, end);
		if (start >= end) return flips;
		++flips;
		start = other_forward(S, '-', start, end);
		++flips;
		if (start >= end) return flips;

		end = other_backward(S, '-', start, end);
		if (start >= end) return flips;
		++flips;
		end = other_backward(S, '+', start, end);
		++flips;
		if (start >= end) return flips;
	}


}

int main(int argc, char const *argv[]) {
	
	int T, L;
	char S[256];
	scanf("%d\n", &T);

	for (int i = 0; i < T; ++i)
	{
		fgets(S, 256, stdin);
		L = strlen(S);
		if (S[L - 1] == '\n') {
			--L; S[L] = '\0';
		}
		printf("Case #%d: %d\n", i+1, flips_opt(S, L));
	}

	return 0;
}