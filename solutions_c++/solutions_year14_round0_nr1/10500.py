//============================================================================
// Name        : googleCodeJam.cpp
// Author      : pH
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <unordered_map>
#include <unordered_set>
//#define F(i,a,b) for(int i=a; i<b; ++i)
using namespace std;

void problem3() {

}

void problem2() {

}

void problem1() {
	std::ios::sync_with_stdio(false);

	int t;
	int r1, r2;
	cin>>t;
	for(int icount=0; icount<t; ++icount) {
		bool found = false;
		int selection=0;
		cin>>r1;
		int rowNums1, rowNums2;
		unordered_set<int> firstRow;
		int skipCount=(r1-1)*4;
		for(int i=0; i<16; ++i) {
			if(i<skipCount || i>=skipCount+4) {
				scanf("%*d");
				continue;
			}
			cin>>rowNums1;
			firstRow.insert(rowNums1);
		}
		cin>>r2;
		int skipCount2=(r2-1)*4;
		for(int i=0; i<16; ++i) {
			if(i<skipCount2 || i>=skipCount2+4) {
				scanf("%*d");
				continue;
			}
			cin>>rowNums2;
			if(firstRow.find(rowNums2) != firstRow.end()) {
				if(!found) {
					selection = rowNums2;
					found = true;
				} else {
					cout<<"Case #"<<icount+1<<": Bad magician!"<<endl;
					selection = -1;
					firstRow.clear();
				}
			}
		}
		if(!found) {
			cout<<"Case #"<<icount+1<<": Volunteer cheated!"<<endl;
		} else if(selection > 0){
			cout<<"Case #"<<icount+1<<": "<<selection<<endl;
		}
	}


}
int main() {
	problem1();
//	problem2();
//	problem3();
	return 0;
}
