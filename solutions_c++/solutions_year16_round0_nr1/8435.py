#include <bits/stdc++.h>

using namespace std;


int main(){
	ios::sync_with_stdio(false);
	int t;
	long long n;
	cin >> t;
	int caso = 1;
	while(t--){
		cout << "Case #" << caso++ << ": ";
		cin >> n;
		stringstream ss;
		int ans = 0;
		
		if(!n)cout << "INSOMNIA\n";
		else{
			char ch;
			int cont = 1;
			long long aux;
			while(ans != 1023){
				aux = n * cont++;
				//cout << ans << " " << aux << endl;
				ss << aux;
				while(ss >> ch)	ans |= (1 << (ch - '0'));	
				
				ss.clear();
			}
			cout << (n * (cont - 1)) << '\n';
		}
	}
	return 0;
}