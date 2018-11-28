#include <bits/stdc++.h>
using namespace std;
int main (){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int z;
	cin >> z;
	for (int i = 0; i < z; ++i){
		string a;
		cin >> a;
		int x = 0;
		int n = a.length();
		for (int j =0; j < n-1; ++j){
			if(a[j] != a[j+1])++x;
		}
		if (a[n-1] == '+')--x;
		cout <<"Case #" << i+1 << ": " << x+1 << '\n'; 
	}
}
