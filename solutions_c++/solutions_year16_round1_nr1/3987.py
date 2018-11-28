#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int test;
	FILE *fp = NULL;
	fp = fopen("A-large.in", "r");
	FILE *fp2 = NULL;
	fp2 = fopen("output.txt", "w");
	fscanf(fp, "%d", &test);

	char input[1005];
	for (int t = 1; t <= test; t++) {
		fscanf(fp, "%s", input);

		int len = strlen(input);
		string str = "";
		str += input[0];

		for (int i = 1; i < len; i++) {
			if (input[i] >= str[0])
				str = input[i] + str;
			else
				str += input[i];
		}
	
		fprintf(fp2, "Case #%d: ", t);
		for (int i = 0; i < len; i++)
			fprintf(fp2, "%c", str[i]);
		fprintf(fp2, "\n");
	}

	return 0;
}