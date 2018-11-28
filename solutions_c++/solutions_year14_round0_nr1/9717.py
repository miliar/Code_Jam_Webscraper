#include <fstream>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;

	fin.open("A-small-attempt0.in");
	fout.open("A-small-attempt0.out");

	int mat1[4];
	int mat2[4];
	int mat3[4];
	int s1,s2,T;
	int count,i,j,k;
	int tmp;

	fin>>T;

	for(int count=0;count<T;count++)
	{
		for(i=0;i<4;i++)
			mat3[i]=0;
		k=0;

		fin>>s1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				if(i==s1-1)
					fin>>mat1[j];
				else
					fin>>tmp;
			}

		fin>>s2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				{
					if(i==s2-1)
						fin>>mat2[j];
					else
						fin>>tmp;
				}

		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				{
					if(mat1[i]==mat2[j])
						mat3[k++]=mat1[i];
				}
		
		if(mat3[0]==0)
			fout<<"Case #"<<count+1<<": Volunteer cheated!"<<endl;
		
		else if(mat3[1]==0)
			fout<<"Case #"<<count+1<<": "<<mat3[0]<<endl;
		else
			fout<<"Case #"<<count+1<<": Bad magician!"<<endl;
	}

	return 0;
}