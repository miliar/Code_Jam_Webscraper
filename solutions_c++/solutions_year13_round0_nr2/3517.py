#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>
#include<climits>
using namespace std;
int verify(vector<vector<int> > input){
	int rows=(int)input.size();
	int cols=(int)input[0].size();
	vector<int> rowmax(rows);
	vector<int> colmax(cols);
	for(int i=0;i < rows;i++){
		int max=0;
		for(int j=0;j < cols;j++){
			if(input[i][j] > max)max=input[i][j];
		}
		rowmax[i]=max;
	}	
	for(int j=0;j < cols;j++){
		int max=0;
		for(int i=0;i < rows;i++){
			if(input[i][j] > max)max=input[i][j];
		}
		colmax[j]=max;
	}
	for(int i=0;i < rows;i++){
		for(int j=0;j < cols;j++){
			if(!(input[i][j] == rowmax[i] || input[i][j] == colmax[j]))return 0;
		}
	}
	return 1;
}
int main(){
	ifstream myfile;
	string strNum;int num;
	myfile.open("input.txt");
	if(myfile.is_open()){
		if(myfile.good()){
			getline(myfile,strNum);
			istringstream(strNum) >> num;
			for(int test=1;test<=num;test++){
				string strN,strM,strNM;
				int N,M;
				getline(myfile,strNM);
				istringstream nmstream(strNM);
				getline(nmstream,strN,' ');
				getline(nmstream,strM,' ');
				istringstream(strN) >> N;
				istringstream(strM) >> M;
				vector<vector<int> > input(N,vector<int>(M));
				for(int row=0;row < N;row++){
					string lawnrow;
					getline(myfile,lawnrow);
					istringstream rowstream(lawnrow);
					for(int col=0;col < M;col++){
						string strHeight;int height;
						getline(rowstream,strHeight,' ');
						istringstream(strHeight) >> height;
						input[row][col]=height;
					}
				}
				if(verify(input)){
					cout << "Case #"<<test <<": YES" << endl;
				}else {
					cout << "Case #"<< test <<  ": NO" << endl;
				}
			}
		}
	}		
}
