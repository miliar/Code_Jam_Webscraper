#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

int mymap[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

int chartoint(char i)
{
	switch(i)
	{
	case '1':
		return 1;
	case 'i':
		return 2;
	case 'j':
		return 3;
	case 'k':
		return 4;
	default:
		return 0;
	}
}

char inttochar(int i)
{
	switch(i)
	{
	case 1:
		return '1';
	case 2:
		return 'i';
	case 3:
		return 'j';
	case 4:
		return 'k';
	default:
		return 0;
	}
}

int main()
{
	int T,c=1;
	scanf("%d",&T);

	while(T--)
	{
		char buf[10001];
		int d,L;
		scanf("%d%d",&d,&L);
		scanf("%s",buf);

		string total="";
		for(int i=0;i<L;i++)
		{
			total+=buf;
		}
		int acc;
		int sign = 1;
		bool ifind,jfind,kfind;
		ifind=jfind=kfind=false;
		string ans;
		while(total.length() > 1)
		{
			int a = chartoint(total[0]);
			int b = chartoint(total[1]);

			if(a<0)
			{
				sign*=-1;
				a = abs(a);
			}
			if(b<0)
			{
				sign*=-1;
				b = abs(b);
			}

			if(!ifind && a == 2)
			{
				ifind = true;
				ans.push_back('i');
				total.replace(0,1,"");
				continue;
			}
			if(ifind && !jfind && a == 3)
			{
				jfind = true;
				ans.push_back('j');
				total.replace(0,1,"");
				continue;
			}
			acc = mymap[a][b];

			if(acc < 0)
			{
				sign*=-1;
				acc = abs(acc);
			}
			char ch = inttochar(acc);
			string anew;
			anew.push_back(ch);
			total.replace(0,2,anew);
		}

		ans+=total;

		if(ans == "ijk" && sign == 1)
		{
			printf("Case #%d: YES\n",c++);
		}
		else
		{
			printf("Case #%d: NO\n",c++);
		}
	}
	return 0;
}