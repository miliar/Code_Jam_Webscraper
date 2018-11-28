#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <array>
#include <math.h>
#include <cmath>
#include <iomanip>

using namespace std;

#define For(i,m,n) for(int i=m; i<n; i++)


int main() {
	bool isSmall = false;
	if (isSmall) {
		//freopen("practice.txt","rt",stdin);
		freopen("A-small-attempt0.in","rt",stdin);
		freopen("A-small.out","wt",stdout);
	}
	else {
		freopen("A-large.in","rt",stdin);
		freopen("A-large.out","wt",stdout);
	}
	
	int T;
	cin >> T;
	
	int Smax;
	string s;
	int count, total;
	For(caseNum,1,T+1) {
		printf("Case #%d: ", caseNum);
		cin >> Smax >> s;
		total = 0;
		count = 0;
		For(i,0,Smax+1) {
			if (total < i && s[i] != '0') {
				count += i-total;
				total = i;
			}
			total += (int) ( s[i] - '0');
					
		}
		
		
		cout << count << endl;
	}
	

	return 0;
	
}
