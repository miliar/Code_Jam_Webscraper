#include <iostream>
#include <string>
using namespace std;

string stack;

void read() {
	stack.clear();
	
	string s;
	char previous = '0';
	cin>>s;
	
	for(int i=0; i<s.length(); i++) {
		if(s[i] != previous) {
			stack += s[i];
			previous = s[i];
		}
	}
}

void swap(int pozition) {
	for(int i=0; i<=pozition; i++) {
		if(stack[i] == '-') stack[i]='+';
		else stack[i]='-';
	}
}

int sortOut(int pozition, int operationsSoFar) {
	if( pozition == 0) {
		if(stack[0] =='-') return operationsSoFar+1;
		return operationsSoFar;
	}
	if( stack[pozition] == '+') {
		stack.erase(pozition);
		return sortOut(pozition-1, operationsSoFar);
	}
	if( stack[0] == '-') {
		swap(pozition);
		stack.erase(pozition);
		return sortOut(pozition-1, operationsSoFar+1);
	}
	
	int i=0;
	while(stack[i]=='+') i++;
	swap(i-1);
	return sortOut(pozition, operationsSoFar+1);
}


int main() {
	
	int T;
	cin>>T;
	
	for(int j=1; j<=T; j++) {
		read();
		cout<<"Case #"<<j<<": "<<sortOut(stack.length()-1, 0 )<<endl;
	}
	
	return 0;
}

