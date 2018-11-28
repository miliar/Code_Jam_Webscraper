#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
using namespace std;

string tabla[5];

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("output.out","w",stdout);

	int n;

	cin>>n;

//	char ss;
	for(int caso = 1; caso <=n; caso++)
	{

		for(int i = 0; i <4; i++)
			cin>>tabla[i];
	
	//	if(caso!=6)cin>>ss;

		//for(int i = 0; i < 4; i++)
		//	cout<<tabla[i]<<endl;

		int cxh, coh, cxv,cov,cx1=0,co1=0,cx2=0,co2=0;
		bool ban=false;	
		int cp = 0;	

		int win=-1;

		for(int i = 0 ; i < 4; i++)
		{
			cxh=0;coh=0;cxv=0;cov=0;
			for(int j = 0; j < 4; j++)
			{
				if(tabla[i][j] == 'X')cxh++;
				else if(tabla[i][j] == 'O')coh++;
				else if(tabla[i][j] == 'T'){coh++;cxh++;}
				else cp++;		


				if(tabla[j][i] == 'X')cxv++;
				else if(tabla[j][i] == 'O')cov++;
				else if(tabla[j][i] == 'T'){cov++;cxv++;}

		
				if(i==j)
				{
					if(tabla[j][i] == 'X')cx1++;
					else if(tabla[j][i] == 'O')co1++;
					else if(tabla[j][i] == 'T'){co1++;cx1++;}
				}

				if(i+j == 3)
				{
					if(tabla[i][j] == 'X')cx2++;
					else if(tabla[i][j] == 'O')co2++;
					else if(tabla[i][j] == 'T'){co2++;cx2++;}
				}
				

			}
			if(cxh == 4 || cxv==4){ban=true;win=1;}
			else if(coh == 4 || cov==4){ban = true;win=2;}
		}

		if(cx1 == 4 || cx2==4){ban=true;win=1;}
		else if(co1 == 4 || co2==4){ban = true;win=2;}			

		if(ban)
		{
			if(win==1)cout<<"Case #"<<caso<<": X won"<<endl;
			if(win==2)cout<<"Case #"<<caso<<": O won"<<endl;			 
		}else
		{
			if(cp==0)cout<<"Case #"<<caso<<": Draw"<<endl;
			else cout<<"Case #"<<caso<<": Game has not completed"<<endl;
		}
	}


	return 0;
}
