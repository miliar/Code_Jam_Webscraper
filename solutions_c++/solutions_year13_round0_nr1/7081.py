#include<string>
#include<iostream>
using namespace std;
int main()
{
	string str[4];
	int t;

	cin>>t;
	for(int tc=1; tc<=t; tc++)
	{
		for(int i=0;i<4;i++)
		{
		cin>>str[i];
		}		
		int w=0;
		for(int i=0; i<4; i++)
		{
			int x=0;
			for(int j=0; j<4; j++)
			if(str[i][j]=='X' || str[i][j]=='T')
			x++;
			if(x==4) { w=1; break; }
			x=0;
			for(int j=0; j<4; j++)
			if(str[j][i]=='X' || str[j][i]=='T')
			x++;
			if(x==4) { w=1; break; }
		}
		for(int i=0; i<4; i++)
		{
			int o=0;
			for(int j=0; j<4; j++)
			if(str[i][j]=='O' || str[i][j]=='T')
			o++;
			if(o==4) { w=-1; break; }
			o=0;
			for(int j=0; j<4; j++)
			if(str[j][i]=='O' || str[j][i]=='T')
			o++;			
			if(o==4) { w=-1; break; }
		}
		int i;
		for(i=0; i<4; i++)
		if(!(str[i][i]=='X' || str[i][i]=='T'))
		break;
		if(i==4) w=1;
		for(i=0; i<4; i++)
		if(!(str[i][3-i]=='X' || str[i][3-i]=='T'))
		break;		
		if(i==4) w=1;
		for(i=0; i<4; i++)
		if(!(str[i][i]=='O' || str[i][i]=='T'))
		break;
		if(i==4) w=-1;
		for(i=0; i<4; i++)
		if(!(str[i][3-i]=='O' || str[i][3-i]=='T'))
		break;		
		if(i==4) w=-1;		
		if(w==1)
		cout<<"Case #"<<tc<<": X won\n";
		else if(w==-1)
		cout<<"Case #"<<tc<<": O won\n";
		else 
		{
			for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			if(str[i][j]=='.') { w=2; i=j=4; }
			if(w==2)
			cout<<"Case #"<<tc<<": Game has not completed\n";
			else
			cout<<"Case #"<<tc<<": Draw\n";
		}
	}
	return 0;
}