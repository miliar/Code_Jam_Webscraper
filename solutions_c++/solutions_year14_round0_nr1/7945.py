#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

void solve(istream&,int, int[][4],int[]);
int main()
{

	string s;
	std::ifstream is("A-small-attempt1.in",std::ios::in);
	std::ofstream os("OutputFile");
	//cout<<"Enter file name"<<endl;
	//cin >> fileName;
	vector<int> Output;
	int Grid[4][4];
	int mat[4][4],mat2[4][4];
	int T,i=0,j;
	int count[16],numCount;
	int row,number;
	is >>T;
	i=0;
	while (i <T)
	{
	 for ( j=0 ; j<16; j++)
		count[j]=0;
	 is >>row;
	 solve (is,row-1,mat,count); 
	 is >> row;
	 solve(is,row-1,mat,count);
	 i++;
	 numCount =0;
	 for ( int j=0 ; j < 16 ;j++)
		if(count[j] ==2)
			{
			  numCount++;
			  number = j+1;
			} 
			
	if(numCount ==1)
		Output.push_back(number);
	else if(numCount == 0)
		Output.push_back(-1);
	else
		Output.push_back(-2);
			
	}

	for ( i =0 ; i<  T ; i++)
	   {
		os <<"Case #"<<i+1<<": "; 
		if( Output[i] == -2)
			os<<"Bad magician!"<<endl;
		else if(Output[i]==-1)
			os<<"Volunteer cheated!"<<endl;
		else
			os<<Output[i]<<endl;
		}
			
}	


void solve(istream &is,int row, int mat[4][4],int count[16])
{
	for( int i =0 ; i < 4; i++)
	 for ( int j=0; j<4; j++)
	 is>> mat[i][j];
	for(int j=0;j<4;j++)
	  count[mat[row][j]-1]++;   	
}