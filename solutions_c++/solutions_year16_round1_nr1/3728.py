#include<bits/stdc++.h>
using namespace std;
int main() {
	int T, i, j, k, len, t;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	char s[1000];
	cin >> T;
	t = 1;
	while(t <= T) {
		vector<char> v;
		cin >> s;
		len = strlen(s);
		j = 1;
		v.push_back(s[0]);
		while(j < len) {
			if(s[j] > v[0])
				v.insert(v.begin(), s[j]);
			else if(s[j] <= v[j-1])
				v.push_back(s[j]);
			else {
				k = 0;
				while(s[j] == v[k] && k < j)
					k++;
				if(v[k] > s[j])
					v.push_back(s[j]);
				else
					v.insert(v.begin(), s[j]);
			}
			j++;
		} 
		

		cout << "Case #" << t << ": ";
		for(i = 0; i < len; i++)
			cout << v[i];
			
		cout << endl;
		t++;		
	}
	return 0;
}
