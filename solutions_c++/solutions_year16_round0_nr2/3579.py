#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

string s;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		cin >> s;
		cout << "Case #" << w << ": ";
		int ret = 0, n = s.size();
		for (int i = 0; i < n; ){
			int j = i;
			while (j < n && s[i] == s[j])	j++;
			ret++;
			i = j;
		}
		if (s[n - 1] != '-')	ret--;
		cout << ret << "\n";
	}
	return	0;
}
