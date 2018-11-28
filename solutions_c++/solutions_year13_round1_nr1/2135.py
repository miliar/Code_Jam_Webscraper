#include <cstdio>
#include <iostream>
using namespace std;
#define SMALL
//#define LARGE

int main() {
	long double x;
long double y;
long double counting=0;
	freopen("A-sample.in", "rt", stdin);
	#ifdef SMALL
		freopen("A-small-attempt2.in", "rt", stdin);
		freopen("A-small-attempt2.out", "wt", stdout);
	#endif
	#ifdef LARGE
		freopen("A-large-practice.in", "rt", stdin);
		freopen("A-large-practice.out", "wt", stdout);
	#endif

	int T;					//The number of test cases
	
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin>>x>>y;
		while(y>0){
		y+=(x*x);
		++x;
		y-=(x*x);
		++x;
		if(y>=0){
		counting+=1;
		}}
		cout << "Case #" << i << ": ";
		cout << counting;
		cout << endl;
		counting = 0;
	}
	
	return 0;
}