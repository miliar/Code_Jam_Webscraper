#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>


using namespace std;


int main(int argc, char* argv[])
{
	ifstream fin ("A-small-attempt1.in");
	//ifstream fin ("test");
	ofstream fout ("output.out");

	int oldA[4][4];
	int newA[4][4];

	int cases;
	fin >> cases;

	cout<<cases;

	for(int i=1;i<=cases;i++){
		fout << "Case #"<<i<<": ";
		int row1, row2;
		cout<<"case "<<i<<endl;

		fin>>row1;
		row1--;
		for(int x=0;x<4;x++)
			for(int y=0;y<4;y++)
				fin>>oldA[x][y];


		fin>> row2;
		row2--;
		for(int x=0;x<4;x++)
			for(int y=0;y<4;y++)
				fin>>newA[x][y];

		bool flag = false;
		bool cheat = false;
		int num;
		
		for( int k = 0; k<4; k++){
			for( int l = 0; l<4; l++){
				if( oldA[row1][k] == newA[row2][l] && flag ){
					fout<<"Bad magician!";
					cheat = true;
					break;
				}
				if( oldA[row1][k] == newA[row2][l] && !flag){
					flag=true;
					num = oldA[row1][k];
				}
			}
			if(cheat)
				break;
		}
		if(!flag)
			fout<<"Volunteer cheated!";
		else if(!cheat)
			fout<<num;
		fout<<endl;		
	}

	fin.close();
	fout.close();


	return 0;
}

