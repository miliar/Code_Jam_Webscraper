#include <iostream> 
#include <algorithm>
#include <vector>
using namespace std;

int main() {

	int t; 
	cin >> t;

	for (int i = 0; i < t; i++) {
		int n;
		vector<double> Nao, Ken;
		cin >> n;
		for (int j = 0; j < n; j++) {
			double temp;
			cin >> temp;
			Nao.push_back(temp);
		}
		for (int j = 0; j < n; j++) {
			double temp;
			cin >> temp;
			Ken.push_back(temp);
		}
		sort(Nao.begin(), Nao.end());
		sort(Ken.begin(), Ken.end());

		/*
		for (int j = 0; j < n; j++) 
			cout << Nao[j] << " ";
		cout << endl;
		for (int j = 0; j < n; j++) 
			cout << Ken[j] << " ";
		cout << endl;
		*/
		int k = 0; 
		int warresult = 0;
		for (int j = 0; j < n; j++) {
			//if (Nao[j] < Ken[k]) 
			//	k++;
			//else {

			while (k < n && Nao[j] > Ken[k])
				k++;
			//}
			
			if (k >= n) {
				warresult = n-j;
				break;
			}
			k++;
		}

		int newresult = 0;
		k = 0;
		for (int j = 0; j < n; j++) {
			if (Nao[j] > Ken[k]) {
				newresult++;
				k++;
			}
		}
		cout << "Case #" << i+1 << ": " << newresult << " " << warresult << endl;
	}

	return 0;
}