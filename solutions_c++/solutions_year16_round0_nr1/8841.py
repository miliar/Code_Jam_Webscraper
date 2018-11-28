#include <bits/stdc++.h>

using namespace std;

bool seen[10];
bool final[10];

bool checkEqual(){
	for(int i = 0 ; i < 10 ; i++){
		if(seen[i] != final[i]) return false;
	}
	return true;
}

int main(int argc, char **argv){
	std::ios::sync_with_stdio(false);

	int n, m, tests;
	int i, j;
	memset(final, true, 10*sizeof(bool));

	cin >> tests;

	for(j = 0 ; j < tests ; j++){
		cin >> n;
		if(n == 0) cout << "Case #" << j+1 << ": INSOMNIA" << endl;
		else{
			memset(seen, false, 10*sizeof(bool));
			for(i = 1 ; i < 1000 ; i++){
				m = n*i;
				while(m != 0){
					seen[m%10] = true;
					m /= 10;
				}
				if(checkEqual()) break;
			}
			if(i == 1000) cout << "Case #" << j+1 << ": INSOMNIA" << endl;
			else cout << "Case #" << j+1 << ": " << i*n << endl;
		}
	}

	return 0;
}