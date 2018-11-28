#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i=0;i<n;i++){
		long long a,b,k;
		cin >> a >> b >> k;
		int s=0;
		for(int ai=0;ai<a;ai++){
			for(int bi=0;bi<b;bi++){
				if((ai&bi)<k) s++;
			}
		}
		cout << "Case #" << i+1 << ": " << s;
		cout << '\n';
	}
	return 0;
}