#include <cstdio>
 
using namespace std;

int main()
{
	int t;
	
	FILE * f1 = fopen("output.txt", "w");
	FILE * f2 = fopen("A-large.in", "r");
	
	fscanf(f2, "%d", &t);
	
	int n, i, j;
	
	for (i = 1; i <= t; ++i) {
		fscanf(f2, "%d", &n);
		
		char a[n + 2];
		
		fscanf(f2, "%s", a);
		int amount = 0, count = 0;
		
		j = 0;
		while (a[j] != '\0') {
			if (j <= count) {
				count += a[j] - '0';
			} else {
				amount += (j - count);
				count += a[j] - '0' + (j - count);
			}
			
			++j;
		}
		
		fprintf(f1, "Case #%d: %d\n", i, amount);
	}
	
	fclose(f1);
	fclose(f2);
	
	return 0;
}
