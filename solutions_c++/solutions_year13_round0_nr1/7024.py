#include<iostream>
#include<fstream>
#include<math.h>
#include<string.h>
using namespace std;

char win(char mat[5][5],char s)
{
	bool notCom = false;
	
	
	for(int i=1;i<5;i++)
	{
		int flag = 0;

		for(int j=1;j<5;j++)
		{
			 if(mat[i][j] == s || mat[i][j] == 'T')
			 {
				 flag++;
			 }
		}
		if(flag == 4)
		{
			return s;
		}
	}

	for(int i=1;i<5;i++)
	{
		int flag = 0;

		for(int j=1;j<5;j++)
		{
			 if(mat[j][i] == s || mat[j][i] == 'T')
			 {
				 flag++;
			 }
		}
		if(flag == 4)
		{
			return s;
		}
	}

	int flag = 0;
	for(int j=1;j<5;j++)
	{
		
		 if(mat[j][j] == s || mat[j][j] == 'T')
		 {
			 flag++;
		 }
	}
	if(flag == 4)
		{
			return s;
		}

	flag = 0;
	for(int j=1;j<5;j++)
	{
		
		 if(mat[j][5-j] == s || mat[j][5-j] == 'T')
		 {
			 flag++;
		 }
	}
	if(flag == 4)
	{
		return s;
	}

	return 'n';
}
bool notcomlete(char mat[5][5])
{
	for(int i=1;i<5;i++)
	{

		for(int j=1;j<5;j++)
		{
			 if(mat[i][j]=='.')
			 {
				 return true;
			 }
		}
	}
	return false;
}
void main()
{

	int T=0;
	ifstream in("A-large.in");
	ofstream save("r1.txt");
	in >> T;
	char s[10];
	in.getline(s,10);
	for(int p=0 ; p<T;p++)
	{
		char mat[5][5];
		bool change = false;
		string re="";

		for(int i=1;i<5;i++)
		{
			char str[10];
			in.getline(str,10);
			for(int j=1;j<5;j++)
			{
				mat[i][j] = str[j-1];
			}
			
		}
		if(win(mat,'X') == 'X')
		{
			save << "Case #"<<p+1<<": "<<"X won" << "\n";
		}
		else if(win(mat,'O') == 'O')
		{
			save << "Case #"<<p+1<<": "<<"O won" << "\n";
		}
		else if(notcomlete(mat))
		{
			save << "Case #"<<p+1<<": "<<"Game has not completed" << "\n";
		}
		else
		{
			save << "Case #"<<p+1<<": "<<"Draw" << "\n";
		}
		in.getline(s,10);
	}
	in.close();
	save.close();
}
