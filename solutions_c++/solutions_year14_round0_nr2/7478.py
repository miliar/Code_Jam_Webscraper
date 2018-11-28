#include<iostream>
#include<fstream>
#include <string>
using namespace std;
void write_txt(int num,int result,int guess_num)		   
{
	ofstream outfile("result.txt",ofstream::out|ofstream::app);
	switch(result)
	{
	case 1:outfile<<"Case #"<<num<<": "<<guess_num<<endl;break;
	case -1:outfile<<"Case #"<<num<<": "<<"Bad magician!"<<endl;break;
	case 0:outfile<<"Case #"<<num<<": "<<"Volunteer cheated!"<<endl;break;
	default:break;
	}
}
void read_line_n(ifstream &infile,int chose1,int *row1)
{
	int temp;
	int k=0;
	for(int i=1;i<=16;i++)
	{
		infile>>temp;
		if(i>=((chose1-1)*4+1)&&i<=chose1*4)
		{
			row1[k]=temp;
			k++;
		}
	}

}
int find_magic( int *row1,int *row2,int &magic)
{
	int result=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(row2[i]==row1[j])
			{
				magic=row2[i];
				result++;
			}
			if(result==0)
				return 0;
			else if(result==1)
				return 1;
			else
				return -1;
}
int main()
{
	ifstream infile("A-small-attempt0.in",ofstream::in);
	int num;int row1[4],row2[4],chose1,chose2;
	infile>>num;
	for(int i=1;i<=num;i++)
	{
		infile>>chose1;
		read_line_n(infile,chose1,row1);
		infile>>chose2;
		read_line_n(infile,chose2,row2);
		int magic,result;
		result=find_magic(row1,row2,magic);
		write_txt(i,result,magic);
	}
	return 0;
}