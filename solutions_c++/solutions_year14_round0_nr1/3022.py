#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int arr1[4][4];
	int arr2[4][4];
	int N,r1,r2;//number of test cases
	ifstream in_f("A-small-attempt0.in",ios::in);
	ofstream out_f("A-small-attempt0.in.out",ios::out);
	in_f>>N;
	for(int CasesCount=1;CasesCount<=N;CasesCount++)
	{
		in_f>>r1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				in_f>>arr1[i][j];

		in_f>>r2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				in_f>>arr2[i][j];

		int comp=0;
		int TS;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				{
					if(arr1[r1-1][i]==arr2[r2-1][j])
					{
						comp++;
						TS=arr1[r1-1][i];
					}
				}
		}
		if(comp==1)
			out_f<<"Case #"<<CasesCount<<": "<<TS<<endl;
		else if(comp>1)
			out_f<<"Case #"<<CasesCount<<": Bad magician!"<<endl;
		else
			out_f<<"Case #"<<CasesCount<<": Volunteer cheated!"<<endl;

	}
	return 0;
}