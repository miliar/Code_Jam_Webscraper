#include <stdio.h>
#include <string.h>
// #include <math.h>

int numTestCases = 0, kase = 0;
int result = 0;


int t = 0, l = 0;
char str[10010] = {0};
char single[10000] = {0};

inline int abs(int a) {
	return a > 0 ? a : -a;
}
#define I (0)
#define J (1)
#define K (2)
#define E (3)
#define _I (4)
#define _J (5)
#define _K (6)
#define _E (7)

#if 1
	#define log(fmt, arg...)\
		fprintf(stderr, "[%s:%d] " fmt "\n", __func__, __LINE__, ## arg)
#else
	#define log(...) void(0)
#endif

// i=0,j=1,k=2,1=3;-i=4,-j=5,-k=6,-1=7
// state[now][input]
int i_tr[8][3] = {
	{_E, K, _J},
	{_K, _E, I},
	{J, _I, _E},
	{I, J, K},
	{E, _K, J},
	{K, E, _I},
	{_J, I, E},
	{_I, _J, _K}
};

int k_tr[8][3] = {
	{_E, _K, J}, 
	{K, _E, _I}, 
	{_J, I, _E},
	{I, J, K},
	{E, K, _J}, 
	{_K, E, I}, 
	{J, _I, E},
	{_I, _J, _K},
};

int handleQ() {
	int shift = 0;
	int i = 0, j = 0, k = 0;
	int last_state = E, state_i = E, state_k = E;
	int i_idx = 0, k_idx = 0;

	for (i = 0; i < t; i++) {
		shift += snprintf(str+shift, 10001, "%s", single);
	}
	log("str: %s", str);

	for (last_state = E, i = 0; i < shift; i++) {
		last_state = i_tr[last_state][str[i]-'i'];
	}

	log("last_state:%d", last_state);
	if (last_state == _E) {
		for (state_i = E, i = 0; i < shift-1; i++) {
			state_i = i_tr[state_i][str[i]-'i'];
			if (state_i == I) {
				log("Found I:%d", i);
				for (state_k = E, k = shift-1; k > i; k--) {
					state_k = k_tr[state_k][str[k]-'i'];
					if (state_k == K) {
						log("Found I:%d K:%d", i, k);
						return 1;
					}
				}
			}
		}
	}
	return 0;
}

int main() {
	scanf("%d", &numTestCases);

	for (kase = 0; kase < numTestCases; kase++) {
		scanf("%d %d", &l, &t);
		scanf("%s", single);

		result = handleQ();

		printf("Case #%d: %s\n", kase+1, result ? "YES" : "NO");

		memset(str, 0, sizeof(str));
		memset(single, 0, sizeof(single));
	}

	return 0;
}