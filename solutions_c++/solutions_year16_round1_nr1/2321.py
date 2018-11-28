#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <cmath>
#include <set>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<char> vc;
typedef vector<vc> vvc;

int main(){
	int T, i, j, k;
	string temp;
	cin >> T;
	for(i = 0; i < T; i++){
		cin >> temp;
		deque <char> answer;
		vc letters(temp.begin(), temp.end());
		answer.push_back(letters[0]);
		for(j = 1; j < letters.size(); j++){
			char start = answer[0];
			if(start > letters[j]) answer.push_back(letters[j]);
			else answer.push_front(letters[j]);
		}
		cout << "Case #" << i + 1 << ": ";
		for(j = 0; j < answer.size(); j++){
			cout << answer[j];
		}
		cout << endl;
	}
}