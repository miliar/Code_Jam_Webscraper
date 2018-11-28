#include<fstream>
using namespace std;
int main()
{
	int casenum;
	int count;
	int result;
	int matrixa[4][4];
	int matrixb[4][4];
	int rowa,rowb;
	ofstream fout;
	fout.open("c://output.out");
	ifstream fin; 
	fin.open("c://input.in");
	fin>>casenum;
	for(int num=1;num<=casenum;num++){
		count=0;
	fin>>rowa;
	rowa--;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			fin>>matrixa[i][j];
	fin>>rowb;
	rowb--;
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			fin>>matrixb[i][j];
		fout<<"Case #"<<num<<": ";
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(matrixa[rowa][i]==matrixb[rowb][j])
			{
				result=matrixa[rowa][i];
				count++;
			}
		}
		if(count==1){fout<<result<<endl;continue;}
		if(count>1){fout<<"Bad magician!"<<endl;continue;}
		if(count==0){fout<<"Volunteer cheated!"<<endl;continue;}

	}
	return 0;
}