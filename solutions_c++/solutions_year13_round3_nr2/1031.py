#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<math.h>
using namespace std;



int main()
{
	ifstream file("B-small-attempt0.in");
	cin.rdbuf(file.rdbuf());
	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	long long T;
	int x,y;
	char res[600];

	cin>>T;
	int a = 0;
	for(int t=0;t<T;t++)
	{
		a = 0;
		cin>>x>>y;
		if(x>0)
		{
			for(int i=1;i<=x;i++)
			{
				res[a++] = 'W';
				res[a++] = 'E';
			}
		}
		else if(x<0)
		{
			for(int i=1;i<=abs(x);i++)
			{
				res[a++] = 'E';
				res[a++] = 'W';
			}
		}
		else
		{
			;
		}

		if(y>0)
		{
			for(int i=1;i<=y;i++)
			{
				res[a++] = 'S';
				res[a++] = 'N';
			}
		}
		else if(y<0)
		{
			for(int i=1;i<=abs(y);i++)
			{
				res[a++] = 'N';
				res[a++] = 'S';
			}
		}
		else
		{
			;
		}
		res[a]='\0';

		cout<<"Case #"<<t+1<<": "<<res<<endl;
	}

	return 0;
}
		