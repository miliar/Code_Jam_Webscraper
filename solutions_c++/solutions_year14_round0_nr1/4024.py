#include<iostream>
#include<vector>

using namespace std;

int main(){
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		int a[4];
		vector<int> sol;
		int na, nb;

		cin >> na;
		for(int j=1; j<=4; j++){
			for(int k=0; k<4; k++){
				int aux;
				cin >> aux;
				if (j == na)
					a[k] = aux;;
			}
		}

		cin >> nb;
		for(int j=1; j<=4; j++){
			for(int k=0; k<4; k++){
				int aux;
				cin >> aux;
				if (j == nb){
					for(int l=0; l<4; l++){
						if (aux == a[l])
							sol.push_back(aux);
					}
				}
			}
		}
		
		if (sol.size() == 0)
			cout << "Case #" << i << ": Volunteer cheated!\n";
		else if (sol.size() == 1)
			cout << "Case #" << i << ": " << sol[0] << "\n";
		else if (sol.size() > 1)
			cout << "Case #" << i << ": Bad magician!\n";

		sol.clear();
	}

	return 0;
}
