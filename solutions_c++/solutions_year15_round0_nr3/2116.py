#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

pair<int, char> multSimple (char a, char b) {
	// a, b estan en {1, i, j, k}
	
	char mul[][4] = {{'1', 'i', 'j', 'k'}, 
					 {'i', '1', 'k' ,'j'},
					 {'j', 'k', '1', 'i'},
					 {'k', 'j', 'i', '1'}};
	int sign[][4] = {{1,  1,  1,  1}, 
					 {1, -1,  1, -1}, 
					 {1, -1, -1,  1}, 
					 {1,  1, -1, -1}};
	
	map<char, int> search;
	search['1'] = 0;
	search['i'] = 1;
	search['j'] = 2;
	search['k'] = 3;
	
	int a_int = search[a], b_int = search[b];
	return make_pair(sign[a_int][b_int], mul[a_int][b_int]);
}

pair<int, char> multSign (pair<int, char> aWithSign, pair<int, char> bWithSign) {
	int sign = aWithSign.first * bWithSign.first;
	char a = aWithSign.second;
	char b = bWithSign.second;
	
	pair<int, char> ret = multSimple(a, b);
	ret.first *= sign;
	return ret;
}

int main () {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	int t, l, x;
	string str, strRepeated;
	pair<int, char> multIzq[300000], multDer[300000];
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cin >> l >> x;
		cin >> str;
		
		strRepeated = "";
		for (int i = 0; i < x; i++)
			strRepeated += str;
		
		//cout << strRepeated << endl;
		int minI = l * x + 2, maxK = -1;	
		multIzq[0] = make_pair(1, '1');
		for (int i = 1; i <= l * x; i++) {
			multIzq[i] = multSign(multIzq[i-1], make_pair(1, strRepeated[i-1]));
			//cout << strRepeated[i-1] << endl;
			//cout << i << " " << multIzq[i].first << " " << multIzq[i].second << endl;
			if (multIzq[i] == make_pair(1, 'i') && minI == l * x + 2) {
				minI = i;
			}
		}
			
		multDer[l * x] = make_pair(1, '1');
		for (int i = l * x - 1; i >= 0; i--) {
			multDer[i] = multSign(make_pair(1, strRepeated[i]), multDer[i+1]);
			//cout << strRepeated[i] << endl;
			//cout << i << " " << multDer[i].first << " " << multDer[i].second << endl;
			if (multDer[i] == make_pair(1, 'k') && maxK == -1) {
				maxK = i;
			}
		}
		
		//cout << minI << " " << maxK;
		cout << "Case #" << tc << ": ";
		if (multIzq[l * x] == make_pair(-1, '1') && minI < maxK) {
			cout << "YES" << endl;
		}
		else {
			cout << "NO" << endl;
		}
	}
}
