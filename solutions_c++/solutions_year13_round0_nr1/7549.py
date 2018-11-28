#include <cstdio>
#include <iostream>
using namespace std;

int licz;
char t[5][5];

bool wiersz(int lp, char znak)
{
	licz=0;
	for(int r=0; r<4; r++)
		if(t[lp][r]==znak || t[lp][r]=='T') licz++;
	if(licz==4) return true;
	return false;
}

bool kolumna(int lp, char znak)
{
	licz=0;
	for(int r=0; r<4; r++)
		if(t[r][lp]==znak || t[r][lp]=='T') licz++;
	if(licz==4) return true;
	return false;
}

bool przek(char znak)
{
	licz=0;
	for(int r=0; r<4; r++)
		if(t[r][r]==znak || t[r][r]=='T') licz++;
	if(licz==4) return true;
	licz=0;
	for(int r=0; r<4; r++)
		if(t[r][3-r]==znak || t[r][3-r]=='T') licz++;	
	if(licz==4) return true;
	return false;
}

int main()
{
	int ile;
	cin>>ile;
	for(int i=0; i<ile; i++)
	{
		char result='-';
		bool kon=true;
		for(int j=0; j<4; j++)
		{
			cin>>t[j][0]>>t[j][1]>>t[j][2]>>t[j][3];
			if(t[j][0]=='.' || t[j][1]=='.' || t[j][2]=='.' || t[j][3]=='.')
				kon=false;
		}
		for(int j=0; j<4; j++)
		{
			if(wiersz(j,'X')) result='X';
			if(kolumna(j,'X')) result='X';
			if(przek('X')) result='X';
			if(przek('O')) result='O';
			if(wiersz(j,'O')) result='O';
			if(kolumna(j,'O')) result='O';
		}
		cout<<"Case #"<<(i+1)<<":";
		if(result=='X') cout<<" X won\n";
		else if(result=='O') cout<<" O won\n";
		else if(!kon) cout<<" Game has not completed\n";
		else cout<<" Draw\n";
	}
}
