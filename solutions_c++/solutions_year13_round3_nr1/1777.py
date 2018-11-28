#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<sstream>
#include<queue>
#include<cctype>

using namespace std;

typedef long long ll;

bool isVowel(char c){
	return isalpha(c) && (c == 'a' || c == 'e' || c == 'u' || c == 'i' || c == 'o');
}

int solve(string s, int n){
	int len = (int)s.length();
	int ret = 0;
	for(int i = 0; i < len; i++){
		for(int j = i; j < len; j++){
			int cnt = 0;
			for(int k = i; k <= j; k++){
				if(cnt > 0 && cnt < n && isVowel(s[k])) cnt = 0;
				else if(!isVowel(s[k])) {
					cnt++;
					if(cnt >= n){
						ret++;
						break;
					}
				}
			}
		}
	}
	return ret;
}


int main(){
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);

	int T;
	scanf("%d", &T);
	cin.ignore();
	for(int t = 1; t <= T; t++){
		string s;
		int n;
		cin >> s >> n;
		cout << "Case #" << t << ": " << solve(s, n);
		if(t < T) cout << endl;
		cin.ignore();
	}
	return 0;
}
