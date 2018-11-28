#include <iostream>
#include <string>

using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++){
		int s;
		string z;	

		cin >> s >> z;

		int standups = 0, friends = 0;
		for (int i = 0; i <= s; i++){
			if (standups < i){
				friends += (i - standups);
				standups = i;
			}
				standups += z[i] - '0';
		}
		cout << "Case #" << t <<": " << friends << endl;
	}


	
}