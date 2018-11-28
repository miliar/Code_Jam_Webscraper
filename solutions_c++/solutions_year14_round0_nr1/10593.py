#include <iostream>
#include <string.h>
#include <set>
using namespace std;

int* getRowData(int fstRow[4]){
	int fst=0;
	cin>>fst;
	for(int i=0; i<4; ++i){
		for(int j=0; j<4; ++j){
			int t=0;
			cin>>t;
			if(i==fst-1){
				fstRow[j] = t;
			}
		}
	}
	return fstRow;
}

int main() {
	int N=0;
	cin>>N;
	for(int prob=1; prob<=N; ++prob){
		int fstRow[4];
		int sndRow[4];
		memset(fstRow, 0, sizeof(fstRow));
		memset(sndRow, 0, sizeof(sndRow));
		getRowData(fstRow);
		getRowData(sndRow);

		set<int> fstSet;
		for(int i=0; i<4; ++i){
			fstSet.insert(fstRow[i]);
		}
	
		
		int findNum=0;
		int findInd=0;
		for(int i=0; i<4; ++i){
			if(fstSet.find(sndRow[i]) != fstSet.end()){
				findNum++;
				findInd=i;
			}
		}

		cout << "Case #" << prob << ": ";
		if(findNum==1)  cout << sndRow[findInd];
		else if(findNum>1) cout << "Bad magician!";
		else cout << "Volunteer cheated!";
		cout << endl;
	}
	return 0;
}