#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int war(vector<double> naomi, vector<double> ken){
	int result =0;
	vector<double>::iterator f = ken.begin();
	bool find = false;
	reverse(ken.begin(), ken.end());
	for (vector<double>::size_type s = 0; s < naomi.size(); s++){
		find = false;
		for (f = ken.begin(); f< ken.end();f++){
			if (*f > naomi[s]){
				find = true;
				break;
			}
		}
		if (find){
			ken.erase(f);
		}
		else{
			ken.erase(ken.begin());
			result++;
		}
	}
	return result;
}

int deceitfulWar(vector<double> naomi, vector<double> ken){
	int result = 0;
	vector<double>::size_type f = 0, b = ken.size()-1;
	for (vector<double>::size_type s = 0; s < naomi.size(); s++){
		if (naomi[f] > ken[s]){
			result++;
			f++;
		}
		else{
			b--;
		}
	}
	return result;
}

int main(){
	ifstream cin("D-large.in");
	ofstream cout("out.ou");

	int t, n;
	double temp;
	vector<double> naomi;
	vector<double> ken;
	cin >> t;
	for (int i = 1; i <= t; i++){
		cin >> n;
		naomi.clear();
		ken.clear();
		for (int j = 0; j < n; j++){
			cin >> temp;
			naomi.push_back(temp);
		}

		for (int j = 0; j < n; j++){
			cin >> temp;
			ken.push_back(temp);
		}

		
		sort(naomi.rbegin(), naomi.rend());
		sort(ken.rbegin(), ken.rend());

		cout << "Case #" << i << ": " << deceitfulWar(naomi, ken) << " " << war(naomi, ken) << endl;
	}

	return 0;
}