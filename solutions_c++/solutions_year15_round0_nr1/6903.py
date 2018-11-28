#include<iostream>
#include<cstdlib>

using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	for(int q=1; q<=t; q++){
		int d;
		cin >> d;
		int sum = 0;
		int res = 0;
		for(int i=0; i<=d; i++){
			char aux;
			cin >> aux;
			if (sum < i){
				res += i-sum;
				sum += i-sum;
			}
			sum += (int) (aux-'0');
		}
		cout << "Case #" << q << ": " << res << "\n";
	}
	return 0;
}
