#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <set>
#include <cstring>
#include <cassert>

#define F(i, a,b) for(int i=int(a);i<int(b);i++)
#define foreach(it, l) for (typeof(l.begin()) it = l.begin(); it != l.end(); it++)
#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;

#define L long long
using namespace std;

int cases = 1;

void resolve() {
	int n;
	cin >> n;
	vector<double> A;
	vector<double> B;
	vector<double> BB;
	F(i,0,n) {
		double aa; cin >> aa;
		A.push_back(aa);
	}
	F(i,0,n) {
		double aa; cin >> aa;
		B.push_back(aa);
		BB.push_back(aa);
	}
	int res = 0, res2 = 0;
	F(i,0,n) {
		int indice = -1;
		double minimo = 10;
		F(j,0,n) {
			if(A[i] - B[j] > 0) {
				if(A[i] - B[j] < minimo) {
					minimo = A[i] - B[j];
					indice = j;
				}
			}
		}
		if(indice != -1) {
			B[indice] = 1;
			res++;
		}
	}

	F(i,0,n) {
		int indice = -1;
		double minimo = 10;
		F(j,0,n) {
			if(BB[i] - A[j] > 0) {
				if(BB[i] - A[j] < minimo) {
					minimo = BB[i] - A[j];
					indice = j;
				}
			}
		}
		if(indice != -1) {
			A[indice] = 1;
			res2++;
		}
	}

	cout <<"Case #"<< cases++ << ": "<< res << " " << n - res2 <<endl;
}

int main() {
	int t;
	cin >> t;
	F(i,0,t) resolve();	
}