#include<bits/stdc++.h>

using namespace std;

int main(){
	int T, N;
	cin >> T;
	set<int> digits;
	for(int i = 0; i < T; i++){
		int aux, j = 1;
		cin >> N;
		int M = N;
		if(N == 0){
			cout << "Case #"<<i+1<<": INSOMNIA"<<endl;
			continue;
		}
		while(digits.size() < 10){
			aux = N;
			while(aux > 0){
				digits.insert(aux % 10);
				aux /= 10;
			}
			N = M * j;
			j++;
		}
		cout << "Case #"<<i+1<<": "<<N-M<<endl;
		digits.clear();
	}
}