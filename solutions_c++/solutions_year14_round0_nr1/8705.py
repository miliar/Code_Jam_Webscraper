// Jai Mata Di
// https://code.google.com/codejam/contest/2974486/dashboard#s=p0
#include <iostream>
#include <vector>
using namespace std;
class MagiciansTrick{
	int caseNo;
	int sizeOfGrid;
	public:
	MagiciansTrick(int caseNum)
	{
		caseNo = caseNum;
		sizeOfGrid = 4;
	}
	void run() {
		int choice1;
		cin>>choice1;
		vector<vector<short> > grid1;

		for (int i = 0; i < sizeOfGrid; i++) {
			vector<short> v;
			for (int j = 0; j < sizeOfGrid; j++) {
				int z;
				cin >> z;
				v.push_back(z);
			}
			grid1.push_back(v);
		}
		int choice2;
		cin>>choice2;
		vector<vector<short> > grid2;
		for (int i = 0; i < sizeOfGrid; i++) {
			vector<short> v;
			for (int j = 0; j < sizeOfGrid; j++) {
				int z;
				cin >> z;
				v.push_back(z);
			}
			grid2.push_back(v);
		}

		int countOfOverlaps=0;
		int ans = -1;
		for(int i=0;i<sizeOfGrid;i++){
			for(int j=0;j<sizeOfGrid;j++){
				if(grid1[choice1-1][i] == grid2[choice2-1][j]){
					ans = grid1[choice1-1][i];
					countOfOverlaps++;
				}
			}
		}

		if(countOfOverlaps == 1)
		{
			cout<<"Case #"<<caseNo<<": "<<ans<<endl;
		}
		else if(countOfOverlaps == 0){
			cout<<"Case #"<<caseNo<<": Volunteer cheated!"<<endl;
		}
		else{
			cout<<"Case #"<<caseNo<<": Bad magician!"<<endl;
		}
	}
};
int main() {
	int noOfTestCases;
	cin>>noOfTestCases;
	for(int testCaseNo = 1; testCaseNo <= noOfTestCases;testCaseNo++){
		MagiciansTrick m(testCaseNo);
		m.run();
	}
	return 0;
}

