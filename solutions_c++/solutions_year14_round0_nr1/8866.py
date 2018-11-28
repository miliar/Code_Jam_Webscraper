#include<fstream>
#include<vector>
#include<iomanip>
using namespace std;

int compareArray(int g1[], int g2[]);
int main()
{


ifstream fin;
ofstream fout;
int numofcase;
fin.open("input.in");
fout.open("output.txt");
fin>>numofcase;
vector<int> v;

for(int casenum=0; casenum<numofcase;casenum++)
{
	int a[4][4];
	int first, second;
	int g1[4],g2[4];
	fin>>first;
	first--;
	for(int i=0; i<4;i++)
		for(int j=0; j<4;j++)
			fin>>a[i][j];
	for(int i=0;i<4;i++)
		g1[i]=a[first][i];
	fin>>second;
	second--;
	for(int i=0; i<4;i++)
		for(int j=0; j<4;j++)
			fin>>a[i][j];
	for(int i=0;i<4;i++)
		g2[i]=a[second][i];
	int result =compareArray(g1,g2);
	v.push_back(result);
}

for(int i=0;i<v.size();i++)
{
	fout<<"Case #"<<i+1<<": ";
	if(v[i]>0)
	fout<<v[i]<<endl;
	else if(v[i]==0)
		fout<<"Bad magician!"<<endl;
	else
		fout<<"Volunteer cheated!"<<endl;
}
}


int compareArray(int g1[], int g2[])
{
	vector<int> result;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(g1[i]==g2[j])
					result.push_back(g2[j]);

		if(result.size()>1)
			return 0;
		else if(result.size()==0)
			return -1;
		else
			return result[0];
}

