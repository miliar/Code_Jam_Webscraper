#include <iostream>
#include <string>

using namespace std;
int T,N;


int main(){
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> N;
		int p[N+10];
		int sum = 0;
		for(int j = 0; j < N; j ++){
			cin >> p[j];
			sum += p[j];
		}
		cout << "Case #" << i+1 << ": ";
		while(sum != 0){
			int pos = 0;
			while(pos != N){
				while(p[pos] != 0){
					p[pos]--;
					sum--;
					cout << char('A' + pos);
					for(int zz = 0; zz < N; zz ++){
						if(p[zz]*2 > sum){
							p[zz]--;
							sum--;
							cout << char('A' + zz);
							break;
						}
					}
					cout << " ";
				}
				pos++;
			}
		}
		cout << endl;
	}
}