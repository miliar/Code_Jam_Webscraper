#include<bits/stdc++.h>
using namespace std;

string solve() {
	int N, P,R,S;
	cin >> N >> R >> P >> S;
	
	map<char, char> next;
	next['P'] = 'R';  
	next['R'] = 'S';  
	next['S'] = 'P';  
	string s = "P";
	for(int i=0; i<N; i++) {
		string tmp = s + s;
		for(int j=0; j<s.size(); j++) {
			tmp[2*j] = s[j];
			tmp[2*j+1] = next[s[j]];
		}
		s = tmp;
	}
//	cout << s << endl;
	int a=0, b=0, c=0 ;
	for(int i=0; i<s.size(); i++) {
		if(s[i]=='P') a++;
		else if(s[i]=='R') b++;
		else c++;
	}
//	cout << a << " " <<b << " " << c << endl;
	if(a==P && b==R && c==S) {
		
	} 
	else if(P==b && R == c && S == a){
		for(int i=0; i<s.size(); i++)
			s[i] = next[next[s[i]]];
		
	}
	else if(P==c && R==a && S==b) {
		for(int i=0; i<s.size(); i++)
			s[i] = next[s[i]];
	}
	else return "IMPOSSIBLE";
	
	int haba = 1;
	for(int i=0; i<N; i++, haba *= 2) {
		for(int j=0; j<(1<<N); j += haba * 2) {
			if(s.substr(j, haba) > s.substr(j+haba, haba)) {
				for(int k=0; k<haba; k++) {
					swap(s[j+k], s[j+k+haba]);
				}
				
			}
		}
		
	}
	return s;
	
	
}

int main() {
	int N;
	cin >> N;
	for(int i=0; i<N;i ++) {
		
		string ans = solve();
		cout << "Case #" << i+1 << ": " << ans << endl;
		
	}
	
	return 0;
	
}

