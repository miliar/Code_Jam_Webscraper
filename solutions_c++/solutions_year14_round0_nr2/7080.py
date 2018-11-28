#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <sstream>
#include <bitset>
#include <numeric>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <stdlib.h> 
#include <ctype.h>

using namespace std;

int main()
{
	FILE *in;
	in = fopen("B-large.in", "r");
	
	FILE *out;
	out = fopen("out.txt","w");

	int test_cases;
	fscanf(in, "%d", &test_cases);
	for(int tc = 0; tc < test_cases; tc++) {
		long double C, F, X;
		fscanf(in, "%Lf %Lf %Lf", &C, &F, &X);

		long double time = 0;
		long double prod = 2;
		long double x1 = X / prod;

		long double x2;
		long double t;
		while(1) {
			x2 = X / (prod + F);
			t = C / prod;
			if(x2 + t > x1) {
				time += x1;
				break;
			}
			time += t;
			prod += F;
			x1 = x2;
		}
		
		fprintf(out, "Case #%d: %.7Lf\n", (tc + 1), time);
	}

	fclose(in);
	fclose(out);
	return 0;
}