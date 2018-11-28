/* https://code.google.com/codejam/contest/2974486/dashboard#s=p0 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int main() {
	int T, row_ans1, row_ans2, arrangement1[4][4], arrangement2[4][4], card1, card2;
	cin>>T;

	for(int i = 0; i < T; i++) {
		row_ans1 = row_ans2 = card1 = card2 = 0;

		cin>>row_ans1;
		row_ans1--;
		for(int j1 = 0; j1 < 4; j1++) {
			for(int k1 = 0; k1 < 4; k1++) {
				cin>>arrangement1[j1][k1];
			}
		}		

		cin>>row_ans2;
		row_ans2--;
		for(int j2 = 0; j2 < 4; j2++) {
			for(int k2 = 0; k2 < 4; k2++) {
				cin>>arrangement2[j2][k2];
			}
		}

		// Comparison
		for(int j3 = 0; j3 < 4; j3++) {
			for(int k3 = 0; k3 < 4; k3++) {
				if(arrangement1[row_ans1][j3] == arrangement2[row_ans2][k3]) {
					if(0 == card1) {
						card1 = arrangement1[row_ans1][j3];
						k3 = 3; // Reset the pointer in row_ans2
					} else {
						card2 = arrangement2[row_ans1][j3];
						j3 = k3 = 3; // Do not look any further for the cards. Exit both the loops 
					}
				}
			}
		}		

		cout<<"Case #"<<i+1<<": ";
		if(0 != card1 && 0 == card2) {
			cout<<card1<<endl;
		} else if(0 == card1 && 0 == card2) {
			cout<<"Volunteer cheated!"<<endl;
		} else {
			cout<<"Bad magician!"<<endl;
		} // end of all test cases
	}
} //end of main()
