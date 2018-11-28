#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;

	int x1,x2,a,num,n,count=0;

    vector<int> temp;
    vector<vector<int>> v1,v2;
	
	fin.open("A-small-attempt0.in");
	fout.open("A-small-attempt0.out");

	fin>>n;

	for(int i=0;i<n;i++){
		v1.clear();
		v2.clear();
		temp.clear();
		
		count=0;
		
		fin>>x1;

		for(int j = 0; j < 4; j++){
			for(int k = 0;k < 4;k++){

				fin>>a;
				temp.push_back(a);
			}

			v1.push_back(temp);
			temp.clear();
		}

		fin>>x2;
		
		for(int j=0;j<4;++j){

			for(int k=0;k<4;++k){

				fin>>a;
				temp.push_back(a);
			}

			v2.push_back(temp);
			temp.clear();
		}
		
		for(int j=0;j<4;j++){

			for(int k=0;k<4;k++){

				if(v1[x1-1][j] == v2[x2-1][k]){	
					
					count++;
					num=v1[x1-1][j];
				}
			}
		}

		if(count==0){

			fout<<"Case #"<<i+1<<":"<<" Volunteer cheated!"<<endl;
		}
		else if(count==1){

			fout<<"Case #"<<i+1<<": "<<num<<endl;
		}
		else if(count>1){

			fout<<"Case #"<<i+1<<":"<<" Bad magician!"<<endl;
		}
	}

	return 0;
}