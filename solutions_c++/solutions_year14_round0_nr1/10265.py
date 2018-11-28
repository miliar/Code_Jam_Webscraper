#include <iostream>

#include <fstream>
using namespace std;
int main()
{
	ifstream in("A-small-attempt0.in",ios::in);
	ofstream out("A-small-attempt0.out",ios::out);
	int v1[4][4],v2[4][4];
	int T;
	int Arr1[4],Arr2[4];
	int Ans1,Ans2;
	in>>T;
	int caseCount = 0;
	while(caseCount != T)
	{	
		in>>Ans1;
		for(int i=0;i<4;i++)
		for(int j=0; j<4;j++ )
		{	
			in>>v1[i][j];
		}
	
		for(int k=0; k<4; k++)
		{
			Arr1[k] = v1[Ans1-1][k];
		}
		in>>Ans2;
		for(int i=0;i<4;i++)
		for(int j=0; j<4;j++ )
		{	
			in>>v2[i][j];
		}
	
		for(int k=0; k<4; k++)
		{
			Arr2[k] = v2[Ans2-1][k];
		}
		int count =0;
		int res;
		for(int i=0;i<4;i++)
		for(int k = 0;k<4;k++)
		{
			if(Arr1[i] == Arr2[k])
			{
				count++;
				res=Arr1[i]; 
			}
		}
		caseCount++;
		if(count == 1)
		{
			out<<"Case #"<<caseCount<<": "<<res<<endl;
		}
		else if(count>1)
		{
			out<<"Case #"<<caseCount<<": Bad magician!"<<endl;
		}
		else
		{
			out<<"Case #"<<caseCount<<": Volunteer cheated!"<<endl;
		}					
		
	}
	return 0;
}
