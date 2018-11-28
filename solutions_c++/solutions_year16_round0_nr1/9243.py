#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ull;
int main(){

	ull T,n,c;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		cin >> n;
		if(n == 0){
			cout << "INSOMNIA" << "\n";
			continue;
		}
		c = n;
		ull ten = 10;
		vector<int> v(10,0);
		while(true){
			ull k = c;
			while(k != 0){
				v[k%ten]=1;
				k/=10;
			}
			bool a = true;
			for(int i=0;i<(int)v.size();i++){
				if(v[i]==0){
					a = false;
					break;
				}
			}
			if(a){
				cout << c << "\n";
				break;
			}
			c += n;
		}
	}
	return 0;
}