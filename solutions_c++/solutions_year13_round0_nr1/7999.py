#include <iostream>
#include <fstream>
using namespace std;
char map[4][4];
int num[4][4];
ifstream fin("A-small-attempt0.in");
ofstream fout("output.out");
int main()
{
	int t;
	fin>>t;
	int index;
	for(index=1;index<=t;++index)
	{
		int i,j;
		int flag=0;
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				fin>>map[i][j];
				if(map[i][j]=='.')
					flag=1;
			}
		}

		char ch;
		int count;
		int ok=0;
		for(i=0;i<4;++i)
		{
			count=1;
			ch=map[i][0];
			for(j=1;j<4;++j)
			{
				if(map[i][j]!='.' && (map[i][j]==ch || map[i][j]=='T'))
					count++;
				else
					break;
			}
			if(count==4)
			{
				ok=1;
				break;
			}
		}
		if(!ok)
		{
			for(i=0;i<4;++i)
			{
			    count=1;
			    ch=map[0][i];
			    for(j=1;j<4;++j)
				{
				    if(map[j][i]!='.' && (map[j][i]==ch || map[j][i]=='T'))
					    count++;
				    else
					    break;
				}
			    if(count==4)
				{
				    ok=1;
				    break;
				}
			}
		}
		if(!ok)
		{
			ch=map[0][0];
			if(ch!='.')
			{
			count=1;
			for(i=1;i<4;++i)
			{
				if(ch==map[i][i] || map[i][i]=='T')
					count++;
				else break;
			}
			if(count==4) ok=1;
			}
		}
		if(!ok)
		{
			ch=map[0][3];
			if(ch!='.')
			{
			count=1;
			for(i=1;i<4;++i)
			{
				if(ch==map[i][3-i] ||map[i][3-i]=='T')
					count++;
				else break;
			}
			if(count==4) ok=1;
			}
		}
	    fout<<"Case #"<<index<<": ";
		if(ok)
		{
		
			if(ch=='X')
				fout<<"X won"<<endl;
			else if(ch=='O')
				fout<<"O won"<<endl;
		}
		else
		{
			if(flag)
				fout<<"Game has not completed"<<endl;
			else
				fout<<"Draw"<<endl;
		}
	}
	return 0;
}

