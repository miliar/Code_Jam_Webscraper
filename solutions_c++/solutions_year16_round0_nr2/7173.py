#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;

char str[201];

bool checkSmile() {
	int len = strlen(str);
	for (int i = 0; i < len; i++)
		if (str[i] == '-')
			return false;
	return true;
}

int main() {
	int t, n, left, right, count;
	FILE *fp = NULL;
	fp = fopen("B-large.in", "r");
	FILE *fp2 = NULL;
	fp2 = fopen("output.txt", "w");
	fscanf(fp, "%d", &t);

	for (int i = 1; i <= t; i++) {
		fscanf(fp, "%s", str);
		count = 0;
		left = 0, right = strlen(str) - 1;
		
		while (!checkSmile()) {
			if (str[left] == '+') {
				count++;
				while(str[left] == '+')
					left++;
			}
			for (int i = 0; i < left; i++)
				str[i] = '-';

			while (str[right] == '+')
				right--;
			
			for (int i = 0; i <= right; i++) {
				if (str[i] == '-')
					str[i] = '+';
				else
					str[i] = '-';
			}
			count++;
		}
		fprintf(fp2, "Case #%d: %d\n", i, count);
	}

	return 0;
}