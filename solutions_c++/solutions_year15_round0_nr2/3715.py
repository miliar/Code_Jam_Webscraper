#include <bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int n;
		cin >>n;
		vector<int> v;
		for(int i = 0; i < n; i++){
			int aux;
			cin >> aux;
			v.push_back(aux);
		}
		
		int mn = 3000;		

		for(int i = 1; i <= 1000; i++){
			int cur = 0;
			for(int j = 0; j < n; j++){
				if(v[j] > i){
					cur += ceil((double)v[j]/i) - 1;
				}
			}

			mn = min(mn, cur+i);
		}

		cout << "Case #"<< t+1 << ": " << mn << endl;
	}
	return 0;
}
