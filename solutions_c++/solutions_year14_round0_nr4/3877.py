#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		int n;
		cin >> n;
		vector<double> naomi;
		vector<double> ken;
		for(int j=0; j<n; j++){
			double aux;
			cin >> aux;
			naomi.push_back(aux);
		}
		for(int j=0; j<n; j++){
			double aux;
			cin >> aux;
			ken.push_back(aux);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int war = 0;
		vector<int> usage(n, 0);
		for(int j=0; j<n; j++){
			for(int k=0; k<n; k++){
				if (ken[k] > naomi[j] && usage[k] == 0){
					usage[k] = 1;
					break;
				}
				if (k == n-1)
					war++;
			}
		}

		int decwar = 0;
		int count = 0;
		for(int j=0; j<n; j++){
			if (naomi[j] < ken[0])
				count++;
			else
				break;
		}
		vector<int> usage2(n, 0);
		for(int j=0; j<n-count; j++){
			for(int k=count; k<n; k++){
				if (naomi[k] > ken[j] && usage2[k] == 0){
					decwar++;
					usage2[k] = 1;
					break;
				}
			}
		}

		cout << "Case #" << i << ": " << decwar << " " << war << "\n";
	}
	return 0;
}
