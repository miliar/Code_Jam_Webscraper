#include <iostream>
#include <vector>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=0; i<t; ++i){
		long long n, m=0;
		vector<int> cifre, a(10, 0);
		cin >> n;
		if(n==0){
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		while(cifre.size()<10){
			m+=n;
			//cout << c << ":  ";
			//for(int j=0; j<10; ++j) cout << a[j] << ' ';
			//cout << endl;
			int x=m;
			while(x!=0){
				int y=x%10;
				a[y]++;
				if(a[y]==1) cifre.push_back(y);
				x/=10;
			}
		}
		cout << "Case #" << i+1 << ": " << m << endl;
	}
	return 0;
}