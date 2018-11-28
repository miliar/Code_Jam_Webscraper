/*
 * ID: sfiction
 * COMP: GCJ
 * ROUND: Qualification
 * PROB: C
 */
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int MAXL = 1E4 + 10;
const int mult[5][5] = {{0, 1, 2, 3, 4},
						{1, 1, 2, 3, 4},
						{2, 2, -1, 4, -3},
						{3, 3, -4, -1, 2},
						{4, 4, 3, -2, -1}};

int L;
long long X;
char S[MAXL], T[MAXL << 3];

int product(){
	int ans = 1, sign;

	for (int i=0;i<L;++i){
		sign = ans > 0 ? 1 : -1;
		ans = sign * mult[ans * sign][S[i] - 'i' + 2];
	}

	sign = ans > 0 ? 1 : -1;
	ans *= sign;
	if (ans > 1)
		ans = (X & 2 ? -1 : 1) * (X & 1 ? ans : 1);
	sign = X & 1 ? sign : 1;

	return ans * sign;
}

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi=1;casi<=cas;++casi){
		printf("Case #%d: ", casi);
		cin >> L >> X;
		scanf("%s", S);
		if (product() != -1){
			puts("NO");
			continue;
		}

		T[0] = '\0';
		for (int i=0;i<8 && i<X;++i)
			strcat(T, S);
//		fprintf(stderr, "CASE:%d %5d %d\n", casi, strlen(T) / strlen(S), X);
		int pro = 1, sign, l = 0;

		for (;pro != 2 && T[l] && l<4*L;++l){
			sign = pro > 0 ? 1 : -1;
			pro = sign * mult[pro * sign][T[l] - 'i' + 2];
		}
		if (pro != 2){
			puts("NO");
			continue;
		}

		for (;pro != 4 && T[l] && l<8*L;++l){
			sign = pro > 0 ? 1 : -1;
			pro = sign * mult[pro * sign][T[l] - 'i' + 2];
		}
		if (pro != 4){
			puts("NO");
			continue;
		}

		puts("YES");
	}
	return 0;
}
