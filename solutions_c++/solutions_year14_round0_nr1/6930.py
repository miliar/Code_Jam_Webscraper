#include "utilities.h"

int main(int argC, char **argV) {
	Initialize(argV[1]);

	int T;
	string line;
	GETLINE(line);
	T = atoi(line.c_str());
	int counter = 0;
	while (counter++ < T) {
		GETLINE(line);
		int choice1 = atoi(line.c_str());
		vector<string> cards1;
		for (int i = 0; i < 4; i++) {
			GETLINE(line);
			if (i == choice1 - 1)
				splitString(line, " ", cards1);
		}
		GETLINE(line);
		int choice2 = atoi(line.c_str());
		vector<string> cards2;
		for (int i = 0; i < 4; i++) {
			GETLINE(line);
			if (i == choice2 - 1)
				splitString(line, " ", cards2);
		}
		int matches = 0;
		int result = 0;
		for (vector<string>::iterator it = cards1.begin(); it < cards1.end(); it++) {
			for (vector<string>::iterator it2 = cards2.begin(); it2 < cards2.end(); it2++) {
				int c1 = atoi(it->c_str());
				int c2 = atoi(it2->c_str());
				if (c1 == c2) {
					matches++;
					result = c1;
				}
			}
		}

		fprintf(out, "Case #%d: ", counter);
		if (matches == 0)
			fprintf(out, "Volunteer cheated!\n");
		else if (matches == 1)
			fprintf(out, "%d\n", result);
		else
			fprintf(out, "Bad magician!\n");
	}
	fclose(in);
	fclose(out);
	return 0;
}