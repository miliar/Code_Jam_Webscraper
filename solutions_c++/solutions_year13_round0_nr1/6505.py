#include<iostream>	
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<algorithm>
#include<functional>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;
int gcd(int a,int b) { while (b > 0) { a = a % b; a ^= b; b ^= a; a ^= b;} return a; }
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define MOD 1000000007
vs v(4);

int count(int x,char c)
{
	//check xth row and xth column for 4 c/T
	int m1=0,m2=0;
	for(int i=0;i<4;i++)
	{
		if(v[x][i]==c || v[x][i]=='T')
			m1++;
			
		if(v[i][x]==c || v[i][x]=='T')
			m2++;
	}
	return max(m1,m2);
}

int count_d(char c)
{
	//check both the diagonals for 4 c/T
	int m1=0,m2=0,i,j;
	for(i=0;i<4;i++)
	{
		if(v[i][i]==c || v[i][i]=='T')
			m1++;
	}
	
	for(i=0,j=3;i<4,j>=0;i++,j--)
	{
		if(v[i][j]==c || v[i][j]=='T')
			m2++;
	}
	return max(m1,m2);
}

int main()
{

	int tc;
	int i,j,n;
	scanf("%d",&tc);
	int p=0;
	while(tc--)
	{		
		p++;
		printf("Case #%d: ",p);
		for(i=0;i<4;i++)
			cin>>v[i];

		int count_dots=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				if(v[i][j]=='.')
					count_dots++;
			}
		
		int flag=0;
		for(i=0;i<4;i++)
		{
			if(count(i,'X')==4)
			{
				printf("X won\n");
				flag=1;
				break;
			}	
			if(count(i,'O')==4)
			{
				printf("O won\n");
				flag=1;
				break;
			}
		}
		if(flag==1)
			continue;
			
		if(count_d('X')==4)
			printf("X won\n");
		else if( count_d('O')==4)
			printf("O won\n");
		else if(count_dots>0)
			printf("Game has not completed\n");
		else
			printf("Draw\n");	
		
	}
	return 0;
}

