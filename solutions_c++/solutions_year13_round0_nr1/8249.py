// google_code_jam_1.cpp : Defines the entry polong for the console application.
//
#include <iostream>
using namespace std;

class puzzle
{
public:
	char tictac[4][4];
	long no;
	puzzle() 
	{
	}
	void set(char ch[][4], long n)
	{ 
		for(int i = 0; i < 4; i ++)
		{
			for(int j = 0; j < 4; j ++)
			{
				tictac[i][j] = ch[i] [j];
			}
		}
		
		no = n;
      
	}

bool check_rows(char ch)
{
	bool found = false;
	long i = 0;
	long j = 0;
	for (i = 0; i <4; i++)
	{
		for(j = 0; j <4; j++)
		{
			if ((tictac[i][j] == ch)||(tictac[i][j] == 'T'))
			 continue;
			else break;
		}
		if (j == 4) 
		{
			found = true;
			break;
		}
	}
}
bool check_columns(char ch)
{
bool found = false;
	long i = 0;
	long j = 0;
	for (i = 0; i <4; i++)
	{
		for(j = 0; j <4; j++)
		{
			if ((tictac[j][i] == ch)||(tictac[j][i] == 'T'))
			 continue;
			else break;
		}
		if (j == 4) 
		{
			found = true;
			break;
		}
	}
}
bool check_forward_diagonal(char ch)
{
    long i = 0;
	for (i = 0; i <4; i++)
	{
		if((tictac[i][i] == ch) || (tictac[i][i] == 'T'))
			continue;
		else break;
	}
if(i == 4) return true;
else return false;

}

bool check_backward_diagonal(char ch)
{
	long i = 0;
	for (i =0; i <4 ;i++)
	{
		if((tictac[4-i][i] == ch) || (tictac[4-i][i] == 'T'))
			continue;
		else
			break;
	}
	if(i == 4) return true;
else return false;
}
bool verify(char ch)
{
	if((this->check_rows(ch)) || (this->check_columns(ch)) || (this->check_backward_diagonal(ch)) || (this->check_forward_diagonal(ch)))
	
  return true;
	
}
bool isdraw()
{
	bool nodraw = true;
	for(long i = 0; i <4 ;i++)
	{ for(long j = 0; j <4; j++)
	  {
		if(tictac[i][j] == '.')
		{
			nodraw = false;
		}
	  }
	}
}

};
long _tmain(long argc, _TCHAR* argv[])
{
  long n;
  cin>>n;
  
  char ch[4][4];
  puzzle p[50];
  for (long i = 1; i <=n ; i ++)
  {
	  for(long j = 0; j <4 ; j++)
	  {
		  for(long k = 0; k < 4; k++)
		  {
			  cin>>ch[j][k];

		  }
	  }
	  p[i].set(ch, i);
  }

  for(long i = 1; i <=n ;i++)
  {
	  if(p[i].verify('O'))
		  cout<<"Case #"<<i<<": O won";
	  else if(p[i].verify('X'))
	  cout<<"Case #"<<i<<": X won";
	  else if(p[i].isdraw())
	  cout<<"Case #"<<i<<": Draw";
	  else
		  cout<<"Case #"<<i<<": Game has not completed";
  }
getch();
	return 0;
}

