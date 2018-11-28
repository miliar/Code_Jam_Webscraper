#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define SZ(v) ((int)((v).size()))

int T;
int N;
string strs[16][2];

bool is_ok(int index, int bitmap){
	bool first = false;
	bool second = false;
	for (int i=0; i<N; i++){
		if (i != index && (bitmap & (1 << i)) == 0){
			if (strs[index][0] == strs[i][0])
				first = true;
			if (strs[index][1] == strs[i][1])
				second = true;
		}
	}
	return (first && second);
}

int compute(){
	int maxi = 0;
	for (int bitmap=0; bitmap < (1 << N); bitmap++){
		/*for (int j=0; j<N; j++){
			if ((bitmap & (1 << j)) != 0){
				cout << strs[j][0] << " " << strs[j][1] << endl;
			}
		}*/
		int cnt = 0;
		for (int j=0; j<N; j++){
			if ((bitmap & (1 << j)) != 0 && is_ok(j, bitmap))
				cnt++;
		}
		//cout << cnt << endl;
		maxi = max(maxi, cnt);
	}
	return maxi;
}

int main(){
	cin >> T;
	for (int i=1; i<=T; i++){
		cin >> N;
		for (int j=0; j<N; j++){
			cin >> strs[j][0] >> strs[j][1];
		}
		cout << "Case #" << i << ": " << compute() << endl;
	}
}		

