#include<fstream>
using namespace std;
int grass[100][100];
int n,m;
bool is_InRow(int i,int j){

	for(int a=0;a<m;a++)
		if(grass[i][j]<grass[i][a]) {
			return true;
		}
	return false;
}
bool is_InColomn(int i,int j){
	
	for(int a=0;a<n;a++)
		if(grass[i][j]<grass[a][j]) {
			return true;
		}
	return false;
}
int main(){
	ofstream fout ("B-large.out");
	ifstream fin ("B-large.in");

	int i,j,t,k,a;
	fin>>t;
	bool is_possible;

		for(k=1;k<=t;k++){

			fin>>n>>m;
			is_possible=true;
			for(i=0;i<n;i++)
				for(j=0;j<m;j++)
					fin>>grass[i][j];
				
			for(i=0;i<n;i++){
				for(j=0;j<m;j++)
					if(is_InRow(i,j)&&is_InColomn(i,j)){
						is_possible=false;
						break;
					}
				if(is_possible==false)break;
			}

			if(is_possible)
				fout<<"Case #"<<k<<": YES"<<endl;
			else
				fout<<"Case #"<<k<<": NO"<<endl;
		}

	return 0;
}