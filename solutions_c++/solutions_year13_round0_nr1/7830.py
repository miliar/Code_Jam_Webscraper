#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("A-large.in","r", stdin);
	freopen("answer.out","w", stdout);
	bool check=true;
	int m=0;
	int raodxst=0,raodxsv=0, raodost=0, raodosv=0, raodw=0;
	int n;
	cin>>n;
	for(int k=1; k<=n; k++)
	{
		check=false;
	char mas[4][4];
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			cin>>mas[i][j];
	for(int i=0; i<4; i++)
	{
		if(mas[i][i]=='X')
			raodxst++;
		else if(mas[i][i]=='O')
			raodost++;
		else if(mas[i][i]=='T')
			{
				raodxst++; raodost++;
			}
		if(mas[i][3-i]=='X')
			raodxsv++;
		else if(mas[i][3-i]=='O')
			raodosv++;
		else if(mas[i][3-i]=='T')
			{
				raodxsv++; raodosv++;
			}
	}
	if(raodxst==4||raodxsv==4)
	{
		cout<<"Case #"<<k<<": X won"<<endl;
		raodxsv=raodxst=0;
		raodosv=raodost=0;
		raodw=0;
		continue;
	}
	
	else if(raodost==4||raodosv==4)
	{
		cout<<"Case #"<<k<<": O won"<<endl;
		raodxsv=raodxst=0;
		raodosv=raodost=0;
		raodw=0;
		continue;
	}
	raodxsv=raodxst=0;
	raodosv=raodost=0;	
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(mas[i][j]=='X')
				raodxst++;
			else if(mas[i][j]=='O')
				raodost++;
			else if(mas[i][j]=='T')
			{
				raodxst++; raodost++;
			}
			else raodw++;
			if(mas[j][i]=='X')
				raodxsv++;
			else if(mas[j][i]=='O')
				raodosv++;
			else if(mas[j][i]=='T')
			{
				raodxsv++; raodosv++;
			}
			else raodw++;
		}
		if(raodxst==4||raodxsv==4)
		{
			cout<<"Case #"<<k<<": X won"<<endl;
			raodxst=raodxsv=0;
		raodost=raodosv=0;
		raodw=0;
			check=true;
			break;
			
		}
		else if(raodost==4||raodosv==4)
		{
			cout<<"Case #"<<k<<": O won"<<endl;
			raodxst=raodxsv=0;
		raodost=raodosv=0;
		    raodw=0;
			check=true;
			break;
			
		}
		raodxst=raodxsv=0;
		raodost=raodosv=0;
	}
	if(check) continue;
	if(raodw==0)
	{
		raodxst=raodxsv=0;
		raodost=raodosv=0;
		cout<<"Case #"<<k<<": Draw"<<endl;
	}
	else
	{
		raodxst=raodxsv=0;
		raodost=raodosv=0;
		cout<<"Case #"<<k<<": Game has not completed"<<endl;
	}
	raodw=0;
   }
	return 0;
}