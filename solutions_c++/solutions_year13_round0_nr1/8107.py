#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int caseNum;
char data[4][4];
int iscomplete;//0��ʾû��ɣ�1��ʾ���
int xtag,otag;//�ֱ�������ʾx,o�Ƿ�Ӯ
void solve();//������ʼ��xtag,otag,iscomplete��Щ�������õ����Ľ��
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
	//������ʼ��,iscomplete
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(data[i][j]=='.')
			{
				iscomplete=0;//��ʾû��
			}
			if(iscomplete==0)
				break;//ֹͣ��ѭ��
		}
	}
	//�ж�һ��4���Ƿ���������Ӯ������
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
	//�ж�4���Ƿ��������
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
	//�жϴ����ϵ������Ƿ��������
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
	//�жϴ����µ������Ƿ��������
	//cout<<"������"<<endl;
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
