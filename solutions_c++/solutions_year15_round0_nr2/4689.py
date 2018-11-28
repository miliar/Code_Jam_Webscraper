#include <iostream>
#include <cmath>
using namespace std;

#define N 1000

int main() {
	int n; cin >> n;

	for(int i=0;i<n;i++){
		int m; cin >> m;
		int list[N], listki[N];
		for(int j=0;j<N;j++){ list[j] = 0; listki[j] = 0; }
		
		int big=0;
		for(int j=0;j<m;j++){
			int tmp; cin >> tmp;
			list[tmp]++;
			listki[tmp]++;
			if(tmp > big) big=tmp;
		}
		//cout << "big=" << big << endl;

		int ans=big;
		int devided=0;

		int root = sqrt(big);
		if(root*root==big && root%2==1 && listki[big]==1 && big > 1){
			int big3=big, devided3=0;
			devided3 = root-1;
			listki[root] += root;
			listki[big3] = 0;
			while(big3--) if(listki[big3] > 0) break;
			while(1){
				//cout << "big=" << big3 << ", devided=" << devided3 << endl;
	
				if(ans > devided3+big3) ans = devided3+big3;
				if(big3 < 3) break;
	
				int half = (big3+1)/2;
				devided3 += listki[big3];
				
				if(big3%2==0) listki[half] += listki[big3]*2;
				else{
					listki[half] += listki[big3];
					listki[half-1] += listki[big3];
				}
				listki[big3] = 0;
				while(big3--) if(listki[big3] > 0) break;
			}
		}

		while(1){
			//cout << "big=" << big << ", devided=" << devided << endl;

			if(ans > devided+big) ans = devided+big;
	
			if(big < 3) break;

			int half = (big+1)/2;
			devided += list[big];
			
			if(big%2==0) list[half] += list[big]*2;
			else{
				list[half] += list[big];
				list[half-1] += list[big];
			}
			list[big] = 0;
			while(big--) if(list[big] > 0) break;
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}