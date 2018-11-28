#include<iostream>

using namespace std;

char win(char c[4][4])
{
	int set_chars=0;
	int won=0;
	int empty = 0;
	for(int i=0;i<4;i++)
	{
		
		char prev_char='*';
		
		int count=0;
		
		prev_char = c[i][0];
		int j=0;
		for(j=1;j<4;j++ )
		{
			if(prev_char == '.')
			{
				prev_char = c[i][j];
				empty =1;
			}
			else
			{
				set_chars++;
				if(prev_char == c[i][j]  )
				{
					count++;
				}
				else if( c[i][j]=='T')
				{
					count++;
				}
				else if(prev_char == 'T')
				{
					count++;
					prev_char = c[i][j];
				}
				
			}
		}
		if(c[i][j] != '.')
			set_chars++;
		else
			empty = 1;
		if(count == 3)
		{
			won =1;
			
			return prev_char;
		}
		count =0;
	}
	
	for(int i=0;i<4;i++)
	{
		int won=0;
		char prev_char='*';
		
		int count=0;
		
		prev_char = c[0][i];
		int j=0;
		for( j=1;j<4;j++ )
		{
			if(prev_char == '.')
				prev_char = c[j][i];
			else
			{
				
				if(prev_char == c[j][i]  )
				{
					count++;
				}
				else if( c[j][i]=='T')
				{
					count++;
				}
				else if(prev_char == 'T')
				{
					count++;
					prev_char = c[j][i];
				}
				
			}
		}
		if(c[j][i] != '.')
			;
		if(count == 3)
		{
			won =1;
			
			return prev_char;
		}
		count =0;
	}
	
	char prev_char =c[0][0];
	int count =0;
	for(int j=1;j<4;j++ )
		{
			if(prev_char == '.')
				prev_char = c[j][j];
			else
			{
				
				if(prev_char == c[j][j]  )
				{
					count++;
				}
				else if( c[j][j]=='T')
				{
					count++;
				}
				else if(prev_char == 'T')
				{
					count++;
					prev_char = c[j][j];
				}
				
			}
		}
		if(count == 3)
		{
			
			return prev_char;
		}
		
		count = 0;
		prev_char =c[3][0];
		for(int j=1;j<4;j++ )
		{
			if(prev_char == '.')
				prev_char = c[3-j][j];
			else
			{
				
				if(prev_char == c[3-j][j]  )
				{
					count++;
				}
				else if( c[3-j][j]=='T')
				{
					count++;
				}
				else if(prev_char == 'T')
				{
					count++;
					prev_char = c[3-j][j];
				}
				
			}
		}
		if(count == 3)
		{
			
			return prev_char;
		}
		
		
		
		
		
		if(won == 0 && empty == 0)
			return 'd';
		else 
			return '.';
		
	
}
int main()
{
	int t;
	char c[4][4];
	cin >>t;
	for(int i=0; i<t;i++)
	{
		for(int j=0 ; j<4;j++)
		{
			for(int k=0 ; k<4;k++)
			{
				cin>>c[j][k];
			}
			
		}
		cout<<"Case #"<<i+1<<": ";
		char res = win(c);
		if(res =='X' || res=='O')
		{
			cout<<res<<" won"<<endl;
		}
		else if(res == 'd')
			cout<<"Draw"<<endl;
		else if(res == '.')
			cout<<"Game has not completed"<<endl;
			
		
	}
	return 0;
}
