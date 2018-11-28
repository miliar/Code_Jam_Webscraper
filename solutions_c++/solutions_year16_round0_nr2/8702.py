#include <bits/stdc++.h>
using namespace std;
#define ll long long

int t;

int lastmenos(const string &s){
	for(int i = s.size()-1; i >= 0; i--){
		if(s[i] == '-') return i;
	}
	return -1;
}

void flip(string &s){
	int last = lastmenos(s);
	for(int i = 0, j = last; i <= j; i++, j--){
		if(i != j){
			if(s[i] == '+') s[i] = '-';
			else if(s[i] == '-') s[i] = '+';

			if(s[j] == '-') s[j] = '+';
			else if(s[j] == '+') s[j] = '-';
		}
		else{
			if(s[i] == '+') s[i] = '-';
			else s[i] = '+';
		}
	}
}


bool worth(string &s){
	//if(s[0] == '-') return true;
	//return false;
	string aux;
    aux = s;
	
	flip(aux);

	if(lastmenos(aux) < lastmenos(s)){
		return true;
	}
	return false;
}

bool complete(const string &s){
	for(int i = 0; i < s.size(); i++){
		if(s[i] == '-') return false;
	}
	return true;
}

void flipmais(string &s){
	int i = 0;
	while(i < s.size() and s[i] == '+'){
		s[i] = '-';
	}
}

ll solve(string &s){
	ll cnt = 0;
	while(!complete(s)){
		//cout << "loopao" << endl;
		//cout << s << endl;
		if(worth(s)){
			flip(s);
		}
		else{
			flipmais(s);
		}
		cnt++;
	}
	return cnt;
}

int main(void){
	ios_base::sync_with_stdio(false);
	cin >> t;
	
	for(int k = 1; k <= t; k++){
		string s;
		cin >> s;

		ll res = solve(s);
		cout << "Case #" << k << ": " << res << '\n';
	}

	return 0;
}
