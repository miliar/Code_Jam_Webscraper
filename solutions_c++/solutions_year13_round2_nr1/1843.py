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
#include <limits>
#include <limits.h>
#include <iomanip>


using namespace std;
#define pb push_back
#define EPS 0.00001
#define MAX 128
int A,N;
vector<int> m;
int count1;


vector<int> countList;


void branch(int a, int i, int c){
//cout << "a is " << a << endl;
//cout << "count is " << c << endl;
	if(i >= N){
		countList.pb(c);
		return;
	}
	// else we are at index i
	if(m[i] < a){
		branch( (a+m[i]) , i+1, c );
	} else {
		// delete
		branch( a, i+1, c+1);
		// add numbers
		if(a> 1){
		int na = a;
		while(true){
			if( m[i] < na ) break;

			na = 2*na - 1;
			c++;
		}
		
		branch( na, i, c);
		}
	}
	//return;
}


int main(){
	int numCases;
	cin >> numCases;

	for(int caseN=1; caseN <= numCases; caseN++){
		cin >> A >> N;
		int a=A;
		int mote;
		m.resize(0);
		for(int i=0 ; i<N; i++){
			cin >> mote;
//cout << "mote " << mote <<endl;
			m.pb(mote);
		}
		/********************/
		//count1 = 0;

/*		for(int j=0; j< N; j++){
			cout << m[j] << " ";
		}
		cout << endl;
*/

		sort(m.begin(), m.end());
		//reverse(m.begin(), m.end());
		// now m is sorted

		countList.resize(0);	
		branch(a, 0, 0);

/*
		while(true){
			int li = m.size() -1; 	// last index
			//cout << "HERE\n";
			if(li < 0) break;
cout << "current a is " << a << endl;
			if(m[li] < a){
				a += m[li];
				m.resize(li);
			} else {
				//int diff = m[li] - a;
				if(2*a-1 > m[li]){
					// if the difference is small enough so that we can add, then add it to a 
					// add count
					a = 2*a-1;
					count1++;

				} else {
					count1++;
					m.resize(li);
				}
			}
		}
*/
		


		// in the end
		sort(countList.begin(), countList.end());
		
		cout << "Case #" << caseN << ": " << countList[0] << endl;
	}

	return 0;
}
