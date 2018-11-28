#include <iostream>
#include <cstring>

using namespace std;
int first[17], second[17], amt[5][5], nums[5][5];

int main(){
	ios_base::sync_with_stdio(false);
	
	int T, vAns1, vAns2, num;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		cout << "Case #" << caso << ": ";
		
		memset(amt,0,sizeof amt);
		
		cin >> vAns1;
		vAns1--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> num;
				first[num] = i;
			}
		}
		
		cin >> vAns2;
		vAns2--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> num;
				second[num] = i;
			}
		}
		for(int i = 1; i <= 16; i++) amt[first[i]][second[i]]++, nums[first[i]][second[i]] = i;
		
		if(amt[vAns1][vAns2] == 0) cout << "Volunteer cheated!\n";
		else if(amt[vAns1][vAns2] == 1) cout << nums[vAns1][vAns2] << '\n';
		else cout << "Bad magician!\n";
	}
}
