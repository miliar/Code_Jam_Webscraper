#include<bits/stdc++.h>
#define endl '\n'
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define ll long long
#define ld long double
using namespace std;

string s;
int len;

void g(int i){
// 	cout << "CALLED G " << i << endl;
	string temp = s;
// 	cout << "Before: " << s << endl;
	for(int k=i;k<len;++k)
		s[k] = temp[len-1+i-k]=='+'?'-':'+';
// 	cout << "After swap " << i << ": " << s << endl << endl;
}

void swapTopPlus(){
	int i=len-1;
	while(s[i] == '+')
		--i;
	g(i+1);
}

int f(int i){
// 	cout << "CALLED F " << i << endl;
	if(i >= 10)
		return 23;
	
	while(i<len && s[i] == '+')
		++i;
	if(i==len)
		return 0;
	
	if(i==len-1)
		return s[i]=='+'?0:1;
	
// 	cout << "BLAH " << s << endl;
	if(s[len-1] == '-'){
		g(i);
		return 1+f(i+1);
	}else{
		swapTopPlus();
		g(i);
		return 2+f(i+1);
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	int ncases, caseNumber = 1;
	cin >> ncases;
	while(ncases--){
		string in;
		cin >> in;
		s = string(in.rbegin(), in.rend());
		len = s.size();
		cout << "Case #" << caseNumber << ": " << f(0) << endl;
		caseNumber++;
	}
	return 0;
}