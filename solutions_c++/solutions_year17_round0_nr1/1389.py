#include <bits/stdc++.h>
using namespace std;

char flip(char ch){
    if(ch == '-')
	return '+';
    else
	return '-';
}

int solve(){
    string s;
    int k;
    cin >> s >> k;
    int lmt = (int)(s.size()) - k;
    int moves = 0;
    for(int i = 0; i <= lmt; i++){
	if(s[i] == '+') continue;
	moves += 1;
	for(int j = i; j < (i + k); j++)
	    s[j] = flip(s[j]);
    }
    int ok = 1;
    for(int i = 0; i < s.size(); i++)
	if(s[i] == '-')
	    ok = 0;
    if(!ok)
	cout << "IMPOSSIBLE";
    else
	cout << moves;
}

int main(){
    int cases;
    cin >> cases;
    for(int t = 1; t <= cases; t++){
	cout << "Case #" << t << ": ";
	solve();
	cout << "\n";
    }
    return 0;
}
