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

void Bullseye(){
	// https://code.google.com/codejam/contest/2418487/dashboard#s=p0

	ifstream ifs ("..\\data\\Bullseye\\A-small-attempt0.in");
	FILE *fout = fopen("..\\data\\Bullseye\\A-small-attempt0.out", "w+");

	string line;
	getline(ifs,line);
	int T = atoi(line.c_str());

	for(int i=0;i<T;i++){

		getline(ifs,line);
		stringstream ss(line);
		vector<string> words;
		string word;
		while(getline(ss, word, ' ')) {
			words.push_back(word);
		}

		double r = _atoi64(words[0].c_str());
		double t = _atoi64(words[1].c_str());

		long long n = (sqrt(4*r*r-4*r+8*t+1)-2*r-3)/4;

		double s=(2*r+1)*(n+1)+2*n*(n+1);
		if (s>t)
			n--;
		
		fprintf(fout, "Case #%d: %lld\n",i+1, n+1);
	}

	ifs.close();
	std::fclose(fout);
}

void main() {
	time_t start, end;
	time(&start);

	Bullseye();

	time(&end);
	double duration = difftime(end, start);
	printf("time spent %.f seconds\n", duration);

	cin.get();
}