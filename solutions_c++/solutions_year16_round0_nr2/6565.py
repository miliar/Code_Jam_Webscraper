#include <iostream>
#include <string>
using namespace std;

int getFlipPoint(string inString);
bool isAllUp(string inString);
void flipSub(string &inString, int length);
char flipcake(char inChar);
int main() {
	int T,count;
	string S;
	cin >> T;
	for(int i=0;i<T;++i) {
		count=0;
		cin >> S;
		char Up=S[0];
		while(!isAllUp(S)) {
			int fPoint = getFlipPoint(S);
			flipSub(S,fPoint);
			count++;
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}
int getFlipPoint(string inString) {
	char first=inString[0];
	for(int i=1;i<inString.length();++i){
		if(first!=inString[i])
			return i;
	}
	return inString.length();
}
bool isAllUp(string inString) {
	bool allUp=true;
	for(int i=0;i<inString.length();++i) {
		if(inString[i]=='-')
			allUp=false;
	}
	return allUp;
}

void flipSub(string &inString, int length) {
	for(int i=0;i<length;++i) {
		inString[i]=flipcake(inString[i]);
	}
}

char flipcake(char inChar) {
	if(inChar=='+')
		return '-';
	return '+';
}