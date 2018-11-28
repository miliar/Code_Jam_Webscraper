#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <list>

using namespace std;

bool is_palindromes(long long x) {
	if(x>=0 && x<10) {
		return true;
	}
	stringstream ss;
	ss << x;
	string s = ss.str();
	int b = 0;
	int e = s.length()-1;
	while(b<e) {
		if(s[b] != s[e]) {
			return false;
		}
		b++;
		e--;
	}
	return true;
}

bool is_square_palindromes(string x, string &out) {
	string square = string(x.length(),'0');
	for(int i=x.length()-1;i>=0;i--) {
		if(x[i]>'0') {
			string curr;
			int sum = 0;
			for(int j=x.length()-1;j>=0;j--) {
				sum += (x[j]-'0')*(x[i]-'0');
				curr = string(1,'0' + sum%10) + curr;
				sum = sum/10;
			}
			if(sum) {
				curr = string(1,'0' + sum%10) + curr;
			}
			curr += string(x.length()-1-i,'0');
			sum = 0;
			for(int j=0;j<square.length();j++) {
				sum += curr[curr.length()-1-j]-'0' + square[square.length()-1-j]-'0';
				curr[curr.length()-1-j] = '0' + sum%10;
				sum = sum/10;
			}
			if(sum) {
				sum += curr[0] - '0';
				curr[0] = '0' + sum%10;
				sum = sum/10;
			}
			if(sum){
				curr.insert(curr.begin(),'0'+sum);
			}
			square = curr;
		}
	}
	out = square;
	int b = 0;
	int e = square.length()-1;
	while(b<e) {
		if(square[b] != square[e]) {
			return false;
		}
		b++;
		e--;
	}
	return true;
}

vector<string> palindromes() {
	vector<string> table;
	int max_data = 30000;
	for(int i=0;i<max_data;i++) {
		int square = i*i;
		if(is_palindromes(i) && is_palindromes(square)) {
			stringstream ss;
			ss << square;
			table.push_back(ss.str());
		}
	}
	string out;
	vector<string> t;
	t.push_back("100001");
	t.push_back("110011");
	t.push_back("101101");
	t.push_back("111111");
	for(vector<string>::iterator it=t.begin();it!=t.end();it++) {
		is_square_palindromes(*it,out);
		table.push_back(out);
	}
	if(is_square_palindromes(string("200002"),out))
		table.push_back(out);

	for(int n=7;n<=50;n+=2) {
		vector<string> curr;
		for(int i=0;i<t.size();i++) {
			string st = t[i].substr(0,n/2) + "0" + 
				t[i].substr(n/2);
			curr.push_back(st);	
			st = t[i].substr(0,n/2) + "1" + 
				t[i].substr(n/2);
			curr.push_back(st);	
		}
		for(vector<string>::iterator it=curr.begin();it!=curr.end();it++) {
			if(is_square_palindromes(*it,out)) 
				table.push_back(out);
		}
		string st(n,'0');
		st[0] = '2';
		st[st.length()-1] = '2';
		if(is_square_palindromes(st,out)) 
			table.push_back(out);
		st[st.length()/2] = '1';
		if(is_square_palindromes(st,out)) 
			table.push_back(out);
		for(int i=0;i<t.size();i++) {
			string st = t[i].substr(0,n/2) + "2" + t[i].substr(n/2);
			string out;
			if(is_square_palindromes(st,out)) {
				table.push_back(out);	
			}
		}
		
		curr.clear();
		for(int i=0;i<t.size();i++) {
			string st = t[i].substr(0,n/2) + "00" + 
				t[i].substr(n/2);
			curr.push_back(st);	
			st = t[i].substr(0,n/2) + "11" + 
				t[i].substr(n/2);
			string out;
			if(is_square_palindromes(st,out)) {
				curr.push_back(st);	
			}
		}
		for(vector<string>::iterator it=curr.begin();it!=curr.end();it++) 
			if(is_square_palindromes(*it,out)) 
				table.push_back(out);
		st = string(n+1,'0');
		st[0] = '2';
		st[st.length()-1] = '2';
		if(is_square_palindromes(st,out)) 
			table.push_back(out);
			
		t = curr;
	}
	return table;
}

bool comp(string a, string b) {
	if(a.length() == b.length()) {
		for(int i=0;i<a.length();i++) {
			if(a[i]!=b[i]) {
				return a[i]<b[i];
			}
		}
	}
	return a.length() < b.length();
}

int main()
{
	vector<string> table = palindromes();
	sort(table.begin(),table.end(),comp);
	int N=0;
	cin >> N;
	for(int n=1;n<=N;n++) {
		string nx, ny;
		cin >> nx >> ny;
		int i = 0;
		int ix = 0;
		int iy = table.size();
		for(i=0;i<table.size();i++) {
			if(table[i] == nx || !comp(table[i],nx)) {
				ix = i;	
				break;
			}
		}
		for(i=table.size()-1;i>=0;i--) {
			if(table[i] == ny || comp(table[i],ny)) {
				iy = i;
				break;
			}	
		}
		int result = max(0, iy-ix+1);
		cout << "Case #" << n << ": " << result << endl;
	}
	return 0;
}
/* vim: set ts=4 sw=4 sts=4 tw=100 noet: */
