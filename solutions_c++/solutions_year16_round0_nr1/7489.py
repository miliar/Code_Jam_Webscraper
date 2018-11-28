#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void main(){
	string STRING;
	ifstream infile;
	vector<int> store;
	infile.open("names.txt");
	getline(infile, STRING);	//trash
	while (!infile.eof()){
		getline(infile, STRING);
		if(!STRING.empty()){
			store.push_back(atoi(STRING.c_str()));
		}
		//cout << STRING << endl;
	}
	infile.close();
	ofstream outFile;
	outFile.open("output.txt");
	for (int i = 0; i < store.size(); i++) {
		printf("%i is ", store[i]);
		if (store[i] == 0) {
			outFile << "Case #" << i+1 << ": INSOMNIA\n";
			printf("INSOMNIA\n");
		}else{
			//printf("value: %i\n", store[i]);
			bool done = false;
			bool data[10] = { false };
			for (int j = 1; j < 100 && !done; j++) {
				int test = store[i] * j;
				//printf("test: %i\n", test);
				int aux = test;
				while (test > 0) {
					int digit = test % 10;
					//printf("%i ", digit);
					data[digit] = true;
					test /= 10;
				}
				//printf("\n");
				int k = 0;
				for (; k < 10 && data[k] == true; k++);
				//printf("k %i\n", k);
				if (k == 10) {
					done = true;
					outFile << "Case #" << i + 1 << ": " << aux << "\n";
					printf("done in j: %i\n", aux);
				}
			}
		}	
	}
	
	outFile.close();
	getchar();
}