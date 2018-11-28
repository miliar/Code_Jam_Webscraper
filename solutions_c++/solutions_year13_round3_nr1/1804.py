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
#include <set>
#include <unordered_map>
#include <unordered_set>

using namespace std;

void Consonants(){
	// https://code.google.com/codejam/contest/2437488/dashboard#s=p0

	ifstream ifs ("..\\data\\Consonants\\A-small-attempt0.in");
	FILE *fout = fopen("..\\data\\Consonants\\A-small-attempt0.out", "w+");

	string line;
	getline(ifs,line);
	int T = atoi(line.c_str());
	bool B[1000000];

	for(int i=0;i<T;i++){

		getline(ifs,line);
		stringstream ss(line);
		vector<string> words;
		string word;
		while(getline(ss, word, ' ')) {
			words.push_back(word);
		}
		string name = words[0];
		int L = name.length();

		for(int j=0;j<L;j++){
			if(name[j]=='a'||name[j]=='e'||name[j]=='i'||name[j]=='o'||name[j]=='u')
				B[j]=false;
			else
				B[j]=true;
		}
		int n = atoi(words[1].c_str());

		int nValue=0;
		int start=0;
		int end=n;

		while(start<=L-n){
			while(end<=L){
				bool consecutive=true;
				for(int j=0;j<n;j++){
					if(!B[end-1-j]){
						consecutive=false;
						break;
					}
				}
				if(consecutive){
					nValue+=L-end+1;
					break;
				}
				else
					end++;
			}
			start++;
			end=start+n;
		}
		fprintf(fout, "Case #%d: %d\n",i+1, nValue);
	}

	ifs.close();
	std::fclose(fout);
}

void main() {
	time_t start, end;
	time(&start);

	Consonants();

	time(&end);
	double duration = difftime(end, start);
	printf("time spent %.f seconds\n", duration);

	cin.get();
}