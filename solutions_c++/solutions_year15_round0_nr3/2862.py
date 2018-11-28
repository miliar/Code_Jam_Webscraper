#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int A[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int cnt;

bool fun(int x,vector<int> Ch,int n) {
	int i = n, t = Ch.size();
	cnt++;
	if (n >= t || cnt > 100000 )
		return false;
	int p = Ch[n];
	if(x == 4) {
		for(i = n+1; i != t; i++) {
			if(p < 0)
				p = -A[-p][Ch[i]];
			else
				p = A[p][Ch[i]];
		}
		if(p == x)
			return true;
		return false;
	}
	else if( x == 2 ) {
		if( p == x ) {
			if ( fun(3,Ch,i+1) )
				return true;
		}
		for(i = n+1; i != t; i++) {
			if(p < 0)
				p = -A[-p][Ch[i]];
			else
				p = A[p][Ch[i]];
			if( p == x ) {
				if ( fun(3,Ch,i+1) )
					return true;
			}
		}
		return false;
	}
	else if ( x == 3 ) {
		if( p == x ) {
			if ( fun(4,Ch,i+1) )
				return true;
		}
		for(i = n+1; i != t; i++) {
			if(p < 0)
				p = -A[-p][Ch[i]];
			else
				p = A[p][Ch[i]];
			if( p == x ) {
				if ( fun(4,Ch,i+1) )
					return true;
			}
		}
		return false;
	}
	else
		return false;
}

int main() {
	int T;
	cin >> T;
	for(int i=1;i <=T; i++) {
		int L,X;
		cin >> L >> X;
		string U;
		cin >> U;
		vector<int> Ch;
		for(int j =0 ; j != X; j++) {
			for(int k = 0; k != L; k++) {
				int m = U[k] - 103;
				Ch.push_back(m);
			}
		}
		cnt = 0;
		if(fun(2,Ch,0))
			U = "YES";
		else
			U = "NO";
		cout << "Case #"<< i << ": " << U << endl;
	}
	return 0;
}
