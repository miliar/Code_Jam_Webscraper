#include <bits/stdc++.h>

using namespace std;

int vet[1000];

int main(){
	ios::sync_with_stdio(false);
	int t, cont = 1;
	cin >> t;
	while(t--){
		cout << "Case #" << cont++ << ": ";
		string str;
		cin >> str;
		for(int i = 0; i < str.size(); i++)
			vet[i] = (str[i] == '-') ? 0 : 1;
		
		int flips = 0;
		for(int i = str.size() - 1; i >= 0; i--){
			if((vet[i] + flips)%2)continue;
			flips++;
		}
		cout << flips << '\n';
	}
	return 0;
}