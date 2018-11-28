#include <bits/stdc++.h>

using namespace std;

int main(){
	int a,b,c,n;
	cin >> n;
	for (int j=0; j< n;j++){
		cin >> a >> b >> c;
		cout << "Case #" << j+1 << ":";
		for (int i=0; i< c;i++){
			cout << " " << i+1;
		}
		cout << endl;
	}
}