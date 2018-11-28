#include <iostream>
using namespace std;
int main(){
	int n;
	cin >> n;
	int k[n],c[n],s[n];
	for(int i=0;i<n;i++){
		cin >> k[i] >> c[i] >> s[i];
	}
	for(int j=0;j<n;j++){
		cout << "Case #" << j+1 << ": ";
		for(int k=1;k<=s[j];k++){
			cout << k << " ";
		}
		cout << endl;
	}
	return 0;
}