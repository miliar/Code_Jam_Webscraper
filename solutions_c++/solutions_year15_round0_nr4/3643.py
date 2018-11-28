#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int solve(int x, int r, int c);


int main()
{
	int caseNum;

	cin >> caseNum;

	char *gabriel = "GABRIEL";
	char *richard = "RICHARD";

	for(int case_i = 1; case_i <= caseNum; case_i++)
	{
		cout<<"Case #"<<case_i<<": ";
		int result = 0;	//min friend

		int x,r,c;

		cin>>x;
		cin>>r;
		cin>>c;
		
		result = solve(x,r,c);
		if(result == 0)
			cout<<richard<<endl;
		else if(result == 1)
			cout<<gabriel<<endl;
		else
			cout<<"ERROR!!!"<<endl;
	}

	return 0;
}


int solve(int x, int r, int c)
{
	int totalblock = r*c;
	if (totalblock % x != 0)
	{
		return 0;	//RICHARD
	}
	else
	{
		switch (x)
		{
			case 1:
				return 1;	//GABRIEL
			case 2:		//12 14	22
				return 1;	//GABRIEL
			case 3:		//13	23	33	34
				if(totalblock == 3)
					return 0;	//RICHARD
				return 1;	//GABRIEL
			case 4:		//14	22	24	34
				if(totalblock < 12)
					return 0;	//RICHARD
				return 1;	//GABRIEL		
		}

	}

	return -1;
}
