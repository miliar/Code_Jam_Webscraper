#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define F2(i,a,b) for(int i=a;i<=b;i++)
#define F3(i,a,b) for(int i=a;i>=b;i--)
#define pb push_back

void d(char c, string &s) {
	size_t found = s.find(c);
	s[found] = 'a';
}

bool fi(char c, string &s) {
	size_t found = s.find(c);
	if (found!=std::string::npos)
		return true;
	else return false;
}

int main() {
	int t,T;
	cin >> T;
	F0(t,T) {
		string s;
		cin >> s;
		vector<int> A;
		{
			while(fi('Z',s)) {
				d('Z',s);
				d('E',s);
				d('R',s);
				d('O',s);
				A.pb(0);
			}
			while(fi('G',s)) {
				d('E',s);
				d('I',s);
				d('G',s);
				d('H',s);
				d('T',s);
				A.pb(8);
			}
			while(fi('W',s)) {
				d('T',s);
				d('W',s);
				d('O',s);
				A.pb(2);
			}
			while(fi('X',s)) {
				d('S',s);
				d('I',s);
				d('X',s);
				A.pb(6);
			}
			while(fi('U',s)) {
				d('F',s);
				d('O',s);
				d('U',s);
				d('R',s);
				A.pb(4);
			}
			while(fi('O',s)) {
				d('O',s);
				d('N',s);
				d('E',s);
				A.pb(1);
			}
			while(fi('H',s)) {
				d('T',s);
				d('H',s);
				d('R',s);
				d('E',s);
				d('E',s);
				A.pb(3);
			}
			while(fi('F',s)) {
				d('F',s);
				d('I',s);
				d('V',s);
				d('E',s);
				A.pb(5);
			}
			while(fi('V',s)) {
				d('S',s);
				d('E',s);
				d('V',s);
				d('E',s);
				d('N',s);
				A.pb(7);
			}
			while(fi('N',s)) {
				d('N',s);
				d('I',s);
				d('N',s);
				d('E',s);
				A.pb(9);
			}
		}
		sort(A.begin(), A.end());
		cout << "Case #"<< (t+1) <<": ";
		F0(i,SZ(A)) {
			cout<<A[i];
		}
		cout << endl;
	}
	return 0;
}