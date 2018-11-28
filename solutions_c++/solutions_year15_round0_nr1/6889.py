#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i = 0; i < T; i++){
		int n;
		int final = 0;
		cin >> n;
		n++;
		int *shy = new int[n];
		string s;
		cin >> s;
		for(int j = 0; j < n; j++){
			shy[j] = s[j] - '0';
		}
		int total = shy[0];
		if(n > 0){
			for (int j = 1; j < n; j++){
					if(total < j){
						final += j - total;
						total += j - total;
					}
					total+= shy[j];
			}
		}
		cout << "Case #" << i+1 << ": " << final << endl;
	}
	return 0;
}