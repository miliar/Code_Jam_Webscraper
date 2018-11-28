#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;
int check[1111], d[1111];

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out","w",stdout);
	int T, n;
	cin >> T;
	for (int z=1; z<= T; z++){
		cin >> n;
		int h, k, res;
		h = 0;
		v.clear();
		for (int i=1; i<= n; i++){
			cin >> k;
			v.push_back(k);
			h = max(h, k);
		}
	
		res = h;
		sort(v.begin(), v.end());
		for (int j=1; j<= h; j++)
			d[j] = 0;
		for (int j=0; j< n; j++)
			d[v[j]]++;
		for (int j=1; j <= h; j++){
			int carry =0;
			for (int k=1; k <= h; k++)
				check[k] = d[k];
			for (int k=n-1; k >= 0; k--){
				if ((v[k] > j) && (check[v[k]] != 0)){
					if (v[k] % j == 0)
						carry += (( v[k] / j) - 1) * check[v[k]];
					else{
						carry += ( v[k] / j) * check[v[k]];
					}
					check[v[k]]=0;
				}
			}
			res = min(res, carry + j);
		}
		cout << "Case #" << z << ": " << res << endl;
	}
}
