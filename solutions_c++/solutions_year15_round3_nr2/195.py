#include <bits/stdc++.h>
using namespace std;

bool mark[200][200];
int K,L,S;
int cnt[200],f[200][200];
double dp[200][200];
string key,target;

double go (int pos, int state){
	if (mark[pos][state])
		return dp[pos][state];
	if (pos == S)
		return 0.0;
	mark[pos][state] = true;
	double &ret = dp[pos][state];
	ret = 0.0;
	for (int i=0; i<26; i++){
		double p = cnt[i] / ((int)key.size() + 0.0);
		int new_state = f[state][i];
		if (new_state == (int)target.size())
			ret+= p * (1.0 + go(pos+1, new_state));
		else
			ret+= p * go(pos+1, new_state);
	}
	return ret;
}

void main2(){
	cin >> K >> L >> S;
	cin >> key >> target;
	memset(cnt, 0, sizeof cnt);
	for (int i=0; i<(int)key.size(); i++)
		cnt[key[i]-'A']++;
	for (int i=0; i<=(int)target.size(); i++){
		for (char ch = 'A'; ch <= 'Z'; ch++){
			string tmp = target.substr(0,i) + ch;
			f[i][ch-'A'] = 0;
			for (int len=min((int)tmp.size(),(int)target.size()); len>0; len--){
				if (target.substr(0,len) == tmp.substr((int)tmp.size()-len)){
					f[i][ch-'A'] = len;
					break;
				}
			}
		}
	}
	for (int i=0; i<(int)target.size(); i++) if (cnt[target[i]-'A'] == 0){
		cout << fixed << setprecision(10) << 0.0 << endl;
		return;
	}
	memset(mark, 0, sizeof mark);
	double ans = go(0,0);
	for (int i=1; i<=(int)target.size(); i++){
		if (target.substr(i) == target.substr(0,(int)target.size()-i)){
			ans = ((S < (int)target.size()) ? (0) : (1 + (S-(int)target.size())/i)) - ans;
			break;
		}
	}
	cout << fixed << setprecision(10) << ans << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
