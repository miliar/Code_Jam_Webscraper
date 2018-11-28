#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main() {
	FILE* in = fopen("problem.txt", "r");
	FILE* out = fopen("solve.txt", "w");

	int T;
	fscanf(in, "%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		char temp[1001];
		fscanf(in,"%s", temp);
		string s = "";
		s += temp[0];
		for (int i = 1; temp[i] != 0; i++) {
			if (s.at(0) > temp[i])
				s = s + temp[i];
			else
				s = temp[i]+s;
		}
		printf( "Case #%d: %s\n ", tc, s.c_str());
		fprintf(out, "Case #%d: %s\n", tc, s.c_str());
		
	}

}