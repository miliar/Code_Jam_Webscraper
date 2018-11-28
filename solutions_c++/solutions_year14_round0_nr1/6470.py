#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main(int argc, char* argv[])
{
  string filename= argv[1];
  string line;
  ifstream file(filename.c_str());
	int numTests;
	file>>numTests;
	int i =1; 	
	int ans1, ans2;
	int grid1[4][4], grid2[4][4];
	bool skip =true;
	int testCount=0;
  while (file) {
		if (i%10==1 ) {
			if (!skip) {
			++testCount;
			int count=0,element;
			for (int j=0; j<4; ++j)
			{		
				for (int k=0; k<4; ++k) {
					if (grid1[ans1-1][j] == grid2[ans2-1][k]){
						element =grid1[ans1-1][j];
						++count;
					}
				}
			}
			if (count > 1) {
				cout <<"Case #"<<testCount<<": Bad magician!"<<endl;
			}	else if (count ==0){
				cout<<"Case #"<<testCount<<": Volunteer cheated!"<<endl;
			}else if (count ==1) {
				cout<<"Case #"<<testCount<<": "<<element<<endl;
			}
			}
			file>>ans1;
			skip =false;
			i=1;
		} else if (i%5 == 1) {
			file>>ans2;
		}
		if (i>=2 && i<=5) {
			for (int j=0;j<4;++j){
				file>>grid1[i-2][j];
			}
		}	else if (i>=7 && i<=10){ 
			for (int j=0;j<4;++j){
				file>>grid2[i-7][j];
			}
		}
		++i;
	}
	/*cout <<"GRID1 "<<ans1<<endl;
	for (int i=0;i<4;++i){
		for (int j=0;j<4;++j){
			cout <<grid1[i][j]<<" ";
		}
		cout<<endl;
	}	
	cout <<"GRID2 "<<ans2<<endl;
	for (int i=0;i<4;++i){
		for (int j=0;j<4;++j){
			cout <<grid2[i][j]<<" ";
		}
		cout<<endl;
	}*/
  file.close();
}
