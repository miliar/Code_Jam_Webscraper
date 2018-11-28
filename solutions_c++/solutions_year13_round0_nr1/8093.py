#include<iostream>
#include<fstream>
using namespace std;
	
	
class clas{
public:
int g,r,c,count,uf;
char T[4][4],z;
bool gm;


void read(ifstream& in,ofstream& out)
{
	in>>g;
	
	for(int i=0;i<g;i++)
	{
		gm=true;uf=0;
		this->chkgame(in);
		if(!gm && z!='.')
		{
		 out<<"Case #"<<i+1<<": "<<z<<" won"<<endl;
		}
		else if(uf==0)
		{
		out<<"Case #"<<i+1<<": Draw"<<endl;
		}
		else
		{
		out<<"Case #"<<i+1<<": Game has not completed"<<endl;
		}
	}


}

void chkgame(ifstream& in)
{
	for(int i=0;i<4;i++)
	{
	 for(int j=0;j<4;j++)
	 {count=0;r=0;c=0;
	 in>>T[i][j];
	 if(!(T[i][j]=='X'||T[i][j]=='O'||T[i][j]=='T'))
	 {
	 uf++;
	 }
	 }
	}

	for(;r<4 &&gm==true;r++)
	{
		count=0;
		z=T[r][0];
	 chkrow();
	}

	for(;c<4 &&gm==true;c++)
	{   count=0;
		z=T[0][c];
	 chkcol();
	}
	
	
	if(gm)
	{  count=0;
		z=T[0][0];
		for(int j=1;j<4;j++)
		{
			if(T[j][j]==z||T[j][j]=='T')
			{
			count++;
			}
		}
	if(count==3)
		gm=false;
	}

	if(gm)
	{  count=0;
		z=T[0][3];
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(i+j==3)
			{
			if(T[i][j]==z||T[i][j]=='T')
			{
			count++;
			}
			}
		}
	if(count==4)
		gm=false;
	}
	
}

void chkcol()
{
	for(int j=1;j<4;j++)
		{
			if(T[j][c]==z||T[j][c]=='T')
			{
			count++;
			}
		}
	if(count==3)
		gm=false;
}
void chkrow()
{
	for(int j=1;j<4;j++)
		{
			if(T[r][j]==z||T[r][j]=='T')
			{
			count++;
			}
		}
	if(count==3)
		gm=false;
}

};

int main()
{
	ifstream in;
	ofstream out;
	clas a;
	in.open("input.in",ios::binary);
	out.open("output.in",ios::out);

	a.read(in,out);

system("pause");
return 0;
}