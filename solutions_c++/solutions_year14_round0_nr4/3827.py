#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int deceitful(vector<double> naomi, vector<double> ken){
	int points_naomi = 0, points_ken = 0;
	while (!naomi.empty()){
		if (naomi.back() > ken.back()){
			++points_naomi;
			naomi.erase(naomi.end() - 1);
			ken.erase(ken.end() - 1);
		}
		else {
			++points_ken;
			naomi.erase(naomi.begin());
			ken.erase(ken.end() - 1);
		}
	}
	return points_naomi;	
}

vector<double>::iterator find_first_greater(vector<double>& v, double value){
	for (vector<double>::iterator it = v.begin(); it != v.end(); ++it){
		if (*it > value)
			return it;
	}
}

int war(vector<double> naomi, vector<double> ken){
	int points_naomi = 0, points_ken = 0;
	while (!naomi.empty()){
		if (naomi.back() > ken.back()){
			++points_naomi;
			naomi.erase(naomi.end() - 1);
			ken.erase(ken.begin());
		}
		else {
			++points_ken;

			ken.erase(find_first_greater(ken, naomi.back()));
			naomi.erase(naomi.end() - 1);
		}
	}
	return points_naomi;	
}

int main(){
	int tests;
	cin >> tests;

	for (int i = 0; i < tests; ++i){
		vector<double> naomi, ken;
		int n;
		cin >> n;

		for (int j = 0; j < n; ++j){
			double temp;
			cin >> temp;
			naomi.push_back(temp);
		}

		for (int j = 0; j < n; ++j){
			double temp;
			cin >> temp;
			ken.push_back(temp);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		cout << "Case #" << i + 1 << ": " << deceitful(naomi, ken) << " " << war(naomi, ken) << endl;
	}
}