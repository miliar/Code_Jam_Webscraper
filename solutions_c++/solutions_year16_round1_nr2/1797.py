#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void solve(){
	int n;
	cin >> n;
	int x;
	vector<int> numeros (2501, 0);
	for (int i = 0; i < 2*n - 1; i++){
		for (int j = 0; j < n; j++){
			cin >> x;
			numeros[x] += 1;
		}
	}
	
	vector<int> res;
	for (int i = 0; i < numeros.size(); i++){
		if (numeros[i] % 2 != 0) res.push_back(i);
	}
	sort(res.begin(),res.end());
	
	for (int i = 0; i < res.size(); i++){
		cout << res[i] << " ";
	}
	cout << endl; 

}

int main(){
	
	//t: Test case
	int t;
	cin >> t;
	
	for (int i = 1; i<= t; i++){
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

