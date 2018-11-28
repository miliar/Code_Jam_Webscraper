#include <bits/stdc++.h>
using namespace std;

int t;
string pile;

int main(void){
	ios :: sync_with_stdio(false);
	cin >> t;
	int p = 0;
	while(t--){
		cin >> pile;
		bool group = false;
		int cont = 0;
		for(int i = 0; i < pile.size(); i++){
			if(i == 0 and pile[i] == '-'){
				cont++;
				group = true;
			}
			if(pile[i] == '+') group = false;
			else if(!group){
				group = true;
				cont += 2;
			}
		}
		cout << "Case #" << ++p << ": " << cont << endl;
	}
	return 0;
}
