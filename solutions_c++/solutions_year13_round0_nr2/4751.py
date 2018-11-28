#include<iostream>
#include<fstream>
using namespace std;

int n,m;
int mapdata[100][100];

bool solve(int x,int y,int num){
	bool flag = true;
	for(int i=0;i<n;i++){
		if(mapdata[i][x] > num){
			flag = false;
			break;
		}
	}
	if(flag){
		return true;
	}

	for(int i=0;i<m;i++){
		if(mapdata[y][i] > num){
			return false;
		}
	}
	return true;
}

int main(){
	ifstream ifs("B-large.in");
	ofstream ofs("ans2.txt");

	int T;
	ifs >> T;
	for(int loop=0;loop<T;loop++){
		ifs >> n >> m;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				ifs >> mapdata[i][j];
			}
		}

		bool flag = true;
		

		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(!solve(j,i,mapdata[i][j])){
						flag = false;
				}
			}
		}

		ofs << "Case #" << (loop+1) << ": ";
		if(flag){
			ofs << "YES" << endl;
		}else{
			ofs << "NO" << endl;
		}
	}
	ofs.close();
}