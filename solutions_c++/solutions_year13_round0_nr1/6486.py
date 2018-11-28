#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int main()
{
	int n,i,j,k,tpr,tpc,incm,pos,flag;
	int winp[10][4]={{0,1,2,3},{4,5,6,7},{8,9,10,11},{12,13,14,15},{0,4,8,12},{1,5,9,13},{2,6,10,14},{3,7,11,15},{0,5,10,15},{3,6,9,12}};
	/*for(i=0;i<10;i++)
	{
		cout<<winp[i][0]<<winp[i][1]<<winp[i][2]<<winp[i][3]<<"\n";
	}*/
	char b[4][4];

	cin>>n;
	for(i=1;i<=n;i++)
	{
		flag=0;
		pos=0;
		incm=0;
		cin>>b[0]>>b[1]>>b[2]>>b[3];
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(b[j][k]=='T')
				{
					tpr=j;
					tpc=k;
					incm=1;
				}
				if(b[j][k]=='.')
				{
					flag=1;
				}
			}
		}

		for(j=0;j<10;j++)
		{
			if(incm)
			{
				b[tpr][tpc]='X';

			}
			//cout<<b[tpr][tpc]<<endl;
			//cout<<
			//cout<<b[(winp[j][0])/4][(winp[j][0])%4]<<(b[(winp[j][1])/4][(winp[j][1])%4])<<(b[(winp[j][2])/4][(winp[j][2])%4])<<(b[(winp[j][3])/4][(winp[j][3])%4])<<" \n";
			if((b[(winp[j][0])/4][(winp[j][0])%4])=='X'&& (b[(winp[j][1])/4][(winp[j][1])%4])=='X'&&(b[(winp[j][2])/4][(winp[j][2])%4])=='X'&&(b[(winp[j][3])/4][(winp[j][3])%4])=='X')
			{
				cout<<"Case #"<<i<<": X won\n";
				pos=1;
				break;
			}
			if(incm)
			{
				b[tpr][tpc]='O';
			}
			if((b[(winp[j][0])/4][(winp[j][0])%4])=='O'&& (b[(winp[j][1])/4][(winp[j][1])%4])=='O'&&(b[(winp[j][2])/4][(winp[j][2])%4])=='O'&&(b[(winp[j][3])/4][(winp[j][3])%4])=='O')
			{
				cout<<"Case #"<<i<<": O won\n";
				pos=1;
				break;
			}
		}
		if(flag==1 && pos==0)
		{
			cout<<"Case #"<<i<<": Game has not completed\n";
		}
		if (flag==0&&pos==0)
		{
			cout<<"Case #"<<i<<": Draw\n";
		}


	}
}