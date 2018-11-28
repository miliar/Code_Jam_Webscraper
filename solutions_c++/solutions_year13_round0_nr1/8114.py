#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
	int t;cin>>t;
	for(int i=1;i<=t;++i) 
	{
		bool out=false;
		string f[4];
		int x=-1,y=-1;
		for(int j = 0; j < 4; ++j)
		{
			cin>>f[j];
		}

		for(int j = 0; j < 4; ++j)
		{
			for(int k = 0; k < 4; ++k)
			{
				if(f[j][k]=='T')
				{
					x=k; y=j;
				}
			}
		}


		for(int T = 0; T < 2; ++T)
		{
			if(out) break;
			if(T==0&&x!=-1) f[y][x]='O';
			if(T==1&&x!=-1) f[y][x]='X';

			int ans=0;
			int cnt=0;
			bool flag=0;
			for(int j = 0; j < 4; ++j)
			{
				for(int k = 0; k < 4; ++k)
				{
					if(f[j][k]!='.') cnt++;
					else continue;

					if(f[j][k]=='O'&&f[j][0]==f[j][1]&&f[j][1]==f[j][2]&&f[j][2]==f[j][3])
					{
						ans=1;
						flag=true;
						break;
					}
					if(f[j][k]=='X'&&f[0][k]==f[1][k]&&f[1][k]==f[2][k]&&f[2][k]==f[3][k])
					{
						ans=2;
						flag=true;
						break;
					}	
				
					if(f[j][k]=='X'&&f[j][0]==f[j][1]&&f[j][1]==f[j][2]&&f[j][2]==f[j][3])
					{
						ans=2;
						flag=true;
						break;
					}
					if(f[j][k]=='O'&&f[0][k]==f[1][k]&&f[1][k]==f[2][k]&&f[2][k]==f[3][k])
					{
						ans=1;
						flag=true;
						break;
					}	
				}
				if(flag) break;	
			}

			if(f[0][0]=='X'&&f[0][0]==f[1][1]&&f[1][1]==f[2][2]&&f[2][2]==f[3][3])
			{
				flag=true; ans=2;
			}

			if(f[0][0]=='O'&&f[0][0]==f[1][1]&&f[1][1]==f[2][2]&&f[2][2]==f[3][3])
			{
				flag=true; ans=1;
			}
			if(f[0][3]=='X'&&f[0][3]==f[1][2]&&f[1][2]==f[2][1]&&f[2][1]==f[3][0])
			{
				flag=true; ans=2;
			}

			else if(f[0][3]=='O'&&f[0][3]==f[1][2]&&f[1][2]==f[2][1]&&f[2][1]==f[3][0])
			{
				flag=true; ans=1;
			}
			
			if(!flag&&t==0) continue;
			if(!flag)
			{
				if(cnt!=16) printf("Case #%d: Game has not completed\n",i);
				else printf("Case #%d: Draw\n",i);	
				out=true;
			}
			else if(ans==1)
			{
				printf("Case #%d: O won\n",i);
				out=true;
			}
			else
			{	
				printf("Case #%d: X won\n",i);
				out=true;
			}
		}
	}
  return 0;
}
