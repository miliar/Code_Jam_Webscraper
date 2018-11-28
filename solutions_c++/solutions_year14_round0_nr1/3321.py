#include<fstream>
using namespace std;

int main(int argc,char *argv[])
{
ifstream fin(argv[1]);
ofstream fout("output.txt");
	int t;
	fin>>t;
	for(int i=1;i<=t;i++){
	fout<<"Case #"<<i<<": ";
		int mat1[4][4],mat2[4][4],ans1,ans2;
		fin>>ans1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				fin>>mat1[j][k];
		fin>>ans2;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				fin>>mat2[j][k];
		int matched=-1,count=0;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				if(mat1[ans1-1][j]==mat2[ans2-1][k]){
					count++;
					matched=mat1[ans1-1][j];
				}
		if(count>1)
			fout<<"Bad magician!";
		else if(count<1)
			fout<<"Volunteer cheated!";
		else 
			fout<<matched;
		fout<<endl;
	}
fin.close();
fout.close();
return 0;
}


