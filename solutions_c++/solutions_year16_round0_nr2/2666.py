#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <unordered_map>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <stack>

using namespace std;

string flip(string pancakes, int i) {
	string topi = pancakes.substr(0, i);
	reverse(topi.begin(), topi.end());
	for (int j = 0; j < i; j++){
		if (topi[j] == '+')
			pancakes[j] = '-';
		else
			pancakes[j] = '+';
	}		
	return pancakes;
}

int f(string pancakes){
	int ret = 0;
	if (pancakes.size() == 0)
		return 0;

	int bottom = pancakes.size() - 1;
	while (bottom >= 0 && pancakes[bottom] == '+')
		bottom--;
	if (bottom < 0)
		return 0;

	int top = 0;
	if (pancakes[0] != '-') {
		while (pancakes[top] == '+')
			top++;
		pancakes = flip(pancakes,top);
		ret++;
	}

	return f(flip(pancakes, bottom+1).substr(0,bottom)) + ret + 1;
	
}

int main() {
	FILE * stream1, *stream2;
	freopen_s(&stream1, "Text.txt", "r", stdin);
	freopen_s(&stream2, "OUTPUT.txt", "w", stdout);
	int T,times;
	times = 1;
	cin >> T;
	while (T--) {		
		string pancakes;
		cin >> pancakes;
		cout << "Case #" << times << ": " << f(pancakes)<< endl;
		times++;
	}
	return 0;
}