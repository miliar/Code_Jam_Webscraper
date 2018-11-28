#include <fstream>

using namespace std;

bool b_IsValid[100][100];
int i_In[100][100];
int i_N, i_M;

ifstream f_In ("C:/Users/SHERMAL/Desktop/B-large.in");
ofstream f_Out ("C:/Users/SHERMAL/Desktop/out.txt");
  
void ExamineRows();
void ExamineCols();
void init();
void CheckValid(int iCaseNo);

int main(int argc, char* argv[])
{
	
	if (f_In.is_open())
	{

		init();
		f_In.close();
	}

	f_Out.close();

	return 0;
}

void init(){
	int iT;
	int iCaseNo = 0;

	f_In >> iT;

	while (iT > 0)
	{

		--iT;
		++iCaseNo;

		f_In >> i_N;
		f_In >> i_M;

		//inputs
		for (int i = 0; i < i_N; i++)
		{
			for (int j = 0; j < i_M; j++)
			{
				f_In >> i_In[i][j];
			}
		}

		for (int i = 0; i < i_N; i++)
		{
			for (int j = 0; j < i_M; j++)
			{
				b_IsValid[i][j] = false;
			}
		}

		ExamineRows();

		ExamineCols();

		CheckValid(iCaseNo);

	}
}

void CheckValid(int iCaseNo)
{

	for (int i = 0; i < i_N; i++)
	{
		for (int j = 0; j < i_M; j++)
		{
			if ( ! b_IsValid[i][j] )
			{
				f_Out << "Case #" << iCaseNo << ": " << "NO" << endl;
				return;
			}
		}
	}	

	f_Out << "Case #" << iCaseNo << ": " << "YES" << endl;	
}

void ExamineRows()
{

	for (int i = 0; i < i_N; i++)
	{
		int iMax = 0;

		for (int j = 0; j < i_M; j++)
		{
			if ( iMax < i_In[i][j] )
			{
				iMax = i_In[i][j];
			}
		}

		for (int j = 0; j < i_M; j++)
		{
			if ( b_IsValid[i][j] )
			{
				continue;
			}

			if ( i_In[i][j] == iMax )
			{
				b_IsValid[i][j] = true;
			}
			else
			{
				b_IsValid[i][j] = false;
			}
		}
	}
}




void ExamineCols()
{
	
	for (int j = 0; j < i_M; j++)
	{
		int iMax = 0;

		for (int i = 0; i < i_N; i++)
		{
			if ( iMax < i_In[i][j] )
			{
				iMax = i_In[i][j];
			}
		}

		for (int i = 0; i < i_N; i++)
		{
			if ( b_IsValid[i][j] )
			{
				continue;
			}

			if ( i_In[i][j] == iMax )
			{
				b_IsValid[i][j] = true;
			}
			else
			{
				b_IsValid[i][j] = false;
			}
		}
	}
}
