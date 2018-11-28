#include <iostream>
#include <string>
using namespace std;

int doit(){
	int m; string s;
	cin >> m;
	cin >> s;
	int curr = 0;
	int ans = 0;
	for(int i = 0; i < m+1; i++){
		int val = static_cast<int>(s[i]) - static_cast<int>('0');
		if(curr + val == 0){
			ans ++; curr++;
		}
		curr += val;
		curr--;
	}
	return ans;
}

int main() {
	int c;
	cin >> c;
	for(int i = 1; i < c+1; i++){
		cout << "Case #"<< i << ": " << doit() << endl;
	}
	return 0;
}