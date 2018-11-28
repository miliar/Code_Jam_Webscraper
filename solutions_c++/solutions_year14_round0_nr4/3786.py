#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
	int tc;
	cin >> tc;
	for(int tcase=1; tcase<=tc; tcase++){
		int n;
		cin >> n;
		vector<double> vv1(n);
		vector<double> vv2(n);
		vector<double> vv1c(n);
		vector<double> vv2c(n);
		for(int i=0 ; i<n ; i++){
			cin >> vv1[i];
			vv1c[i] = vv1[i];
		}
		for(int i=0 ; i<n ; i++){
			cin >> vv2[i];
			vv2c[i] = vv2[i];
		}
		
		sort(vv1.begin(), vv1.end());
		sort(vv2.begin(), vv2.end());
		
		sort(vv1c.begin(), vv1c.end());
		sort(vv2c.begin(), vv2c.end());
		
		int dec = 0;
		int nor = n;
		
		int curr = 0;
		for(int i=0 ; i<n ; i++){
			if(vv1[i] > vv2[curr]){
				dec++;
				curr++;
				//vv2.erase(vv2.begin());
			}
		}
		
		for(int i=0 ; i<n ; i++){
			for(int j=0 ; j<vv2c.size() ; j++){
				if(vv2c[j]!=-1 && vv2c[j] > vv1c[i]){
					nor--;
					vv2c[j] = -1;
					//vv2c.erase(vv2c.begin()+j);
					break;
				}
			}
		}
		cout << "Case #" << tcase << ": " << dec << " " << nor << endl;
	}
	return 0;
}
