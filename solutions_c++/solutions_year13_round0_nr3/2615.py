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

bool isPalindrome(string s){
	for(int i=0;i<s.length()/2;i++){
		if(s[i]!=s[s.length()-1-i])
			return false;
	}
	return true;
}

bool isPalindrome(long long n){
	return isPalindrome(to_string(n));
}

bool isPalindromeSquare(long long n){
	long long r = static_cast<long long>(floor(sqrt(n)+0.5));
	if(r*r!=n)
		return false;
	if(isPalindrome(r))
		return true;
	else
		return false;
}

void FairAndSquare(){
	// https://code.google.com/codejam/contest/2270488/dashboard#s=p2

	ifstream ifs ("..\\data\\FairAndSquare\\C-small-attempt0.in");
	FILE *fout = fopen("..\\data\\FairAndSquare\\C-small-attempt0.out", "w+");

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

		long long A = _atoi64(words[0].c_str());
		long long B = _atoi64(words[1].c_str());

		long long count = 0;

		for(long long n=A;n<=B;n++){
			if(		isPalindrome(n)
				&&	isPalindromeSquare(n)
				)
				count++;
		}

		fprintf(fout, "Case #%d: %lld\n",i+1, count);
	}

	ifs.close();
	std::fclose(fout);
}

void main() {
	time_t start, end;
	time(&start);

	FairAndSquare();

	time(&end);
	double duration = difftime(end, start);
	printf("time spent %.f seconds\n", duration);

	cin.get();
}