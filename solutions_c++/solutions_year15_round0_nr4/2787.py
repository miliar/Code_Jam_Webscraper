#include<iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		int X,R,C;
		bool win=false;
		cin>>X>>R>>C;
		if(X==1)	win=true;
		else if(X==2)
		{
			if(R%2==0||C%2==0)	win=true;
		}
		else if(X==3)
		{
			if((R==3&&C>=2)||(R>=2&&C==3))	win=true;
		}
		else if(X==4)
		{
			if((R>=3&&C==4)||(R==4&&C>=3))	win=true;
		}
		if(win)	printf("Case #%d: GABRIEL\n",i);
		else 	printf("Case #%d: RICHARD\n",i);
	}
}
