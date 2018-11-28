#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

int main() {
	int test;
	FILE *fp = NULL;
	fp = fopen("A-large.in", "r");
	FILE *fp2 = NULL;
	fp2 = fopen("output.txt", "w");
	fscanf(fp, "%d", &test);

	for (int t = 1; t <= test; t++) {
		int n, num;
		priority_queue<pair<int, char>> q;
		fscanf(fp, "%d", &n);
		for (int i = 0; i < n; i++) {
			fscanf(fp, "%d", &num);
			q.push(make_pair(num, char('A' + i)));
		}

		fprintf(fp2, "Case #%d: ", t);
		char party1, party2;
		int num1, num2;
		while (!q.empty()) {
			if (q.size() == 1) {
				party1 = q.top().second;
				num1 = q.top().first;
				q.pop();
				if (num1 >= 2) {
					fprintf(fp2, "%c%c ", party1, party1);
				}
				fprintf(fp2, "%c ", party1);
			}
			else {
				party1 = q.top().second;
				num1 = q.top().first;
				q.pop();
				party2 = q.top().second;
				num2 = q.top().first;
				if (num1 > num2+1) {
					fprintf(fp2, "%c%c ", party1, party1);
					num1 -= 2;
					if (num1 > 0) {
						q.push(make_pair(num1, party1));
					}
				}
				else if (q.size() == 2 && num1 == 1) {
					fprintf(fp2, "%c ", party1);
					num1--;
					if(num1 > 0)
						q.push(make_pair(num1, party1));
				}
				else {
					fprintf(fp2, "%c%c ", party1, party2);
					num1--; num2--;
					q.pop();
					if (num1 > 0) {
						q.push(make_pair(num1, party1));
					}
					if (num2 > 0) {
						q.push(make_pair(num2, party2));
					}
				}
			}
		}
		fprintf(fp2, "\n");
	}

	return 0;
}