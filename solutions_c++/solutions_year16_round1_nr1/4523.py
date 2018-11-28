#include <iostream>
#include <string>
#include <algorithm>

#define MAX_N 1000

using namespace std;

int T;
string N;
string R;

void input()
{
	cin >> T;
}

void dfs(string str) {
	if (str.length() == N.length()) {
		if (R < str) R = str;
		return;
	}
	dfs(str + N[str.length()]);
	dfs(N[str.length()] + str);
}

void process(){
	cin >> N;
	R = string(N.length(), 'A');
	dfs("");
}

void output(int n){
	cout << "Case #" << n << ": " << R << endl;
}

int main(){
	input();
	for (int i = 0; i < T; i++){
		process();
		output(i+1);
	}
	return 0;
}