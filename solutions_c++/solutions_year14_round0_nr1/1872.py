#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;


int ary1[4][4], ary2[4][4];


int main(){
	ifstream ifs("A-small-attempt1.in");
	ofstream ofs("A-small-output.out");
	int numCases;
	ifs>>numCases;
	for(int q = 0; q<numCases; q++){
		int firstRow = 0;
		int secondRow = 0;
		ifs>>firstRow;
		for(int i = 0; i<4; i++)
			for(int j = 0; j<4; j++)
				ifs>>ary1[i][j];
		ifs>>secondRow;
		for(int i = 0; i<4; i++)
			for(int j = 0; j<4; j++)
				ifs>>ary2[i][j];
		
		
		vector<int> fRow, sRow, ans;
		for(int i = 0; i<4; i++){
			fRow.push_back(ary1[firstRow-1][i]);	
			sRow.push_back(ary2[secondRow-1][i]);	
		}

		sort(fRow.begin(), fRow.end());
		sort(sRow.begin(), sRow.end());
		
		int i = 0, j = 0;
		while( i<4 && j<4){
			if(fRow[i] == sRow[j]){
				ans.push_back(fRow[i]);
				i++;
				j++;
			}else{
				if(fRow[i] < sRow[j]){
					i++;
				}else{
					j++;
				}
			}
		}
		ofs<<"Case #"<<q+1<<": ";
		if(ans.size() == 1)
			ofs<<ans[0]<<endl;
		else if(ans.size() > 1)
			ofs<<"Bad magician!"<<endl;
		else if(ans.size() == 0)
			ofs<<"Volunteer cheated!"<<endl;

		
	}
	system("pause");
}

