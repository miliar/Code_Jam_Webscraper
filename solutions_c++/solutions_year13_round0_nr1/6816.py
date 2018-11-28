#include<iostream>
#include<string>
#include<vector>
#include<list>
#include<stack> 
#include<queue> 
#include<set>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;

char a[4][4];
char row[4],col[4],dgo[2];

int main()
{
	freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\A-large.in","r",stdin);
	freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\out-large.txt","w",stdout);
	int t;
	cin>>t;
	getchar();
	for(int nt=1;nt<=t;nt++)
	{
		bool tag=false;
		bool full=true;
		for(int i=0;i<4;i++)
		{							 
			for(int j=0;j<4;j++)
			{	
				scanf("%c",&a[i][j]);
				if(a[i][j]=='.')
					full=false;
			}
			getchar();
		}
		getchar();
			

		
		for(int i=0,j;i<4;i++)
		{
			bool flag=false,win=true;
			char now;
			for(j=0;a[i][j]!='.'&&j<4;j++)
			{ 
				if(a[i][j]=='T') continue;
				if(!flag){flag=true; now=a[i][j];continue;}
				else if(now!=a[i][j]) win=false; 
			}
			if(j>=4&&win) { printf("Case #%d: %c won\n",nt,now);tag=true;break;}		
		}
		if(tag) continue;
		
		
		for(int i=0,j;i<4;i++)
		{
			bool flag=false,win=true;
			char now;
			for(j=0;j<4&&a[j][i]!='.';j++)
			{ 
				if(a[j][i]=='T') continue;
				if(!flag){flag=true; now=a[j][i];continue;}
				else if(now!=a[j][i]) win=false; 
			}
			if(j>=4&&win) { printf("Case #%d: %c won\n",nt,now);tag=true;break;}		
		}
		if(tag) continue;

		bool flag=false,win=true;
		char now;
		int i;		
		for(i=0;i<4&&a[i][i]!='.';i++)
		{ 
			if(a[i][i]=='T') continue;
			if(!flag){flag=true; now=a[i][i];continue;}
			else if(now!=a[i][i]) win=false; 
		}
		if(i>=4&&win) { printf("Case #%d: %c won\n",nt,now);continue;}	
		
		flag=false,win=true;
		for(i=0;i<4&&a[i][3-i]!='.';i++)
		{ 
			if(a[i][3-i]=='T') continue;
			if(!flag){flag=true; now=a[i][3-i];continue;}
			else if(now!=a[i][3-i]) win=false; 
		}
		if(i>=4&&win) {printf("Case #%d: %c won\n",nt,now);continue;}	
		
		
		if(full) printf("Case #%d: Draw\n",nt);
		else printf("Case #%d: Game has not completed\n",nt);	
						
	}
	
			
	return 0;
}
