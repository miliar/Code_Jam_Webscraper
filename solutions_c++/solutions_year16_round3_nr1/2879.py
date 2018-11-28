#include<iostream>
#include<vector>
#include<algorithm>
#define ALL(V) (V).begin(),(V).end()
using namespace std;
int T, N;
struct Z{
	int i;
	char c;
	bool operator<(const Z& z)const {
		return this->i > z.i;
	}
	Z(int a, char c) {
		this->i = a;
		this->c = c;
	}
	Z() {}
};
vector<Z > V;
int main() {
	cin >> T;
	for (int i = 1; i <= T; i++){
		cout << "Case #" << i << ": ";
		cin >> N;
		V.clear();
		for (int j = 0; j < N; j++){
			int in;
			cin >> in;
			V.push_back(Z(in, j + 'A'));
		}
		sort(ALL(V));
		///
		if (V[0].i != V[1].i){
			int k = V[0].i - V[1].i;
			V[0].i -= k;
			while (k--){
				cout << V[0].c;
			}
			cout << ' ';
		}
		for (int k = 2; k < V.size(); k++){
			int m = V[k].i;
			while (m!=0){
				if (m % 2 == 0){
					m -= 2;
					cout << V[k].c << V[k].c;
				}
				else{
					m--;
					cout << V[k].c;
				}
				cout << ' ';
			}
		}
		int m = V[0].i;
		while (m != 0){
			
			m--;
			cout << V[0].c << V[1].c << ' ';
			
		}
		///
		cout << endl;
	}
	return 0;
}