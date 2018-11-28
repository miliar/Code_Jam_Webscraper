/*
 * osmos.cpp
 *
 *  Created on: May 4, 2013
 *      Author: saha
 */


#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long mylong;

int main()
{
	int T;
	int A, n;
	vector<int> v;
	int x;

	mylong s=0;

	cin >> T ;
//	cout << "Number of test cases = " << T << endl;
	for(int t=1; t<=T ; t++) {
		cin >> A  >> n ;
//		cout << "****** test case number  = " << t << endl;
//		cout << "A = " << A << ", n = " << n << endl;

		v.clear();
		for(int i=0 ; i<n ; i++) {
			cin >>x;
			v.push_back(x);
		}

		mylong count = 0;
		sort(v.begin(), v.end());
		s=A;
		int j=0;
		for( ; j<n ; j++) {
			if(v[j] < s) {
				s += v[j];
				continue;
			} else {
				mylong s1 = s;
				mylong k=j;
				for( ; k < n ; k++) {
//					cout << "new element inserted " << (s1-1) << endl;
					s1 += (s1-1);
					count++;
					int l=j;
					while(v[l] < s1 && l<n && l<=k)
					{
						s1 += v[l];
						l++;
					}
					s = s1;
					if(v[k] < s) {
//						cout << "now sum is " << s  << " # and breaking "<< endl;
						break;
					}
//					cout << "now temp sum is " << s1 << endl;
				}
				j=k;
			}
		}
		cout << "Case #" << t <<": " << count << endl;
	}


	return 0;
}




