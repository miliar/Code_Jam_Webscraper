#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int n, a, b, c;
string ans;
bool found;
char win[200][200];

bool ok(string s){
	int z = 1;
	for (int i = 0; i < n; i++, z <<= 1)
		for (int j = 0; j < (1<<n); j += z<<1){
			if (s[j] == s[j + z])	return false;
			s[j] = win[s[j]][s[j + z]];
		}
	return true;
}

void gen(int cur = 0){
	if (cur == (1<<n)){
		if (ok(ans))
			found = 1;
		return;
	}

	if (b)
		ans[cur] = 'P', b--, gen(cur + 1), b++;	
	if (found)
		return;

	if (c)
		ans[cur] = 'R', c--, gen(cur + 1), c++;
	if (found)
		return;

	if (a)
		ans[cur] = 'S', a--, gen(cur + 1), a++;
}

int main(){
	win['S']['P'] = win['P']['S'] = 'S';
	win['P']['R'] = win['R']['P'] = 'P';
	win['R']['S'] = win['S']['R'] = 'R';
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int i = 1; i <= te; i++){
		cout << "Case #" << i << ": ";
		cin >> n >> c >> b >> a;
		ans.resize(1<<n);
		found = 0;
		gen();
		if (!found)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << "\n";
	}
	return 0;
}
