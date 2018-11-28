#include <iostream>

using namespace std;


int main(){

	int T;
	int Smax;

	int S[1000];


	cin >> T;
	for (int i = 0; i < T;i++){
		int N;
		int upnum = 0;
		int frie = 0;
		cin >> Smax;
		for (int j = 0; j <= Smax;j++){
			char tc;
			cin >> tc;
			//cout << tc << endl;
			if (tc == '0'){
				continue;
			}

			if (j <= upnum){
				upnum += (int)(tc-'0');
			}
			else{
				int sa = j-upnum;
				frie += sa;
				upnum = j + (int)(tc - '0');
				//cout << "fre " << j << endl;
			}
		}
		cout << "Case #" << i + 1 << ": " << frie << endl;

	}

	return 0;
}