#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (){
	int t;
	cin >>t;
	for (int u = 0; u < t; u++){
		int n;
		cin >>n;
		vector <int> v (4,0);
		for (int i = 0; i < 4; i++){
			for (int k = 0; k < 4; k++){
				int m;
				cin >>m;
				if (i+1 == n ) v[k] = m; 
			}
		}
		cin >>n;
		int cont = 0;
		int val = -1;
		for (int i = 0; i < 4; i++){
			for (int k = 0; k < 4; k++){
				int m;
				cin >>m;
				if (i+1 == n ) {
					if (find(v.begin(),v.end(), m) != v.end()) {
						cont++;
						val = m;
					}
				} 
			}
		}
		cout <<"Case #"<<u+1<<": "; 
		if (cont == 0) cout <<"Volunteer cheated!"<<endl;
		else if (cont == 1) cout <<val<<endl;
		else  cout <<"Bad magician!"<<endl;
	}

}