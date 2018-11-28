#include <iostream>
using namespace std;

int main(){

	int T;
	int maxS;
	char aud;
	int shylevel[1001];
	int friends;
	int comp;

	cin >> T;
	for (int i = 1; i <= T; i++){
		cin >> maxS;
		friends = 0;
		comp = 0;

		for (int j = 0; j <= maxS; j++){
			cin >> aud;
			shylevel[j] = aud - '0';
		}

		for (int j = 0; j < maxS; j++){
			comp += shylevel[j];
			if (comp <= j){
				friends++;
				comp++;
			}
		}


		cout << "Case #" << i << ": " << friends << endl;
		
	}
	return 0;
}