// Include Header and Libraries
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>

#define FOR(i,n) for(int i=0;i<n;i++)

using namespace std;

// Main Program Starts
int main() {

	
	int T=0;

	cin >> T;

	FOR(t,T){
		int sm;
		
		cin >> sm;
		
		string a;

		cin >> a;
		
		int add=0;
		
		int ov=0;

		FOR(i,sm+1){
			if(i<=ov) ov+=a[i]-'0';
			else{
				add+=i-ov;
				ov=i+a[i]-'0';
			}
		}
		cout << "Case #" << t+1 <<": " << add << endl;
	}
		
	return 0;
}

