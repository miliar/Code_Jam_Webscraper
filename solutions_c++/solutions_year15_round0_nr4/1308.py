//============================================================================
// Name        : CodeJam2015_Qa_D.cpp
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
#define all(x) x.begin() , x.end()
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

template <class T>
void printAll(vector<T> vecs){
	for(int i = 0 ; i< SZ(vecs) ; i++){
		cout << vecs[i] << " " ;
	}
	cout << endl;
}
template <class T>
void printAll( T vecs[] , int length){
	for(int i = 0 ; i< length ; i++){
		cout << vecs[i] << " " ;
	}
	cout << endl;
}
int nCr(int n, int r) {
   if(r>n) {printf("FATAL ERROR"); return 0;}
   if(n==0 || r==0 || n==r) {
      return 1;
   } else {
      return (int)lround( ((double)n/(double)(n-r)/(double)r) * exp(lgamma(n) - lgamma(n-r) - lgamma(r)));
   }
}
int nPr(int n, int r) {
   if(r>n) {printf("FATAL ERROR"); return 0;}
   if(n==0 || r==0) {
      return 1;
   } else {
      if (n==r) {
         r = n - 1;
      }
      return (int)lround( ((double)n/(double)(n-r)) * exp(lgamma(n) - lgamma(n-r)));
   }
}

bool small(int x , int r, int c){
	if(x == 1)
		return true;

	if(x == 2){
		if(r*c % 2 == 0 ){
			return true;
		}else{
			return false;
		}
	}

	if(x==3){
		if(r== 1 || c == 1){
			return false;
		}
		if(r*c %3 ==0){
			return true;
		}
		return false;
	}

	if(x==4){
		if(r== 1 || c == 1){
			return false;
		}
		if(r== 2 || c == 2){
			return false;
		}
		if(r*c %4 ==0){
			return true;
		}
		return false;
	}


	return false;
}

void main2(){
	int X , R , C ;
	cin >> X >> R >> C ;
//	cout << X << " " << R << " " << C << " " << endl ;

	if(small(X,R,C)){
		cout << "GABRIEL" << endl;
	}else{
		cout << "RICHARD" << endl;
	}
}

int main() {
	    freopen("test.in", "r", stdin);

	    freopen("D-small-attempt0.in", "r", stdin);
	    freopen("D-small.out", "w", stdout);

//	    freopen("C-large-practice.in", "r", stdin);
//	    freopen("C-large.out", "w", stdout);

	    scanf("%d\n" , &tn) ;

	    F1(tt,tn) {
	    	printf("Case #%d: ", tt);
	    	main2();

	    }

	return 0;
}




