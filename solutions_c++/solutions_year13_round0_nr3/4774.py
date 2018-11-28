#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;
// 1 2 3 11 111 121 
ofstream fo("haha.out");
bool isp(int n) {
	int a[128]={0};
	while (n) {
		a[++a[0]] = n%10;
		n/=10;
	}
	for ( int i = 1 ; i <= a[0]/2 ; ++ i )
		if ( a[i] != a[a[0]-i+1] )
			return false;
return true;
}
int main () {
	int t, i ,j;
	int T, A, B;
	int count;
	
	cin >> T;

	for ( t = 1 ; t <= T ; ++ t ) {
		cin >> A >> B;
		count=0;
		for ( i = A ; i <= B ; ++ i )
		if (isp(i)&&sqrt(i)==(int)(sqrt(i))&&isp(sqrt(i))) {
			count++;
		}
		cout << "Case #" << t << ": " << count<<endl;
	} 
	return 0;
}
