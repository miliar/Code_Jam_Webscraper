#include <iostream>
using namespace std;

int main(){
	int T;
	cin >> T;
	
	for(int z = 1; z <= T; z++){
		string S;
		cin >> S;
		
		int res = 0;
		if(S[0] == '-')
			res++;
		
		for(int i = 0; i < (int)S.size() - 1; i++){
			if(S[i] == '+' && S[i + 1] == '-')
				res = res + 2;
		}
		
		cout << "Case #" << z << ": " << res << endl;
	}
	return 0;
}
