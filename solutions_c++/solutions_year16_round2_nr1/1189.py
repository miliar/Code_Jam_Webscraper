#include<iostream>
#include<vector>
#include<string>

using namespace std;

string nn[10] = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
string s;
bool b;
int n, T, a[30];  
vector <int> v;

bool ok(int x) {
	int m = nn[x].size();
	for(int i=0; i<m; i++)
		if(!a[nn[x][i]-'a']) return false;
}

void solve(int x, int n) {
	if(!n) {
		b = true;
		for(int i=0; i<v.size(); i++) cout<<v[i];
		return;
	}
	for(int i=x; i<10 && !b; i++) 
		if(ok(i)) {
		    for(int j=0; j<nn[i].length(); j++) a[nn[i][j]-'a']--;
		    v.push_back(i);
			solve(i, n-nn[i].size());
			v.pop_back();
		    for(int j=0; j<nn[i].length(); j++) a[nn[i][j]-'a']++;
		}
}

int main(){
	cin>>T;
	for(int t=0; t<T; t++) {
		cin>>s;
		n = s.size();
		for(int i=0; i<26; i++) a[i]=0;
		for(int i=0; i<n; i++) a[s[i]-'A']++;
		cout<<"Case #"<<t+1<<": ";
		b = false;
		solve(0, n);
		cout<<endl;
	}
}