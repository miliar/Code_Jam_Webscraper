#include <iostream>
#include <algorithm>

using namespace std;

string makeShort(string line){
	string newone = "";
	newone += line[0];
	char last = line[0];
	
	for(int i = 1; i < line.length(); i++){
		if(line[i] != last){
			newone += line[i];
			last = line[i];
		}
	}
	return newone;
}

void solve(int T){
	string line; cin >> line;
	cout << "Case #" << T << ": ";
	
	line = makeShort(line);
	
	int moves = 0;
	for(int i = 0; i < line.length(); i++){
		if(line[i] == '-') moves++;
		else if(line[i] == '+' && i != line.length() - 1) moves++;
	}
	
	cout << moves << endl;
}

int main() {
	int T; cin >> T;
	
	for(int i = 1; i <= T; i++){
		solve(i);
	}
	
	return 0;
}
