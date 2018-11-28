#include<iostream>
#include<fstream>
using namespace std;

int check_row(char arr[4][5], int r)
{
	bool incom = false;
	bool ans = true;
	for(int i=0; i<4; i++)
	{
		if(arr[r][i] == '.')
			incom = true;
		if( arr[r][i] != 'X' && arr[r][i] != 'T')
			ans = false;
	}
	if(ans)
		return 1;
		
	ans = true;
	for(int i=0; i<4; i++)
	{
		if(arr[r][i] == '.')
			incom = true;
		if( arr[r][i] != 'O' && arr[r][i] != 'T')
			ans = false;
	}
	if(ans)
		return 2;
	
	if(incom)
		return 0;
	else	
		return -1;
}

int check_col(char arr[4][5], int r)
{
	bool incom = false;
	bool ans = true;
	for(int i=0; i<4; i++)
	{
		if(arr[i][r] == '.')
			incom = true;
		if( arr[i][r] != 'X' && arr[i][r] != 'T')
			ans = false;
	}
	if(ans)
		return 1;
		
	ans = true;
	for(int i=0; i<4; i++)
	{
		if(arr[i][r] == '.')
			incom = true;
		if( arr[i][r] != 'O' && arr[i][r] != 'T')
			ans = false;
	}
	if(ans)
		return 2;
		
	
	if(incom)
		return 0;
	else	
		return -1;
}

int check_dia(char arr[4][5])
{
	bool incom = false;
	bool ans = true;
	for(int i=0; i<4; i++)
	{
		if(arr[i][i] == '.')
			incom = true;
		if( arr[i][i] != 'X' && arr[i][i] != 'T')
			ans = false;
	}
	if(ans)
		return 1;
	ans = true;
	for(int i=0, j=3; i<4; i++, j--)
	{
		if(arr[i][j] == '.')
			incom = true;
		if( arr[i][j] != 'X' && arr[i][j] != 'T')
			ans = false;
	}
	if(ans)
		return 1;
		
	ans = true;
	for(int i=0, j=3; i<4; i++, j--)
	{
		if(arr[i][j] == '.')
			incom = true;
		if( arr[i][j] != 'O' && arr[i][j] != 'T')
			ans = false;
	}
	if(ans)
		return 2;
	ans = true;
	for(int i=0; i<4; i++)
	{
		if(arr[i][i] == '.')
			incom = true;
		if( arr[i][i] != 'O' && arr[i][i] != 'T')
			ans = false;
	}
	if(ans)
		return 2;
		
	if(incom)
		return 0;
	else	
		return -1;
}



int main()
{
	char arr[4][5];
	int t;
	
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");
	
	in>>t;
	for(int x = 1; x<=t; x++)
	{
		for(int i =0; i<4; i++)
			in>>arr[i];
		
		int a = 0;
		for(int i =0; i<4 && a <= 0; i++)
		{
			a = check_row(arr, i);
		}
		
		for(int i =0; i<4 && a <= 0; i++)
		{
			a = check_col(arr, i);
		}
		
		if(a<=0)
			a= check_dia(arr);
		
		switch(a)
		{
			case -1:
				out<<"Case #"<<x<<": Draw"<<endl;
				break;
			case 0:
				out<<"Case #"<<x<<": Game has not completed"<<endl;
				break;
			case 1:
				out<<"Case #"<<x<<": X won"<<endl;
				break;
			case 2:
				out<<"Case #"<<x<<": O won"<<endl;
				break;
				
		}
	}
	return 0;
}

