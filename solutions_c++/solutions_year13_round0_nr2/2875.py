#include <stdio.h> // for cin/cout
#include <iostream> // for printf
#include <fstream> // for ifstream and ofstream
#include <math.h>
#include <ctime>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <stack>
#include <map>
#include <unordered_map>
#include <unordered_set>

using namespace std;

void Lawnmower(){
	// https://code.google.com/codejam/contest/2270488/dashboard#s=p1

	ifstream ifs ("..\\data\\Lawnmower\\B-large.in");
	FILE *fout = fopen("..\\data\\Lawnmower\\B-large.out", "w+");

	string line;
	getline(ifs,line);
	int T = atoi(line.c_str());

	for (int i=0;i<T;i++){	

		getline(ifs,line);
		stringstream ss(line);
		vector<string> words;
		string word;
		while(getline(ss, word, ' ')) {
			words.push_back(word);
		}

		int N = atoi(words[0].c_str());
		int M = atoi(words[1].c_str());

		vector<vector<int>> loan;
		for(int j=0;j<N;j++){
			vector<int> row;
			getline(ifs,line);
			ss = stringstream(line);
			while(getline(ss, word, ' ')) {
				row.push_back(atoi(word.c_str()));
			}
			loan.push_back(row);
		}

		string result = "YES";
		for(int j=0;j<N;j++){
			for(int k=0;k<M;k++){
				int height = loan[j][k];
				bool horizontalcut = true;
				for(int p=0;p<M;p++){
					if(loan[j][p]>height){
						horizontalcut = false;
						break;
					}
				}
				if(horizontalcut)
					continue;
				bool verticalcut = true;
				for(int p=0;p<N;p++){
					if(loan[p][k]>height){
						verticalcut = false;
						break;
					}
				}
				if(!horizontalcut&&!verticalcut){
					result = "NO";
					goto conflictfound;
				}
			}
		}

conflictfound:
		fprintf(fout, "Case #%d: %s\n",i+1, result.c_str());
	}

	ifs.close();
	std::fclose(fout);
}

void main() {
	time_t start, end;
	time(&start);

	Lawnmower();

	time(&end);
	double duration = difftime(end, start);
	printf("time spent %.f seconds\n", duration);

	cin.get();
}