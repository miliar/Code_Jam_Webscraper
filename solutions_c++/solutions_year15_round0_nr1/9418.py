/* Standing Ovation */
#include <iostream>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

static void printFriendsNeeded(char * str) {
	char sMaxTemp[5];
	int sMax = 0;
	int friendsNeeded = 0;
	int countStandingOvation = 0;

	char * space = strchr(str, ' ');
	strncpy(sMaxTemp, str, space - str);
	*(sMaxTemp + (space - str)) = 0;
	sMax = atoi(sMaxTemp);
	space++;

	for (int i = 0; i <= sMax; i++) {
		char c = *space;
		if ((countStandingOvation + friendsNeeded) < i) {
			friendsNeeded = friendsNeeded + (i - (countStandingOvation + friendsNeeded));
		}
		countStandingOvation = countStandingOvation + atoi(&c);
		space++;
	}

	cout << friendsNeeded << endl;
}

int main(int argc, char ** argv) {
	ifstream infile(argv[1]);
	string linebuff;

	if (infile.is_open()) {
		// Start
		if (!getline(infile, linebuff))
			return -1;
		int num_lines = atoi(linebuff.c_str());

		for (int i = 0; i < num_lines; i++) {
			if (!getline(infile, linebuff))
				return -1;
			//
			char * str = (char *)malloc((linebuff.length() + 1) * sizeof(char));
			strcpy(str, linebuff.c_str());
			cout << "Case #" << i + 1 << ": ";
			printFriendsNeeded(str);
			free(str);
			//
		}
		// End
		infile.close();
	}
	return 0;
}