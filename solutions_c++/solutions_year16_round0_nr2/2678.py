#include <iostream>
#include <stdio.h>


using namespace std;

int cal(char* k) {
	int count = 0;
	if (k[0] == '+')
		count = 0;
	else
		count = 1;
	for (int i = 1; k[i] != '\n'; i++) {
		if (k[i - 1] == '+' && k[i] == '-')
			count += 2;
	}
	return count;
}

int main() {
	FILE *fpi;
	FILE *fpo;
	char k[105];
	int n;
	int i = 1;
	fpi = fopen("input.txt", "r");
	fscanf(fpi, "%d", &n);
	fgets(k, 104, fpi);
	fpo = fopen("output.txt", "w");
	while (n--) {
		fgets(k, 104, fpi);
		fprintf(fpo, "Case #%d: %d\n", i++, cal(k));
		
	}
	fclose(fpi);
	fclose(fpo);
	return 0;
}

