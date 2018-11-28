#include <iostream>
#include <fstream>

using namespace std;

void problem(string s){
	int anss = 0;
	if(s.at(s.size() - 1) == '-')
		anss++;
	for(size_t i = 0; i < s.size() - 1; i++){
		if(s.at(i) != s.at(i + 1))
			anss++;
	}
	cout << anss << endl;
}

int main(){
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	int n;
	cin >> n;
	
	string s;
	for(int i = 0; i < n; i++){
		cin >> s;
		cout << "Case #" << i + 1 << ": ";
		problem(s);
	}
}