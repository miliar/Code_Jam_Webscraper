#include <iostream>

using namespace std;
char board[5][5];
int lookDown(int k);
int lookLDiag();
int lookRDiag();
int lookRight(int j);
int lookRight(int j)
	{
		int i,count=0;
		if(board[j][0] == '.')
			return 0;
		if(board[j][0] == 'T')
			count++;
		for(i=1;i<4;i++)
		{
			if(board[j][i] == '.')
				return 0;
			if(board[j][i] == 'T')
			{
				count++;
				if(count>1)
					return 0;
			}
			if(board[j][i]!=board[j][i-1])
			{
			if(board[j][i]=='T' || board[j][i-1]=='T')
				continue;
			else
				return 0;
			}
		}
		return 1;
	}
int lookDown(int k)
	{
		int i,count=0;
		if(board[0][k] == '.')
			return 0;
		if(board[0][k] == 'T')
			count++;
		for(i=1;i<4;i++)
		{
			if(board[i][k] == '.')
				return 0;
			if(board[i][k] == 'T')
			{
				count++;
				if(count>1)
					return 0;
			}
			if(board[i][k]!=board[i-1][k])
			{
			if(board[i][k]=='T' || board[i-1][k]=='T')
				continue;
			else
				return 0;
			}
		}
		return 1;
	}
int lookRDiag()
	{
		int i,count=0;
		if(board[0][0] == '.')
			return 0;
		if(board[0][0] == 'T')
			count++;
		for(i=1;i<4;i++)
		{
			if(board[i][i] == '.')
				return 0;
			if(board[i][i] == 'T')
			{
				count++;
				if(count>1)
					return 0;
			}
			if(board[i][i]!=board[i-1][i-1])
			{
			if(board[i][i]=='T' || board[i-1][i-1]=='T')
				continue;
			else
				return 0;
			}
		}
		return 1;
	}
int lookLDiag()
	{
		int i,j,count=0;
		if(board[0][3] == '.')
			return 0;
		if(board[0][3] == 'T')
			count++;
		for(i=1,j=2;i<4,j>=0;i++,j--)
		{
		if(board[i][j] == '.')
			return 0;
		if(board[i][j] == 'T')
		{
			count++;
			if(count>1)
				return 0;
		}
		if(board[i][j]!=board[i-1][j+1])
		{
			if(board[i][j]=='T' || board[i-1][j+1]=='T')
				continue;
			else
				return 0;
		}
		}
		return 1;
	}

int main()
{
    int i,j,k,n,flag,dot,out;
    cin >> n;
    for(i=0;i<n;i++)
		{
			out=0;
			flag=0;
			dot=0;
			for(j=0;j<4;j++)
			{
				for(k=0;k<4;k++)
					{
					    cin >> board[j][k];
					    if(board[j][k] == '.')
                          			  dot=1;
					}
			}
			if(lookRDiag())
				{
					j=0;
					k=0;
					if(board[0][0] == 'T')
					{
						j=1;
						k=1;
					}
					cout << "Case #" << (i+1) << ": " << board[j][k] << " won" << endl;
		                        flag = 1;
					continue;
				}
           		 else if(lookLDiag())
				{
					j=0;
					k=3;
					if(board[0][3] == 'T')
					{
						j=3;
						k=0;
					}
					cout << "Case #" << (i+1) << ": " << board[j][k] << " won" << endl;
					continue;
				}
			for(j=0;j<4;j++)
			{
				if(lookRight(j))
				{
					k=0;
					if(board[j][k] == 'T')
						k++;
					cout << "Case #" << (i+1) << ": " << board[j][k] << " won" << endl;
					flag = 1;
					break;
				}
				else if(lookDown(j))
				{
					k=0;
					if(board[k][j] == 'T')
						k++;
					cout << "Case #" << (i+1) << ": " << board[k][j] << " won" << endl;
					flag = 1;
					break;
				}
			}
			if(flag==0)
           		{
		                if(dot==0)
                		    cout << "Case #" << (i+1) << ": " << "Draw" << endl;
                		else
                		    cout << "Case #" << (i+1) << ": " << "Game has not completed" << endl;
            		}
		}
    return 0;
}
