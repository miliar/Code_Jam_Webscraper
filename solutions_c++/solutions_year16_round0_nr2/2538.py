#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

int count(string str){
	if (str.empty())
		return 0;
	if (str.back() == '+')
		return count(str.substr(0, str.length() - 1));
	if (str.front() == '+'){
		unsigned int ind = 0;
		while (ind < str.length() && str[ind] == '+'){
			str[ind] = '-';
		}
		return 1 + count(str);
	}
	string old = str;
	for (unsigned int ind = 0; ind < str.length(); ind++){
		if (old[ind] == '+')
			str[str.length() - 1 - ind] = '-';
		else
			str[str.length() - 1 - ind] = '+';
	}
	return 1 + count(str);
}

bool ok(string str){
	for (char e : str){
		if (e != '+')
			return false;
	}
	return true;
}

string turn(string str, unsigned int nb){
	string old = str;
	for (unsigned int i=0; i<nb; i++){
		if (old[i] == '-')
			str[nb - 1 - i] = '+';
		else
			str[nb - 1 - i] = '-';
	}
	return str;
}	

int bfs(string str){
	set<string> seen;
	seen.insert(str);
	queue<pair<string, int> > q;
	q.push(mp(str, 0));
	while (!ok(q.front().first)){
		string reversed = turn(q.front().first, q.front().first.length());
		if (seen.count(reversed) == 0){
			seen.insert(reversed);
			q.push(mp(reversed, q.front().second + 1));
		}
		unsigned int le = 0;
		for (; le < q.front().first.length() && q.front().first[le] == q.front().first[0]; le++){}
		string mod = turn(q.front().first, le);
		if (seen.count(mod) == 0){
			seen.insert(mod);
			q.push(mp(mod, q.front().second + 1));
		}
		q.pop();
	}
	return q.front().second;
}
	

int main(){
	int T;
	string str;
	cin >> T;
	for (int i=1; i<=T; i++){
		cin >> str;
		cout << "Case #" << i << ": " << bfs(str) << endl;
	}
}			

