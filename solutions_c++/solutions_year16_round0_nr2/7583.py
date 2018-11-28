#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void main(){
	string STRING;
	ifstream infile;
	vector<string> store;
	infile.open("names.txt");
	getline(infile, STRING);	//trash
	while (!infile.eof()){
		getline(infile, STRING);	
		if(!STRING.empty()){
			printf("%s\n", STRING.c_str());
			store.push_back(STRING);
		}
		//cout << STRING << endl;
	}
	infile.close();
	ofstream outFile;
	outFile.open("output.txt");
	for (int i = 0; i < store.size(); i++) {
		//printf("Working with: %s ", store[i].c_str());
		int aux = 0;
		bool done = false;
		while (!done) {
			int k = 0;
			for (; k < store[i].size() && store[i].c_str()[k] == '+'; k++);
			if (k == store[i].size()) {
				printf("A correct in %i moves\n", aux);
				outFile << "Case #" << i + 1 << ": " << aux << "\n";
				done = true;
			}
			else {
				k = 0;
				for (; k < store[i].size() && store[i].c_str()[k] == '-'; k++);
				if (k == store[i].size()) {
					printf("B correct in %i moves\n", aux + 1);
					outFile << "Case #" << i + 1 << ": " << aux + 1 << "\n";
					done = true;
				}
				else {
					if (store[i].size() == 1 && store[i].c_str()[0] == '-') {
						printf("C correct in 1 moves\n");
						outFile << "Case #" << i + 1 << ": 1" << "\n";
						done = true;
					}
					else {	
						for (int j = 1; j < store[i].size(); j++) {
							if (store[i][j] != store[i][j - 1]) {
								for (int l = 0; l <= j - 1; l++) {
									if (store[i][l] == '+') {
										store[i][l] = '-';
									}
									else {
										store[i][l] = '+';
									}
								}
								aux++;
								printf("SWAP: %s\n", store[i].c_str());
							}
						}
					}
				}
			}
		}
	}
	outFile.close();
	getchar();
}