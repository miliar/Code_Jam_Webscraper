#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int min(int a, int b) {return (a<b)?a:b;}
int max(int a, int b) {return (a>b)?a:b;}

using namespace std;

unsigned int testNum;
vector<unsigned> shyLevels;

int main(int argc, char **argv) {
	unsigned int i;
	ifstream ifile("A-large.in");
	FILE *ofile = fopen("out.txt", "w");
	ifile >> testNum;
	for (i = 0; i < testNum; i++) {
		shyLevels = vector<unsigned>();
		unsigned maxShyLevel;
		char shyChar;
		ifile >> maxShyLevel;
		for (unsigned j = 0; j <= maxShyLevel; j++) {
			ifile >> shyChar;
			shyLevels.push_back(shyChar-'0');
		}
		/*for (unsigned j = 0; j < shyLevels.size(); j++) cout << shyLevels[j] << " ";
		cout  << endl;*/
		unsigned standing = 0, friends = 0;;
		for (unsigned j = 0; j < shyLevels.size(); j++) {
			if (standing < j) {
				friends += j-standing;
				standing = j;
			}
			standing += shyLevels[j];
		}
		fprintf(ofile, "Case #%d: %d\n", i+1, friends);
	}
	ifile.close();
	fclose(ofile);
	return 0;
}
