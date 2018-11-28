#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<climits>
#include<algorithm>
#include<set>
#include<math.h>
#include<map>
#include<time.h>
#include<fstream>
#include<sstream>

#define FOR(i ,  n) \
	for(i = 0; i < n; i++)
#define FORI(i ,startForIndex , endForIndex) \
	for(i = startForIndex ;i < endForIndex; i++)
#define FORD(i ,startForIndex , endForIndex) \
	for(i = startForIndex - 1;i >= endForIndex; i--)
#define tr( container , it) \
	for( typeof(container.begin()) it = container.begin() ; it != container.end() ; it++ ) 
#define print1(ar) \
	for( typeof(ar.begin()) it = ar.begin() ; it != ar.end(); it++){\
		cout << * it << " " ;\
	}printf("\n") ;
#define print2(ar)\
	for( typeof(ar.begin()) it = ar.begin() ; it != ar.end(); it++){\
		for(typeof(it->begin()) itt = it->begin() ; itt !=  it->end() ; itt++ ){\
			cout << * itt << " " ;\
		}printf("\n") ;\
	}printf("\n");
#define ALL(ar)\
	ar.begin() , ar.end()
#define PB push_back
#define LL long long int 
#define VI	vector < int > 
#define VVI 	vector < VI >  
#define VVVI 	vector < VVI > 
#define VS	vector < string >
#define VL	vector < LL > 
#define VVL 	vector < VL >
#define V(i) 	vector < i >
#define VV(i) 	vector < vector < node > > 
#define pi(var)	cout << #var << " = " << var << endl ;
#define si(var)	scanf("%d" , &var)
using namespace std ;

LL pali(LL num) {
	VL ar;
	LL i , n, fl = 1;
	while(num != 0) {
		ar.PB(num %10 );
		num /= 10 ;
	}
	n = ar.size() ;
	FOR(i, n /2) {
		if(ar[i] != ar[n-1-i])  {
			fl =0 ;
			break ;
		}
	}
	return fl ;
}

int main(){
	LL i , t , j , tmp, n, m , k , cnt , fl, ind, a, b, t1, t2;
	int val[] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002, 10000001 } ;
	/*pi(sizeof(val) / sizeof(int)) ;
	FOR(i, 40) {
		cout << val[i] << " " << i << endl;
	}*/
	cin >> t; 
	FOR(k,t) {
		scanf("%lld %lld",  &a, &b) ;
		t1 = sqrt(a) ;
		t2 = sqrt(b) ;
		if( t1 * t1 != a ) {
			t1++ ;
		}
		cnt = 0;
		FOR(i,40) {
			if(val[i] >= t1 and val[i] <= t2) {
				cnt++ ;
			}
		}
		printf("Case #%lld: %d\n", k+1, cnt) ;
	}
}
