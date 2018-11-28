#include <iostream>
#include <string>

using namespace std;

int dig( char c ){
	return c - '0';
}

int solve( int len, string& s)
{
	int p = 0; // people
	int v = 0; // invitees
	
	for (int k=0; k<=len; k++){
		if (k > p){
			v += (k - p);
			p += (k - p);
		}
		p += dig(s[k]);
	}
	
	cerr << "p= " << p << endl; 
	
	return v;
}


int main ()
{
	int T;
	string s;
	
	cerr << "Hello Ovation!!" << endl;

	cin >> T;
	cerr << T << " test cases" << endl;
	
	for (int i=1; i<=T; i++){
		
		int len;
		string s;
		int sol = -1;
		
		cin >> len >> s;
		
		cerr << len << ", " << s << endl;

		sol = solve(len,s);
		cout << "Case #" << i << ": " << sol << endl;
	}
	

	return 0;
}
