#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
char c;
int x,o,f;
bool w;
string p;
char s[5][5];
int n;
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin>>n;
	for(int i=1;i<=n;i++)
	{
		if(i!=1){w=false;fout<<endl;f=0;}
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				fin>>s[j][k];
		for(int j=0;j<4;j++)
		{
			x=0;o=0;
			for(int k=0;k<4;k++)
			{
				if(s[j][k]=='X'||s[j][k]=='T')x++;
				if(s[j][k]=='O'||s[j][k]=='T')o++;
				if(s[j][k]=='.')f++;
			}
			if(x==4||o==4){w=true; j=4;}
		}
		if(w)
		{
			if(x==4)fout<<"Case #"<<i<<": X won";
			else fout<<"Case #"<<i<<": O won";
			continue;
		}
		for(int k=0;k<4;k++)
		{
			x=0;o=0;
			for(int j=0;j<4;j++)
			{
				if(s[j][k]=='X'||s[j][k]=='T')x++;
				if(s[j][k]=='O'||s[j][k]=='T')o++;
				if(s[j][k]=='.')f++;
			}
			if(x==4||o==4){w=true;k=4;}
		}
		if(w)
		{
			if(x==4)fout<<"Case #"<<i<<": X won";
			else fout<<"Case #"<<i<<": O won";
			continue;
		}
		x=0;o=0;
		for(int k=0,j=0;k<4,j<4;k++,j++)
		{
				if(s[j][k]=='X'||s[j][k]=='T')x++;
				if(s[j][k]=='O'||s[j][k]=='T')o++;
				if(s[j][k]=='.')f++;
		}
		if(x==4){ fout<<"Case #"<<i<<": X won";continue;}
		if(o==4){ fout<<"Case #"<<i<<": O won";continue;}
		x=0;o=0;
		for(int k=3,j=0;k>=0,j<4;k--,j++)
		{
				if(s[j][k]=='X'||s[j][k]=='T')x++;
				if(s[j][k]=='O'||s[j][k]=='T')o++;
				if(s[j][k]=='.')f++;
		}
		if(x==4){ fout<<"Case #"<<i<<": X won";continue;}
		if(o==4){ fout<<"Case #"<<i<<": O won";continue;}
		if(f){ fout<<"Case #"<<i<<": Game has not completed";continue;}
		fout<<"Case #"<<i<<": Draw";continue;
	}
	return 0;
}