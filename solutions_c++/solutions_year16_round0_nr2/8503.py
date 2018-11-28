#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (n); i++)
#define fornn(i, q, n) for (int i = (q); i < (n); i++)
#define times clock() * 1.0 / CLOCKS_PER_SEC

using namespace std;

typedef long long ll;

int main(){
	freopen("b.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int count;
	cin >> count;
forn(tim, count){
   	string s;
   	cin >> s;
   	vector<int> pos;
   	int ans = 0;
   	if (s[0] == '+') ans--;
    forn(i, (int)s.size() - 1){
    	if (s[i] == '+' && s[i + 1] != '+') pos.push_back(i);
    }
    if (s[(int)s.size() - 1] == '+') pos.push_back((int)s.size() - 1);
    ans += (int)pos.size() * 2;       
    forn(i, s.size()){
    	if (s[i] == '+') 
    		s[i] = '-';
    	else
       	    s[i] = '+';
    }
    int ans2 = 0;
    pos.resize(0);
    if (s[0] == '+') ans2--;
    forn(i, (int)s.size() - 1){
    	if (s[i] == '+' && s[i + 1] != '+') pos.push_back(i);
    }

    if (s[(int)s.size() - 1] == '+') pos.push_back((int)s.size() - 1);
    ans2 += (int)pos.size() * 2;       
    
    cout << "Case #" << tim + 1 << ": " << min(ans + 1, ans2) << endl;


}
    return 0;
}