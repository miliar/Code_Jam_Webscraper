//============================================================================
// Name        : CodeJam2014_1B_B.cpp
// Author      : jackson huang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


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
#include <stack>
#include <sstream>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define STRLEN(x) (int)(strlen(x))
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }

const int maxn = 1000 ;
char line[maxn] ;
int cnt ;
int i,j,k,m,n,x,y,z;
int tt, tn;

void main2(){
	int A,B,K ;

	cin >> A >> B >> K ;

	int result = 0 ;


	for(int a = 0 ; a < A ; a++){
		for(int b = 0 ; b < B ; b++){
			if( (a & b) < K){
//				cout << a << " " << b << " " << K <<  endl;
				result ++ ;
			}
		}
	}

	cout << result << endl ;



}

int main() {
//	    freopen("test.in", "r", stdin);

	    freopen("B-small-attempt0.in", "r", stdin);
	    freopen("B-small.out", "w", stdout);

//	    freopen("B-large-practice.in", "r", stdin);
//	    freopen("B-large.out", "w", stdout);

	    scanf("%d\n" , &tn) ;

	    F1(tt,tn) {
	    	printf("Case #%d: ", tt);
	    	main2();

	    }

	return 0;
}


