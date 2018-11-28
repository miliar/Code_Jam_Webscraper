#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
#include <cstring>

using namespace std;

string flip(const string& stack, int index){
	string newStack(stack.begin(), stack.begin() + index + 1);
	for (int i = 0; i < index + 1; i++){
		newStack[i] = stack[index - i]=='+' ? '-' : '+';
	}
	return newStack;
}

char getOpposition(char ch){
	return ch == '+' ? '-' : '+';
}

int flipTo(char ch, string stack, int index){
	if (index == 0){
		if (stack[0] == ch)
			return 0;
		else
			return 1;
	}

	if (stack[index] == ch)
		return flipTo(ch, stack, index - 1);
	else{
		int oppositeAnswer = flipTo(getOpposition(ch), stack, index - 1) + 1;
		string newStack = flip(stack, index);

		int answer;
		if (newStack[index] != ch){
			answer = flipTo(getOpposition(ch), newStack, index - 1) + 2;
		}
		else{
			answer = flipTo(ch, newStack, index - 1) + 1;
		}
		return min(oppositeAnswer, answer);
	}
}

void main(){
	/*freopen("B-small-attempt3.in", "r", stdin);
	freopen("B-small-attempt3.out", "w", stdout);*/
	int testCase;
	cin >> testCase;
	for (int t = 1; t <= testCase; t++){
		string stack;
		cin >> stack;

		int plusCount = flipTo('+', stack, stack.length() - 1);
		int minusCount = 1 + flipTo('-', stack, stack.length() - 1);
		cout << "Case #" << t << ": " << min(plusCount, minusCount) << endl;
	}
}