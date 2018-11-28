#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;


int check_row(char a[4][4],int cur)
{
	int x,o;
	x = o = 0;
	for(int i=0;i<4;i++)
	{
		if(a[cur][i] == 'X')
		{
			x++;
		}
		else if(a[cur][i] == 'O')
		{
			o++;
		}
		else if(a[cur][i] == 'T')
		{
			x++;
			o++;
		}
		else
		{
			//....
		}
	}
	if(x == 4) return 1;//x win
	else if (o == 4) return -1;//o win
	else return 0;//continue
}

int check_column(char a[4][4],int cur)
{
	int x,o;
	x = o = 0;
	for(int i=0;i<4;i++)
	{
		if(a[i][cur] == 'X')
		{
			x++;
		}
		else if(a[i][cur] == 'O')
		{
			o++;
		}
		else if(a[i][cur] == 'T')
		{
			x++;
			o++;
		}
		else
		{
			//......
		}
	}
	if(x == 4) return 1;//x win
	else if (o == 4) return -1;//o win
	else return 0;//continue

}

int check_xie(char a[4][4])
{
	int x,o;
	x = o = 0;
	for(int i=0;i<4;i++)
	{
		if(a[i][i] == 'X')
		{
			x++;
		}
		else if(a[i][i] == 'O')
		{
			o++;
		}
		else if(a[i][i] == 'T')
		{
			x++;o++;
		}
		else
		{
			//.......
		}
	}
	if(x == 4) return 1;//x win
	if(o == 4) return -1;//o win
	
	x = o = 0;
	for(int i=0;i<4;i++)
	{
		if(a[i][3-i] == 'X')
		{
			x++;
		}
		else if(a[i][3-i] == 'O')
		{
			o++;
		}
		else if(a[i][3-i] == 'T')
		{
			x++;o++;
		}
		else
		{
			//.......
		}
	}
	if(x == 4) return 1;//x win
	else if(o == 4) return -1;//o win
	else return 0;//continue
}

int main()
{
	int test,ans;
	int row_ans,column_ans,xie_ans;
	int not_fill_flag;
	char a[4][4];
	cin>>test;
	for(int ll=0;ll<test;ll++)
	{
		//init
		ans = 0;
		row_ans = column_ans = xie_ans = 0;
		not_fill_flag = 0;
		//input
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) {cin>>a[i][j];}
		for(int i=0;i<4;i++)
		{
			row_ans = check_row(a,i);
			column_ans = check_column(a,i);
			
			if(row_ans == 1 || column_ans == 1)
			{
				ans = 1;
				break;
			}
			else if(row_ans == -1 || column_ans == -1)
			{
				ans = -1;
				break;
			}

		}
		xie_ans = check_xie(a);
		if(xie_ans == 1) ans = 1;
		else if(xie_ans == -1) ans = -1;
		else {}

		if(ans == 1) {cout<<"Case #"<<ll+1<<": X won"<<endl<<endl;}
		else if (ans == -1) {cout<<"Case #"<<ll+1<<": O won"<<endl<<endl;}
		else 
		{
			for(int i=0;i<4;i++) 
			{
				for(int j=0;j<4;j++)
				{
					if(a[i][j] == '.')
					{
						not_fill_flag++;
					}
				}
			}
			if(not_fill_flag == 0) cout<<"Case #"<<ll+1<<": Draw"<<endl<<endl;
			else cout<<"Case #"<<ll+1<<": Game has not completed"<<endl<<endl;
		}
	}
	return 1;
}