#include <bits/stdc++.h>
using namespace std;

int main(){
	int nbTests;
	cin >> nbTests;
	int shyness[1010];
	for(int testNb = 1; testNb <= nbTests; testNb++){
		int Smax;
		cin >> Smax;
		cin.ignore();
		for(int i = 0; i <= Smax; i++){
			char d;
			cin >> d;
			shyness[i] = d-'0';
		}
		
		int nbStanding = 0;
		int nbInvited = 0;
		for(int i = 0; i <= Smax; i++){
			while(nbStanding < i){
				nbInvited++;
				nbStanding++;
			}
			nbStanding+=shyness[i];
		}
		
		cout << "Case #" << testNb << ": " << nbInvited << endl;
	}
	return 0;
}