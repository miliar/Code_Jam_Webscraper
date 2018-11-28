
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int GetMax(char da[4][4],int x,int y,int acc,char point)
{
	switch(point)
	{
		case 'L':
			acc++;
			if(x>0&&y<3&&(da[x][y]==da[x-1][y+1]||da[x-1][y+1]=='T'))
			{
				da[x-1][y+1]=da[x][y];
				return GetMax(da,x-1,y+1,acc,'L');
			}
			else
			{
				return acc;
			}
		break;
		case 'S':
			acc++;
			
			if(y<3&&(da[x][y]==da[x][y+1]||da[x][y+1]=='T'))
			{
				da[x][y+1]=da[x][y];
				return GetMax(da,x,y+1,acc,'S');
			}
			else
			{
				return acc;
			}
		break;
		case 'R':
			acc++;
			if(x<3&&y<3&&(da[x][y]==da[x+1][y+1]||da[x+1][y+1]=='T'))
			{
				da[x+1][y+1]=da[x][y];
				return GetMax(da,x+1,y+1,acc,'R');
			}
			else
			{
				return acc;
			}
		break;
		case 'E':
			acc++;
			if(x<3&&(da[x][y]==da[x+1][y]||da[x+1][y]=='T'))
			{
				da[x+1][y]=da[x][y];
				return GetMax(da,x+1,y,acc,'E');
			}
			else
			{
				return acc;
			}
		break;
		case 'C':
			int a1=1,a2=1,a3=1,a4=1;
			
			if(x>0&&y<3)
			{
				if(da[x][y]==da[x-1][y+1]||da[x-1][y+1]=='T')
				{
					da[x-1][y+1]=da[x][y];
					a1=GetMax(da,x-1,y+1,a1,'L');
				}
			}
			if(y<3)
			{
				if(da[x][y]==da[x][y+1]||da[x][y+1]=='T')
				{
					da[x][y+1]=da[x][y];
					a2=GetMax(da,x,y+1,a2,'S');
				}
			}
			if(x<3&&y<3)
			{
				if(da[x][y]==da[x+1][y+1]||da[x+1][y+1]=='T')
				{
					da[x+1][y+1]=da[x][y];
					a3=GetMax(da,x+1,y+1,a3,'R');
				}
			}
			if(x<3)
			{
				if(da[x][y]==da[x+1][y]||da[x+1][y]=='T')
				{
					da[x+1][y]=da[x][y];
					a4=GetMax(da,x+1,y,a4,'E');
				}
			}
			int aa1,aa2;
			aa1=(a1>a2)?a1:a2;
			aa2=(a3>a4)?a3:a4;
			return (aa1>aa2)?aa1:aa2;
	}
	
};
int main()
{
	int T=0,num;
	int Xmax,Omax,cur;
	ifstream fin("A-small-attempt11.in");
	ofstream fout("output.out");
	char data[4][4];
	string ss;
	getline(fin,ss,'\n');
	T=atoi(ss.c_str());
	int p=0;
	string str="";
	while(p<T)
	{
		num=0;
		Xmax=0;
		Omax=0;
		cur=0;
		while(num<4)
		{
			getline(fin,ss,'\n');
			if(ss=="")
			{
				getline(fin,ss,'\n');
			}
			data[num][0]=ss[0];
			data[num][1]=ss[1];
			data[num][2]=ss[2];
			data[num][3]=ss[3];
			num++;
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				switch(data[i][j])
				{
				case 'X':
					cur=GetMax(data,i,j,0,'C');
					if(cur>Xmax)Xmax=cur;
					break;
				case 'O':
					cur=GetMax(data,i,j,0,'C');
					if(cur>Omax)Omax=cur;
					break;
				case 'T':
					data[i][j]='X';
					cur=GetMax(data,i,j,0,'C');
					if(cur>Xmax)Xmax=cur;
					data[i][j]='O';
					cur=GetMax(data,i,j,0,'C');
					if(cur>Omax)Omax=cur;
					data[i][j]='T';
					break;
				}
			}
		}
		string output="";
		if(Xmax>=3||Omax>=3)
		{
			if(Xmax>Omax)
			{
				output="X won";
			}
			else if(Xmax<Omax)
			{
				output="O won";
			}
			else if(Xmax==Omax)
			{
				output="Draw";
			}
		}
		else
		{
			output="Game has not completed";
		}
		fout<<"Case #"<<p+1<<": "<<output<<endl;
		p++;
	}
	fin.close();
	fout.close();
	return 0;
}

