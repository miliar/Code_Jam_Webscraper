#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std;

#define YES 1
#define NO 2

string ans[3] = {"Case #",": YES\n",": NO\n"};

ifstream fin;
ofstream fout;
int N , M;

bool
chk(int row , int col , int h,vector<vector<int> >& record){//, vector<vector<int> > & current){
	bool flag_h = true;
	bool flag_v = true;
	//fix the row, try cross the lawn horizontally ->>
	for(int i = 0 ; i < M ; i++ ){
		if(record[row][i] > h){
			flag_h = false;
			break;
		}
	}

	//fix the col, try cross the lawn vertically  |
	for(int i = 0 ; i < N ; i++){
		if(record[i][col] > h){
			flag_v = false;
			break;
		}
	}
	return flag_h || flag_v;
}

int 
solve(){
	fin >> N >> M ;
	vector<vector<int> >record;

	//init the data
	for(int i = 0 ; i < N ; i++){
		record.push_back(vector<int>(M));
		for(int j = 0 ; j < M ; j++){
			fin >> record[i][j];
		}
	}

	//height from 99 to 1
	//every time check whether the lawnmower could go through the lawn
	for(int h = 99 ; h > 0 ; h--){
		for(int i = 0 ; i < N ; i++){
			for(int j = 0 ; j < M ; j++){
				//check the row i / col j
				if(record[i][j] == h)
					if(!chk(i,j,h,record))//,current))
						return NO;
			}
		}
	}
	return YES;
}

int
main(){
	fin.open("2.in",ifstream::in);
	fout.open("2.out",ofstream::out);
	int T;
	fin>>T;
	for(int i = 1 ; i <= T ;i++){
		fout<<ans[0]<<i<<ans[solve()];
	}
	return 0;
}
