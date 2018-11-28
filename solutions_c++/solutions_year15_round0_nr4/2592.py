#include <string>
#include <cstdio>
#include <iostream>

#define FILE_NAME "data"

using namespace std;

char buffer[256];

int main()
{
	int case_num, i, X, R, C, status;

	sprintf(buffer, "%s.in", FILE_NAME);
	freopen(buffer, "r", stdin);
	sprintf(buffer, "%s.out", FILE_NAME);
	freopen(buffer, "w", stdout);

	cin>>case_num;
	i=0;
	while(i<case_num)
	{
		status = 0;
		cin>>X>>R>>C;
		switch(X)
		{
			case 1:
				status = 1;
				break;
			case 2:
				if(R*C%2==0)
					status = 1;
				break;
			case 3:
				if(R*C==6||R*C==9||R*C==12)
					status = 1;
				break;
			case 4:
				if(R*C==12||R*C==16)
					status = 1;
				break;
			default:
				break;
		}
		if(status)
			cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
		else
			cout<<"Case #"<<i+1<<": RICHARD"<<endl;
		
		i++;
	}
		
	return 0;
}