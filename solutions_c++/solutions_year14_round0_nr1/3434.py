#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int cards[5];

int main(){
	int T, a1, a2;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cin >> a1;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++){
				int card; cin >> card;
				if(i == a1)
					cards[j] = card;
			}
		cin >> a2;
		int good = 0, C = 0;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++){
				int card; cin >> card;
				if(i == a2){
					for(int k = 1; k <= 4; k++)
						if(cards[k] == card){
							good++;
							C = card;
						}
				}
			}
		cout << "Case #" << t << ": ";
		if(!good) cout << "Volunteer cheated!\n";
		else if(good > 1) cout << "Bad magician!\n";
		else cout << C << endl;
	}
	return 0;
}