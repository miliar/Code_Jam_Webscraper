#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<stdio.h>
#include<string>
using namespace std;

int test;
FILE *fp = fopen("B-large.in", "r");
//FILE *fp = fopen("input.txt", "r");
FILE *fo = fopen("output.txt","w");
long long int n, p, r1, r2;

int main()
{
	fscanf(fp, "%d", &test);
	for(int t = 1; t <= test; t++) {
		//input
		fscanf(fp, "%lld %lld", &n, &p);

		// process
		long long int s = 1, s2;
		for(int i = 0; i < n; i++) s *= 2;
		s2 = s;
		long long int cut = s-1;
		long long int T = s;

		if (s == p) {
			r1 = p-1;
			r2 = p-1;
		}
		else {
			// could
			for(long long int i = 1; i <= T; i *= 2) {
				cut -= i;
				s /= 2;
				if(s <= p) {
					r2 = cut;
					break;
				}
			}

			// gurantee
			long long int now = s2 / 2, temp = 2, res = 0, dt = s2 / 4;
			for(long long int i = 0; i < n; i++) {
				if (p <= now) {
					r1 = res;
					break;
				}
				res += temp;
				temp *= 2;
				now += dt;
				dt /= 2;
			}
		}

		// output
		fprintf(fo, "Case #%d: %lld %lld\n", t, r1, r2);
	}

	fclose(fp);
	fclose(fo);
	//scanf("%d");
	return 0;
}