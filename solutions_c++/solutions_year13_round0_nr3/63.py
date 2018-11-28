#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cassert>

using namespace std;

string rev(string r){
	string res = r;
	reverse(res.begin(), res.end());
	return res;
}

string mul(string s){
	string res(2*s.size()-1, '0');
	for(int i=0;i<s.size();i++){
		for(int j=0;j<s.size();j++)
			res[i+j] += (s[i]-'0')*(s[j]-'0');
	}
	if(res == "121022001") cout << s << endl;
	return res;
}

bool isParindrome(long long t){
	int a[100];
	int size = 0;
	while(t) { a[size++] = t%10; t/=10; }
	for(int i=0;i<size-i-1;i++)
		if(a[i]!=a[size-i-1]) return false;
	return true;
}

bool isParindrome(string s){
	for(int i=0;i<s.size()-i-1;i++)
		if(s[i]!=s[s.size()-i-1]) return false;
	return true;
}

bool inRange(const string& A, const string& val, const string& B){
	if(val.size() < A.size() || (val.size() == A.size() && val < A)) return false;
	if(B.size() < val.size() || (B.size() == val.size() && B < val)) return false;
	return true;
}

int main(){
	int T; cin >> T;

	vector<string> vs;
	vs.push_back("1");
	vs.push_back("4");
	vs.push_back("9");
	for(int i=1;i<=50;i++){
		string s1(i, '0');
		string s2(i, '0');
		s1[0] = '1';
		s2[0] = '2';
		string r1 = rev(s1);
		string r2 = rev(s2);
		vs.push_back(mul(s1+r1));
		vs.push_back(mul(s1+"0"+r1));
		vs.push_back(mul(s1+"1"+r1));
		vs.push_back(mul(s1+"2"+r1));
		vs.push_back(mul(s2+r2));
		vs.push_back(mul(s2+"0"+r2));
		vs.push_back(mul(s2+"1"+r2));
		for(int j=1;j<i;j++){
			s1[j] = '1';
			r1[i-j-1] = '1';
			vs.push_back(mul(s1+r1));
			vs.push_back(mul(s1+"0"+r1));
			vs.push_back(mul(s1+"1"+r1));
			vs.push_back(mul(s1+"2"+r1));
			for(int k=j+1;k<i;k++){
				s1[k] = '1';
				r1[i-k-1] = '1';
				vs.push_back(mul(s1+r1));
				vs.push_back(mul(s1+"0"+r1));
				vs.push_back(mul(s1+"1"+r1));
				for(int l=k+1;l<i;l++){
					s1[l] = '1';
					r1[i-l-1] = '1';
					vs.push_back(mul(s1+r1));
					vs.push_back(mul(s1+"0"+r1));
					vs.push_back(mul(s1+"1"+r1));
					s1[l] = '0';
					r1[i-l-1] = '0';
				}
				s1[k] = '0';
				r1[i-k-1] = '0';
			}
			s1[j] = '0';
			r1[i-j-1] = '0';
		}
	}

	string A, B;
	for(int test=1;test<=T;test++){
		cin >> A >> B;
		printf("Case #%d: ", test);
		long long res = 0;
		for(int i=0;i<vs.size();i++)
			if(inRange(A, vs[i], B)) res++;
		cout << res << endl;
	}
}
