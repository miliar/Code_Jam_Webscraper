#include <iostream>
#include <fstream>
using namespace std;

bool JudgeAvailible(int** pattern,bool** &valid, int width, int length);
void destructor(int** &pointer,int width);
void destructor(bool** &pointer,int width);
int main(int argc,char* argv[])
{
	ifstream fin(argv[1]);
	ofstream fout("Lawnmower.out");

	int counter;
	fin>>counter;
	int width,length;
	for(int i=0;i<counter;i++)
	{
		fin>>width>>length;
		int** pattern=new int*[width];
		bool** valid=new bool*[width];
		for(int j=0;j<width;j++)
		{
			pattern[j]=new int[length];
			valid[j]=new bool[length];
		}	
        for(int j=0;j<width;j++)
			for (int k = 0; k < length; ++k)
			{
				fin>>pattern[j][k];
				valid[j][k]=false;
			}	
		bool Result=JudgeAvailible(pattern,valid,width,length);
		fout<<"Case #"<<(i+1)<<": ";
		if(Result)
			fout<<"YES"<<endl;
		else
			fout<<"NO"<<endl;
		destructor(pattern,width);
		destructor(valid,width);
	}
	return 0;
}

bool _JudgeColumn(int** pattern, int width,int Cindex)
{
	bool result=true;
	int value=pattern[0][Cindex];
	for (int i = 1; i < width; ++i)
	{
		if(pattern[i][Cindex]!=value)
		{
			result=false;
			break;
		}
	}
	return result;
}

void _ValidicateColumn(bool** &valid, int width,int Cindex)
{
	for (int i = 0; i < width; ++i)
	{
		valid[i][Cindex]=true;
	}
}
bool _JudgeRow(int** pattern, int length,int Rindex)
{
	bool result=true;
	int value=pattern[Rindex][0];
	for (int i = 1; i < length; ++i)
	{
		if(pattern[Rindex][i]!=value)
		{
			result=false;
			break;
		}
	}
	return result;
}

void _ValidicateRow(bool** &valid, int length,int Rindex)
{
	for (int i = 0; i < length; ++i)
	{
		valid[Rindex][i]=true;
	}
}
bool JudgeAvailible(int** pattern,bool** &valid,int width, int length)
{
	bool result=true;
	if(width==1||length==1) return result;
	for (int i = 0; i < width; ++i)
	{
		for (int j = 0; j < length; ++j)
		{
			if(valid[i][j]) continue;
			if(pattern[i][j]==1)
			{
				if(_JudgeRow(pattern,length,i)&&_JudgeColumn(pattern,width,j))
				{
					_ValidicateColumn(valid,width,j);
					_ValidicateRow(valid,length,i);
					continue;
				}
				else if(_JudgeColumn(pattern,width,j))
				{
					_ValidicateColumn(valid,width,j);
					continue;
				}
				else if(_JudgeRow(pattern,length,i))
				{
					_ValidicateRow(valid,length,i);
					continue;
				}
				else
				{
					result=false;
					return result;
				}
			}
		}
	}
	return result;
}

void destructor(int** &pointer,int width)
{
	for(int i=0;i<width;i++)
		delete pointer[i];
	delete pointer;
}

void destructor(bool** &pointer,int width)
{
	for(int i=0;i<width;i++)
		delete pointer[i];
	delete pointer;
}
