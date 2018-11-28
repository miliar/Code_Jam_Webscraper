#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main()
{
    freopen("C:\\Users\\Administrator\\Desktop\\D-large.in", "r", stdin);
    freopen("C:\\Users\\Administrator\\Desktop\\1.out", "w", stdout);
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        int N; scanf("%d", &N);
        double A[N], B[N];
        for (int i = 0 ; i < N; ++i)
        	scanf("%lf", &A[i]);
        for (int i = 0 ; i < N; ++i)
            scanf("%lf", &B[i]);

        sort(A, A+N);
        sort(B, B+N);

        // war
        int j = 0, res_war = 0;
        for (int i = 0; i < N; ++i) {
        	while (j < N && A[i] >= B[j])
        		j++;
        	if (j == N) {
        		res_war = N - i;
        		break;
        	} else {
        		j++;
        	}
        }

        // deceitful war
        int i = 0, m = 0, n = N-1, res_dec = 0;
        while (i < N && m < N && n >= m) {
        	if (A[i] > B[m]) {
        		i++;
        		m++;
        		res_dec++;
        	} else if (A[i] <= B[n]) {
        		i++;
        		n--;
        	}
        }

        printf("%d %d\n", res_dec, res_war);

    }
    return 0;
}
