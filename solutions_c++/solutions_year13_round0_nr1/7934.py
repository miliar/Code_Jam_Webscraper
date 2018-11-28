#include <iostream>
#include <string>
#include <vector>
using namespace std;
char busq(vector <string> &tab)
{
	bool win=true;
	char diag=tab[0][0];
	for(int i=1;i<4;i++)
	{
		if((tab[i][i]!=diag) and (tab[i][i]!='T')) win=false;
	}
	if(win) return diag;
	win=true;
	diag=tab[0][3];
	for(int i=1;i<4;i++)
	{
		if(tab[i][3-i]!=diag and tab[i][3-i]!='T') win=false;
	}
	if(win) return diag;
	win=true;
	for(int i=0;i<4;i++)//horiz
	{
		char hor=tab[i][0];
		for(int j=1;j<4;j++)
		{
			if((tab[i][j]!=hor) and (tab[i][j]!='T')) win=false;
		}
		if(win) return hor;
		win=true;
	}
	for(int i=0;i<4;i++)//ver
	{
		char ver=tab[0][i];
		for(int j=1;j<4;j++)
		{
			if(tab[j][i]!=ver and tab[j][i]!='T') win=false;
		}
		if(win) return ver;
		win=true;
	}
		for(int i=0;i<4;i++)//.
	{
		for(int j=0;j<4;j++)
			if(tab[i][j]=='.') return '.';
	}
	return 'd';
}
int main()
{
	int t;
	cin >>t;
	string str;
	getline(cin,str);
	for(int i=0; i<t;i++)
	{
		vector<string> tab (4,"0000");
		for(int j=0; j<4;j++)
			getline(cin,tab[j]);
		getline(cin,str);
		char res = busq (tab);
		cout <<"Case #" <<i+1 <<": ";
		if(res=='.') cout <<"Game has not completed" <<endl;
		else if(res=='X') cout <<"X won" <<endl;
		else if(res=='O')cout <<"O won" <<endl;
		else if(res=='d') cout <<"Draw" <<endl;
	}
	return 0;
}
