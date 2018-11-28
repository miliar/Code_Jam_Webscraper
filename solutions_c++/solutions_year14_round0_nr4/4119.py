#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){
	
	int T;
	cin >> T;
	for (int y = 1; y <= T; y++){
		int n;
		cin >> n;
		vector <double> naomi(n);
		vector <double> ken(n);
		for (int i = 0; i < n; i++){
				cin >> naomi[i];
			}
		for (int i = 0; i < n; i++){
				cin >> ken[i];
			}
		int war = 0, decite = 0;
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		
		int itr2 = n-1;
		for (int j = n-1; j >=0; j--){
			if (naomi[itr2] > ken[j]){
				decite++;
				itr2--;
				}
			}
			
		int itr = 0, i = 0;
		while (i < n && itr < n){
				if (naomi[i] < ken[itr]){
					itr++;
					i++;
					continue;
				}
				else{
					war++;
					itr++;
				}
			}
		
		
			cout << "Case #" << y << ": " << decite << " " << n - i << endl;
			
	}
}
