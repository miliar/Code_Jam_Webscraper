#include<bits/stdc++.h>
using namespace std;

int main(void)
{
	int T,X,R,C;
	freopen("SO.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	int c = 1;
	while(T--)
	{
		printf("Case #%d: ",c++);
		scanf("%d %d %d",&X,&R,&C);
		if(X == 1)
			cout<<"GABRIEL\n";
		else if(X == 2)
		{
			int area = R*C;
			if(area % 2 == 0)
				cout<<"GABRIEL\n";
			else
				cout<<"RICHARD\n";
		}
		else if(X == 3)
		{
			int area = R*C;
			if(area == 6 || area == 9 || area == 12)
				cout<<"GABRIEL\n";
			else
				cout<<"RICHARD\n";
		}
		else
		{
			int area = R*C;
			if(area == 12 || area == 16)
				cout<<"GABRIEL\n";
			else
				cout<<"RICHARD\n";
		}	
	}
	return 0;
}
