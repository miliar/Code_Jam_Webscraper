#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int caseNum;
char data[4][4];
int iscomplete;//0表示没完成，1表示完成
int xtag,otag;//分别用来表示x,o是否赢
void solve();//用来初始化xtag,otag,iscomplete这些量用来得到最后的结果
int main(int argc,char *argv[])
{
	int i,j,k;
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);

	cin>>caseNum;
	for(i=1;i<=caseNum;i++)
	{
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>data[j][k];
			}
		}
		iscomplete=1;
		xtag=-1;
		otag=-1;
		solve();
		if(xtag==1)
		{
			cout<<"Case #"<<i<<":"<<" "<<"X won"<<endl;
		}
		else if(otag==1)
		{
			cout<<"Case #"<<i<<":"<<" "<<"O won"<<endl;
		}
		else if(iscomplete==1)
		{
			cout<<"Case #"<<i<<":"<<" "<<"Draw"<<endl;
		}
		else
			cout<<"Case #"<<i<<":"<<" "<<"Game has not completed"<<endl;
	}
	return 0;
}

void solve()
{
	int i,j,k;
	//用来初始化,iscomplete
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(data[i][j]=='.')
			{
				iscomplete=0;//表示没完
			}
			if(iscomplete==0)
				break;//停止外循环
		}
	}
	//判断一到4行是否满足题中赢的条件
	for(i=0;i<4;i++)
	{
		char e=data[i][0];
		if(e=='.')
			continue;
		if(e=='T')
			e=data[i][1];
		else
		{
			j=0;
			while((data[i][j]==e || data[i][j]=='T')&&j<4)
				j++;
			if(j==4)
			{
				if(e=='O')
				{
					otag=1;
					return;
				}
				else if(e=='X')
				{
					xtag=1;
					return;
				}
			}
		}
	}
	//判断4列是否满足情况
	for(j=0;j<4;j++)
	{
		char e=data[0][j];
		if(e=='.')
			continue;
		if(e=='T')
			e=data[1][j];
		i=0;
		while((data[i][j]==e||data[i][j]=='T')&&i<4)
			i++;
		if(i==4)
		{
			if(e=='O')
			{
				otag=1;
				return;
			}
			else if(e=='X')
			{
				xtag=1;
				return;
			}
		}
	}
	//判断从左上到右下是否满足情况
	char e=data[0][0];
	if(e=='.')
	{
	}
	if(e=='T')
		e=data[1][1];
	if(e!='.')
	{
		i=0;j=0;
		while((data[i][j]==e||data[i][j]=='T')&&i<4&&j<4)
		{
			i++;
			j++;
		}
		if(i==4&&j==4)
		{
			if(e=='O')
			{
				otag=1;
				return;
			}
			else if(e=='X')
			{
				xtag=1;
				return;
			}
		}
	}
	//判断从左下到右上是否满足情况
	//cout<<"到着了"<<endl;
	e=data[3][0];
	if(e=='.')
	{
		return;
	}
	if(e=='T')
	{
		e=data[2][1];
	}
	i=3;
	j=0;
	while((data[i][j]==e||data[i][j]=='T')&&j<4)
	{
		i--;
		j++;
		//cout<<".........."<<endl;
	}
	if(j==4)
	{
		if(e=='O')
		{
			otag=1;
			return;
		}
		else if(e=='X')
		{
			xtag=1;
			return;
		}
	}
}
