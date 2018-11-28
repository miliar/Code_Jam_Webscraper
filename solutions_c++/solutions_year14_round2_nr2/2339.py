#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
#include<algorithm>
#define INF 999999999
using namespace std;
int main()
{
	freopen("/home/jb/Downloads/input.txt", "r", stdin);
	freopen("/home/jb/Downloads/output.txt", "w", stdout);
	int TC, T;
	scanf("%d", &TC);
	for (T = 1; T <= TC; T++){
		int a,b,k,j, j2, wins;
		wins = 0;
		printf("Case #%d: ", T);
		scanf("%d %d %d", &a, &b, &k);
		for (j = 0; j < a; j++) {
			for (j2 = 0; j2 < b; j2++) {
				if ((j & j2) < k) {
					wins++;
				}
			}
		}
		printf("%d\n", wins);
	}

}
