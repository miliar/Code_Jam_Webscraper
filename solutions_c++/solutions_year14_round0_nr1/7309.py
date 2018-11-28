#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;
bool canFindinSecondMatrix(int cur, int matrix[2][4][4], int row){
	for(int i = 0 ; i<4;++i){
		if(matrix[1][row-1][i]==cur)
			return true;
	}
	return false;
}
void showAns(int round, vector<int> ans, ofstream& file){
	file<<"Case #"<<round<<": ";
	int num = ans.size();
	if(num == 0)
		file<<"Volunteer cheated!";
	else if(num ==1)
		file<<ans[0];
	else
		file<<"Bad magician!";
	file<<endl;
	return;
}
void main(){
	ifstream file("A-small-attempt2.in");
	if(!file)
		return;
	int T =0;
	file>>T;
	ofstream outfile("output");
	for(int idx = 1; idx<=T; ++idx){
		int ans[2];
		int matrix[2][4][4];
		for(int n =0; n<2; ++n){
			file>>ans[n];
			for(int i = 0;i<4;++i){
				for(int j = 0; j < 4;++j){
					file>>matrix[n][i][j];
				}
			}
		}
		vector<int> answer;
		for(int i = 0; i < 4; ++i){
			int cur = matrix[0][ans[0]-1][i];
			if(canFindinSecondMatrix(cur,matrix,ans[1]))
				answer.push_back(cur);
		}
		showAns(idx,answer,outfile);	
	}
	outfile.close();
	file.close();

}