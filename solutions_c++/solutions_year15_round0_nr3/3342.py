#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;

#define MOD 1000000007
#define rec(i, n) for(int i = 0; i < n; i++)
#define max(a,b) ((a)>(b))?(a):(b)
#define u unsigned

int T, L, X;
int arr[5][5] = { {0,1,2,3,4}, {1,1,2,3,4}, {2,2,-1,4,-3}, {3,3,-4,-1,2}, {4,4,3,-2,-1}};

// 1 =1 , i = 2, j = 3, k = 4
int v[10001];

int i, j, k, turn = 1;
int main() {
	scanf("%d", &T);
	while(T--) {
		scanf("%d %d", &L, &X);
        string s;
        cin>>s;
        int l = s.length();

        k = 0;
        for ( i = 0; i < X; i++) {
            for (j = 0; j < l; j++) {
                v[k++] = s[j] - 'g';
            }
        }

        int state = 0;
        int buffer = 0;
        bool negative = false;

        for(i = 0; i < k; i++) {

            buffer = arr[buffer][v[i]];
            if (negative) buffer *= -1;

            if (state == 0 && buffer == 2) {
                // means i
                state++;
                buffer = 0;
            } if (state == 1 && buffer == 3) {
                state++;
                buffer = 0;

            } if (state == 2 && buffer == 4) {
                state++;
                buffer = 0;
            }

            if (buffer < 0) {
                buffer *= -1;
                negative = true;
            } else negative = false;
        }

        if (state == 3 && !negative) {
            if (buffer == 0 || buffer == 1)
                printf("Case #%d: %s\n", turn++, "YES");
            else printf("Case #%d: %s\n", turn++, "NO");
        } else printf("Case #%d: %s\n", turn++, "NO");

	}
}