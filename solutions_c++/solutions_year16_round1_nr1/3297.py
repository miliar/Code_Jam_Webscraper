#include <iostream>
#include <stdio.h>

using namespace std;


int main() {
	FILE *fpi;
	FILE *fpo;
	int N;
	string s = "";
	char tmp;
	string ts = "a";
	char charbuf[1010];
	fpi = fopen("input.txt", "r");
	fscanf(fpi, "%d", &N);
	fgets(charbuf, 1005, fpi);
	fpo = fopen("output.txt", "w");

	for (int i = 0; i < N;i++) {
		fprintf(fpo, "Case #%d: ",i+1);
		//Start
		fgets(charbuf, 1005, fpi);
		s = "";
		for (int j = 0; j < strlen(charbuf)-1; j++) {
			ts[0] = charbuf[j];
			if (s.length() == 0) {
				
				s = ts;
			}
			else {
				if (s[0] <= ts[0]) {
					s = ts + s;
				}
				else
					s = s + ts;
			}				
		}
		for (int j = 0; j < strlen(charbuf) - 1; j++)
			charbuf[j] = s[j];
		fprintf(fpo, "%s", charbuf);
		
		//End
		//fprintf(fpo, "\n");
	}
	fclose(fpi);
	fclose(fpo);
	return 0;
}

