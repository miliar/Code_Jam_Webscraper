#include <iostream>
#include <vector>
#include <set>

using namespace std;

int inversions(char* s){
	int i = 1;
	char cur = s[0];
	int count = 0;
	while(s[i] != '\0'){
		if(s[i] != cur)
			count++;
		cur = s[i];
		i++;	
	}
	return count;
}

int main() {
	int T;
	cin >> T;
	char S[101];
	bool topUp;
	for (int i = 1; i <= T; i++) {
		cin >> S;
		topUp = S[0] == '+';
		
		cout << "Case #" << i << ": ";
		int count = inversions(S);
		if(count % 2 == 1 && topUp || count % 2 == 0 && !topUp)
			count++;
		cout<< count<<endl;

	}
}
