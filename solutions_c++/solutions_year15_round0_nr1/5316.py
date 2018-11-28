#include<iostream>

using namespace std;

int main(void){

	int T;
	int all;
	int res;
	char* S;
	int snum;
	cin >> T;
	for(int t = 0;t<T;t++){

		all = 0;
		res = 0;
		cin >> snum;
		snum += 1;
		S = new char[snum];

		for(int i=0;i<snum;i++){
			cin >> S[i];
			
			if(S[i] != '0' && all < i){
				res += i - all;
				all += res;
			}

			//cout << S[i] << endl;
			//cout << "S[i]" << int(S[i] - '0') << endl;
			all += int(S[i] - '0');
			//cout << "all:" << all << endl;
			//cout << "res:" << res << endl;
		}
		
		cout << "Case #" << t+1 << ": " << res << endl; 

		delete [] S;
	}
	return 0;
}
