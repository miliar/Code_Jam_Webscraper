#include <iostream>
#include <string>

using namespace std;

void solve(int caseNumber){
	int smax;
	string s;
	cin >> smax;
	cin >> s;
	int standing = 0;
	int level = 0;
	int missing = 0;
	for (char i : s){
		int current = i - 48;
		if (standing < level){
			missing += level - standing;
			standing += level - standing;
		}
		standing += current;
		level++;
	}
	cout <<"Case #"<< caseNumber << ": "<< missing<<endl;
}

int main(){
	int testCases;
	cin >> testCases;

	for (int i = 1; i <= testCases; ++i){
		solve(i);
	}
	return 0;
}