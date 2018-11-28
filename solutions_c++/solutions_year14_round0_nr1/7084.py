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
	in = fopen("A-small-attempt0.in", "r");
	
	FILE *out;
	out = fopen("out.txt","w");

	int test_cases;
	fscanf(in,"%d", &test_cases);
	for(int tc = 0; tc < test_cases; tc++) {
		int answer1, answer2;
		fscanf(in,"%d", &answer1);
		int numbers[17] = {0};
		int n1, n2, n3, n4;
		for(int i = 0; i < 4; i++) {
			fscanf(in,"%d %d %d %d", &n1, &n2, &n3, &n4);
			if(i == (answer1 - 1)) {
				numbers[n1]++; numbers[n2]++; numbers[n3]++; numbers[n4]++;
			}
		}

		int count = 0;
		int ans;
		fscanf(in,"%d", &answer2);

		for(int i = 0; i < 4; i++) {
			fscanf(in,"%d %d %d %d", &n1, &n2, &n3, &n4);
			if(i == (answer2 - 1)) {
				if(numbers[n1] == 1) {
					count++;
					ans = n1;
				}
				if(numbers[n2] == 1) {
					count++;
					ans = n2;
				}
				if(numbers[n3] == 1) {
					count++;
					ans = n3;
				}
				if(numbers[n4] == 1) {
					count++;
					ans = n4;
				}
			}
		}
		
		fprintf(out, "Case #%d: ", (tc + 1));
		if(count == 1)
			fprintf(out, "%d\n", ans);
		else if(count == 0)
			fprintf(out, "Volunteer cheated!\n");
		else
			fprintf(out, "Bad magician!\n");
	}

	fclose(in);
	fclose(out);
	return 0;
}