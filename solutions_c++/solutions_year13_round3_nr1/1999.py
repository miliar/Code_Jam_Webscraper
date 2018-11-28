#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isConsonant(char c) {
	if(c >= 'a' && c <='z') {
		if(c == 'a' || c=='e' || c=='i' || c=='o' || c=='u')
			return false;
		return true;
	}
	cerr << "not a letter" << endl;
	return false;
}


long long solve(string name, long long n) {
	long long lastStartPoint = -1;
	long long lastIndex = name.length() - n;
	long long nVal = 0;
	for(long long i = 0; i <= lastIndex; i++)
	{
		bool allConsonants = true;
		for(long long j = 0; j < n; j++)
			if(!isConsonant(name[i + j])) {
				allConsonants = false;
				break;
			}
		if(allConsonants) {
			//cout << "index " << i << " worked, and lastStartingPoint = " << lastStartPoint << endl;
			nVal += (i - lastStartPoint)*(lastIndex - i + 1);
			lastStartPoint = i;
		}
	}
	return nVal;
}

int main() {
	//cout << "hello world" << endl;
	string s;
	int n;
	int T;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cin >> s >> n;
		cout << "Case #" << i+1 << ": " <<solve(s, n) << endl;
	}
	return 0;
}
