#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

#define FILE
#define MAX 101

using namespace std;

string llintToString(long long int num){
	string str;
	stringstream ss;
	ss << num;
	ss >> str;
	return str;
}

bool isPalindromes(string str)
{
	int size = (int)str.size();
	int left=0;
	int right=size-1;
	for (int i=0;i<size;++i){
		if (str[left] != str[right]) {
			return false;
		}
		++left;
		--right;
	}
	return true;
}

int solve(long long int start,long long int end)
{
	int count = 0;
	long long int n = 0;
	while ((n*n) < start) {
		++n;
	}
	long long int square = n * n;
	while (square <= end) {
		if (isPalindromes(llintToString(n))){
			if (isPalindromes(llintToString(square))) {
				++count;
			}
		}
		++n;
		square = n * n;
	}
	return count;
}

int main()
{
	int num;
	
#ifdef FILE
	ifstream ifs( "/Users/iseki/Downloads/C-small-attempt0.in" );
	ifs >> num;
#endif
#ifndef FILE
	cin >> num;
#endif
	ofstream ofs("/Users/iseki/Downloads/ans.dat");
	long long int start,end;
	for (int i=0; i<num; ++i) {
#ifndef FILE
		cin >> start;
		cin >> end;
#endif
#ifdef FILE
		ifs >> start;
		ifs >> end;
#endif
		
		int result = solve(start, end);
		
		cout << "Case #" << i+1 << ": " ;
		ofs << "Case #" << i+1 << ": " ;
		cout << result << endl;
		ofs << result << endl;
		
	}
	
	return 0;
}