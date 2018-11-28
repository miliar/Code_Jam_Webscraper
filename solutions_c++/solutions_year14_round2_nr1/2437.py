#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>

using namespace std;

typedef long long ll;
typedef long double ld;

FILE * fin, *fout;

string getUnique2(const string& s1, const string& s2) {
	size_t len1 = s1.size();
	size_t len2 = s2.size();
	string uq;
	size_t i, j;
	for(i=0, j = 0; i < len1 && j < len2; ) {
		if(s1[i] == s2[j]) {
			uq += s1[i];
			i++;
			j++;
		}
		else if(i == 0 || j == 0) {
			break;
		}
		else {
			if(s1[i-1] == s1[i])
				i++;
			else if(s2[j-1] == s2[j])
				j++;
			else {
				uq = "";
				return uq;
			}
		}
	}
	
	if(uq.size() > 0) {
		if(i < len1) {
			for(size_t k = i; k<len1; k++) {
				if(s1[k-1] != s1[i]) {
					uq = "";
					return uq;
				}
			}
		}
		if(j < len2) {
			for(size_t k = j; k<len2; k++) {
				if(s2[k-1] != s2[j]) {
					uq = "";
					return uq;
				}
			}
		}
	}
	
	return uq;
}

string getUnique(const string& s) {
	size_t len = s.size();
	string uq;
	char c = 0;
	for(size_t i=0; i<len; i++) {
		if(c != s[i]) {
			uq += s[i];
			c = s[i];
		}
	}
	return uq;
}

void solve(int problemIdx) {
	// read
	char buff[102];
	int n;
	vector<string> a;
	fscanf(fin, "%d", &n);
	a.resize(n);
	for(int i=0; i<n; i++) {
		fscanf(fin, "%s", buff);
		a[i] = buff;
	}
	
	// solve
	printf("solving %d\n", problemIdx);
	
	int m = 0;
	bool ok = false;
	if(n == 1) {
		ok = true;
	}
	else if(n == 2) {
		string u = getUnique2(a[0], a[1]);
		
		ok = u.size() > 0 || a[0] == a[1];
		m = abs(((int) a[0].size()) - (int) u.size()) + abs(((int) a[1].size()) - (int) u.size());
		
		printf("u : %s  m = %d\n", u.c_str(), m);
	}
	else {
		string u = getUnique2(a[0], a[1]);
		m = abs(((int) a[0].size()) - (int) u.size()) + abs(((int) a[1].size()) - (int) u.size());
		
		for(int i=2; i<n && u.size() > 0; i++) {
			string tmp = getUnique2(u, a[i]);
			if(tmp.size() < u.size()) {
				m += i * (u.size() - tmp.size());
				u = tmp;
			}
		}
		
		ok = u.size() > 0;
		
		printf("u : %s  m = %d\n", u.c_str(), m);
	}
	
	// output
	if(ok)
		fprintf(fout, "Case #%d: %d\n", problemIdx, m);
	else
		fprintf(fout, "Case #%d: Fegla Won\n", problemIdx);
}

int main(int argc, char** argv) {
	fin = fopen("input.txt", "rt");
	fout = fopen("output.txt", "wt");
	if(NULL == fin || NULL == fout) {
		printf("error opening files...\n");
		return -1;
	}
	
	int nrProblems;
	fscanf(fin, "%d", &nrProblems);
	for(int problemIdx = 1; problemIdx <= nrProblems; problemIdx++) {
		solve(problemIdx);
	}
		
	return 0;
}