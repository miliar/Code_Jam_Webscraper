#include<bits/stdc++.h>
using namespace std;

int bum[10];
int main(){
	int tc, x;
	cin >> tc;
	for (int t = 1; t <= tc; t++){
		cin >> x;
		for (int i = 0; i <= 9; i++) bum[i] = 0;
		cout << "Case #" << t << ": ";
		if (x == 0) cout << "INSOMNIA" << endl;
		bool wow = false;
		int idx = 1;
		while (!wow && x != 0){
			wow = true;
			int tmp = x * idx;
		
			while (tmp > 0){
				bum[tmp % 10] = 1;
				tmp = tmp / 10;
			}
			for (int i = 0; i <= 9; i++){
				if (bum[i] == 0) wow = false;
			}
			idx++;
			//cout << x * idx << endl;;
		}
		if (x != 0) cout << x * ( idx-1 )  << endl;
	}
	return 0;
	
}
