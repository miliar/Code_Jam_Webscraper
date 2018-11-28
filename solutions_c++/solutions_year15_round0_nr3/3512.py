#include<iostream>
#include<string>
#define f first
#define s second
#define mp make_pair
using namespace std;

int t, l, x;

string chars = "1ijk";

pair<char, bool> mat[4][4] = {	{mp('1', 0), mp('i', 0), mp('j', 0), mp('k', 0)},
								{mp('i', 0), mp('1', 1), mp('k', 0), mp('j', 1)},
								{mp('j', 0), mp('k', 1), mp('1', 1), mp('i', 0)},
								{mp('k', 0), mp('j', 0), mp('i', 1), mp('1', 1)}
							 };
							 
pair<char, bool> operator*(pair<char, bool> l, pair<char, bool> r) {
	bool sign = l.s ^ r.s;
	
	pair<char, bool> ret = mat[chars.find(l.f)][chars.find(r.f)];
	ret.s = ret.s ^ sign;
	
	return ret;
}



//---------------------------------------------------------------
//Main algorithm begins here

pair<char, bool> rangeacc[10001][10001];


int main() {
	
	cin.sync_with_stdio(false);
	cin >> t;
	
	for(int TCASE = 1; TCASE <= t; TCASE++) {
		cin >> l >> x;
		
		string str, tmp;
		cin >> tmp;
		
		for(int i=0;i<x;i++)
			str += tmp;
		
		int sz = l * x;
		
		
		for(int i=0;i <= sz;i++) {
			rangeacc[i][i] = mp('1', false);
			
			for(int j=i;j<sz;j++)
				rangeacc[i][j+1] = rangeacc[i][j] * mp(str[j], false);
		}
		
		bool valid = false;
		
		for(int i=1;i<sz;i++)
			for(int j=i+1;j<sz;j++) {
			
				if(rangeacc[0][i] == mp('i', false) && rangeacc[i][j] == mp('j', false) && rangeacc[j][sz] == mp('k', false) )
					valid = true;
			}
		
		
		cout << "Case #" << TCASE << ": ";
		
		if(valid)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	
	return 0;
}







































