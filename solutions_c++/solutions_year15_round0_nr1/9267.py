#include <iostream>
#include <vector>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int tc=1; tc<=t ; tc++){
		int smax;
		cin >> smax;
		
		int res = 0;
		vector<int> vals(smax+1);
		int count = 0;
		
		for(int i=0; i<=smax; i++){
			char c;
			cin >> c;
			vals[i] = c - '0';
		}
		
		for(int i=0; i<=smax; i++){
			if(count+res < i){
				res += (i - count - res);
			}
			count += vals[i];
		}
		
		cout << "Case #" << tc << ": " << res << endl;
	}
	
	return 0;
}
