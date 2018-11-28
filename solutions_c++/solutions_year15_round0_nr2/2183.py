//============================================================================
// Name        : CodeJam2015_Qa_B.cpp
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
#include <stdio.h>

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

const int maxn = 1001 ;
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

int cakes[maxn] ;

const int small = 9 ;
const int large = 1000;
const int maxP = large;

int maxx ;

int d(int n, int i){
	if(i <= n)
		return 0;

	int count = 0 ;
	while(i > n){
		i -= n;
		count++;
	}
	return count;
}

int f(int n ){
//	cout << "f" <<  n    <<endl ;
	int result = n ;

	for(int i = maxx ; i >= 1 ; i--){
		int de = d(n,i) ;
//		cout << "i " <<  i << " de " << de << "  cakes[i] " <<  cakes[i] <<endl ;
		result += de * cakes[i] ;
	}

	return result ;
}

void main2(){

	// init
	F1(i,maxP){
		cakes[i] = 0 ;
	}

	maxx = 0;
	// input
	int N ;
	cin >> N ;
//	cout << N << endl ;
	F0(i,N){
		int cake;
		cin >> cake ;
//		cout << cake << " " ;
		cakes[cake]++ ;

		maxx =  std::max(maxx, cake);
	}
//	cout << endl ;

	// count result
	int minn = maxx;
//	cout << "min " <<  minn << " " <<endl ;

	for(int i = maxx ; i >= 1 ; i--){

		int count = f(i);
//		cout << "i " <<  i << " count " << count  <<endl ;
		minn = std::min(minn , count) ;
	}

	cout << minn << endl ;

}

int main() {
//	    freopen("test.in", "r", stdin);

//	    freopen("B-small-attempt1.in", "r", stdin);
//	    freopen("B-small.out", "w", stdout);

	    freopen("B-large.in", "r", stdin);
	    freopen("B-large.out", "w", stdout);

	    scanf("%d\n" , &tn) ;

	    F1(tt,tn) {
	    	printf("Case #%d: ", tt);
	    	main2();

	    }

	return 0;
}




