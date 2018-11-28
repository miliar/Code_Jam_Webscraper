//============================================================================
// Name        : CodeJam2015_Qa_A.cpp
// Author      : jackson huang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>     // std::string, std::stoi

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


int getint(char a){
	if( a== '0')
		return 0 ;
	else if( a =='1')
		return 1 ;
	else if( a =='2')
		return 2 ;
	else if( a =='3')
		return 3 ;
	else if( a =='4')
		return 4 ;
	else if( a =='5')
		return 5 ;
	else if( a =='6')
		return 6 ;
	else if( a =='7')
		return 7 ;
	else if( a =='8')
		return 8 ;
	else if( a =='9')
		return 9 ;

	return 0;

}

void main2(){
	int N ;
	string aud ;
	cin >> N >> aud ;

//	cout << N << " " <<  aud << endl ;


	int result = 0 ;
	int stand  = getint(aud[0]) ;
	F0(i,N+1){
		if(stand  > i && i+1 <= N+1){
			stand += getint(aud[i+1]);

		}else{
			result ++ ;
			stand ++ ;
			if(stand  > i && i+1 <= N+1){
				stand += getint(aud[i+1]);
			}

		}
//		cout << " i " << i << " stand " << stand <<  " result "  << result << endl ;
	}

	cout << result << endl ;
}

int main() {
//	    freopen("test.in", "r", stdin);

//	    freopen("A-small-attempt0.in", "r", stdin);
//	    freopen("A-small.out", "w", stdout);

	    freopen("A-large.in", "r", stdin);
	    freopen("A-large.out", "w", stdout);

	    scanf("%d\n" , &tn) ;

	    F1(tt,tn) {
	    	printf("Case #%d: ", tt);
	    	main2();

	    }

	return 0;
}




