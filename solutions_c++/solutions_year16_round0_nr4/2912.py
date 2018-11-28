#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int k, c, s;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		cin >> k >> c >> s;
		cout << "Case #" << w << ": ";
		for (int i = 1; i <= s; i++)
			cout << i << " ";
		cout << "\n";
	}
	return	0;
}
