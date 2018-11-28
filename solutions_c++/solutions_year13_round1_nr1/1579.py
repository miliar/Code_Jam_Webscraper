/* BA 2013 */
#include <iostream>
#include <cmath>
#include <cstdio>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <utility>

using namespace std;
#define pb push_back
long long r, t;

int main(){
	int numCases;
	cin >> numCases;

	for(int caseN=1; caseN <= numCases; caseN++){
		cin >> r >> t;
		/// done obtaining information

		long long left = t;
		long long i;
		for(i=0; ; i++){
			left -= 2L*(r+2L*i) + 1L;
			if(left < 0){
				break;	
			}
		}
		// i is the index such that it is not enough


		cout << "Case #" << caseN << ": " << i << endl;
	}

	return 0;
}
