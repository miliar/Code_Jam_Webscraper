#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int K[200000];

int main(){
	ios_base::sync_with_stdio(false);
	int z;
	cin >> z;
	
	for(int l = 1; l <= z; l++){
		string A;
		cin >> A;
		for(int p = 'A'; p <= 'Z'; p++)
			K[p] = 0;
		vector <int> OUT;
		for(int i = 0; i < (int)A.size(); i++)
			K[(int)A[i]]++;
			
		int ile = A.size();
		
		while(ile > 0){
			while(K['X'] > 0){
				OUT.push_back(6);
				K['S']--;
				K['I']--;
				K['X']--;
				ile = ile - 3;
			}
			while(K['Z'] > 0){
				OUT.push_back(0);
				K['Z']--;
				K['E']--;
				K['R']--;
				K['O']--;
				ile = ile - 4;
			}
			while(K['S'] > 0){
				OUT.push_back(7);
				K['S']--;
				K['E']--;
				K['V']--;
				K['E']--;
				K['N']--;
				ile = ile - 5;
			}
			while(K['G'] > 0){
				K['E']--;K['I']--;K['G']--;K['H']--;K['T']--;
				ile = ile - 5;
				OUT.push_back(8);
			}
			while(K['V'] > 0){
				K['F']--;K['I']--;K['V']--;K['E']--;
				ile = ile -4;
				OUT.push_back(5);
			}
			while(K['F'] > 0){
				K['F']--;K['O']--;K['U']--;K['R']--;
				ile = ile -4;
				OUT.push_back(4);
			}
			while(K['R'] > 0){
				K['T']--;
				K['H']--;
				K['R']--;
				K['E']--;
				K['E']--;
				ile = ile - 5;
				OUT.push_back(3);
			}
			while(K['I'] > 0){
				K['N']--;
				K['I']--;
				K['N']--;
				K['E']--;
				ile = ile - 4;
				OUT.push_back(9);
			}
			while(K['W']>0){
				K['T']--;
				K['W']--;
				K['O']--;ile=ile-3;OUT.push_back(2);
			}
			while(K['N']>0){
				K['O']--;
				K['N']--;
				K['E']--;
				ile = ile - 3;
				OUT.push_back(1);
			}
		}
		sort(OUT.begin(), OUT.end());
		cout << "Case #" << l << ": ";
		for(int i = 0; i < OUT.size(); i++)
			cout << OUT[i];
		cout << endl;
	}
}
