#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <cassert>


using namespace std;

typedef long long unsigned ll;


void dPause() {
	int j = 0;
	++j;
	return;
}


/*
string getName(const string &rawStr, int& n) {
	unsigned i;
	for(i = 0; i < rawStr.size(); ++i) {
		if(rawStr[i] != ' ')
			continue;
	}
	string ansStr = rawStr.substr(0, i);
//	string nStr = rawStr.substr(i, rawStr.size() - i);
	sscanf(rawStr.c_str(), "%d", &n);
	return ansStr;
}
*/

bool isCons(char c) {
	if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
		return false;
	else 
		return true;
}


int consNumber(const string &name, unsigned frstInd = 0) {
	int consN = 0;
	for(unsigned i = frstInd; i < name.size(); ++i) 
		if(isCons(name[i]))
			++consN;
	return consN;
}


bool hasNCons(const string &name, unsigned n, unsigned frstInd, unsigned lastInd) {
	unsigned curN = 0;
	for(unsigned i = frstInd; i <= lastInd; ++i) {
		if(!isCons(name[i])) {
			curN = 0;
			continue;
		}
		++curN;
		if(curN >= n)
			return true;
	}
	return false;
}


ll getNVal(const string &name, unsigned n) {
	ll ans = 0LL;
	for(unsigned startInd = 0; startInd < name.size(); ++startInd) {
		for(unsigned endInd = startInd; endInd < name.size(); ++endInd) {
			if(hasNCons(name, n, startInd, endInd))
				++ans;
		}
	}
	return ans;
}



/*
ll getNVal(const string &name, unsigned n, unsigned frstInd, bool haveLC) {
	if(frstInd >= name.size())
		return 0LL;
	// Not less then one letter
	if(n == 0)
		return ((ll) 1 << name.size()) - 1;


	int consN = consNumber(name, frstInd);
	// Not enough consonants (even for one n-substr)
	if(consN < n)
		return 0LL;

	// If have leading consonants then get rid of current leading vovels
	if(haveLC && !isCons(name[frstInd]))
		return getNVal(name, n, frstInd + 1, true);

	if(consN == n) {
		// Can't occure if have leading C
		int vovBefore = 0;
		for(unsigned i = frstInd; i < name.size(); ++i) {
			if(isCons(name[i]))
				break;
			++vovBefore;
		}

		int vovAfter = 0;
		for(unsigned i = name.size() - 1; i >= frstInd; --i) {
			if(isCons(name[i]))
				break;
			++vovAfter;
		}

		int vovExtra = vovBefore + vovAfter;
		ll ans = (ll) 1 << vovExtra;
		return ans;
	}


	if(!isCons(name[frstInd])) {
		if(!haveLC)
			return 2 * getNVal(name, n, frstInd + 1, true);
		else
			return getNVal(name, n, frstInd + 1, false);
	}
	
	// if use this consonant then have leading C, else the parameter remains the same
	return getNVal(name, n - 1, frstInd + 1, true) + getNVal(name, n, frstInd + 1, haveLC);
}
*/




void printAnswer(unsigned ti, ll ans) {
	cout << "Case #" << ti << ": " << ans << endl;
}



int main()
{
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("outA-small-attempt0.txt", "wt", stdout);
	
//	string readLine;

	// Number of tests
	unsigned T;
	cin >> T;
	
	for(unsigned ti = 1; ti <= T; ++ti) {
		cerr << ti << endl;
		string name;
		cin >> name;//getline(cin, readLine);
		unsigned n;
		cin >> n;

		//string name = getName(readLine, n);

		ll ans = getNVal(name, n);

		printAnswer(ti, ans);

//		dPause();
	}


	dPause();
	return 0;
}