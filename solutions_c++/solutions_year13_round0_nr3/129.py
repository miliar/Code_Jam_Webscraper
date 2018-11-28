#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>

using namespace std;

bool palsqr(string a, string &b){
	b = "";
	for(size_t i = 0; i < a.size()*2-1; ++i) {
		b += " ";
		b[i] = 0;
	}
	for(size_t i = 0; i < a.size(); ++i) {
		for(size_t j = 0; j < a.size(); ++j) {
			b[i+j] += (a[i] - '0') * (a[j] - '0');
		}
	}
	for(size_t i = 0; i < b.size(); ++i) {
		if (b[i] > 9) return false;
		b[i] += '0';
	}
	return true;
}

bool iszero(string s){
	for(size_t i = 0; i < s.size(); ++i) {
		if (s[i] != '0') return false;
	}
	return true;
}

struct stringcomp{
	bool operator ()(const string &a, const string &b) const {
		if (a.size() == b.size()) return a < b;
		return a.size() < b.size();
	}	
};

void compute(std::vector<string> &V, std::vector<string> &S){
	V.push_back("0");
	V.push_back("1");	
	V.push_back("2");
	V.push_back("3");
	V.push_back("00");		
	V.push_back("11");
	V.push_back("22");	
	S.push_back("1");
	S.push_back("4");	
	S.push_back("9");
	S.push_back("121");
	S.push_back("484");	
	
	for(size_t i = 0; i < V.size() && V.back().size() < 52; ++i) {
		string s = V[i], b = "";
		s = "0" + V[i] + "0";		
		// cout << V[i] << endl;
  		V.push_back(s);
		s = "1" + V[i] + "1";
		if (palsqr(s, b)) {S.push_back(b), V.push_back(s);}
		s = "2" + V[i] + "2";
		if (palsqr(s, b)) {S.push_back(b), V.push_back(s);}
	}
}


int main (int argc, char const *argv[]) {
	int tcase;
	char in[102];
	std::vector<string> V;
	std::vector<string> S;	
	cin >> tcase;
	compute(V, S);
	sort(S.begin(), S.end(), stringcomp());
	// cout << "done" << endl;
	for(size_t casen = 0; casen < tcase; ++casen) {
		string A, B;
		cin >> A >> B;
		// cout << A << " " << B << endl;		
		B[B.size() - 1]++;
		size_t toA = (std::lower_bound(S.begin(), S.end(), A, stringcomp()) - S.begin());
		size_t toB = (std::lower_bound(S.begin(), S.end(), B, stringcomp()) - S.begin());	
		// cout << toA << " " << toB << endl;
		cout << "Case #" << casen + 1 << ": ";
		cout << toB - toA << endl;
		
	}
	
	return 0;
}

/* SMALL / LARGE 1 INPUT */

bool palindrome(string a){
	for(size_t i = 0; i < a.size()/2; ++i) {
		if (a[i] != a[a.size()-1-i]) return false;
	}
	return true;
}

int main_small(){
	int tcase;
	char in[102];
	
	std::vector<long long> V;
	for(long long i = 1; i*i <= 100000000000000LL; ++i) {
		sprintf(in,"%lld", i);
		if (palindrome(in)){
			long long sqr = i*i;
			sprintf(in,"%lld", sqr);
			if (palindrome(in)){
				cout << i << " " << sqr << endl;	
				V.push_back(sqr);
			}			
		}
	}
	cin >> tcase;	
	
	for(size_t casen = 0; casen < tcase; ++casen) {
		long long A, B;
		cin >> A >> B;
		// cout << A << " " << B << endl;		
		size_t toA = (std::lower_bound(V.begin(), V.end(), A) - V.begin());
		size_t toB = (std::lower_bound(V.begin(), V.end(), B+1) - V.begin());	
		// cout << toA << " " << toB << endl;
		cout << "Case #" << casen + 1 << ": ";
		cout << toB - toA << endl;
		
	}
	

	return 0;
}