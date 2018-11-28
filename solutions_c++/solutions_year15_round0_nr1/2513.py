#include <iostream>

using namespace std;

int answer(){
	int total = 0, friends = 0;
	int S;
	char n;
	cin >> S;
	for (int s = 0; s <= S; s++){
		cin >> n;
		n -= 48;
		if (n > 0){
			if (total < s){
				friends += s - total;
				total = s;
			}
			total += n;
		}
	}
	return friends;
}

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cout << "Case #" << i << ": " << answer() << "\n";
	}
	cout << endl;
}