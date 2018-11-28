#include<fstream>

using namespace std;

int main()
{
	ifstream f1("A-small-attempt2.in", ios::in);
	ofstream f2("standingOvation.txt", ios::out);
	int t,x, ax;
	string a;
	char c = '0';
	if(!f1)
		printf("Can't open file for reading");
	else if(!f2)
		printf("Can't open file for writing");
	else
	{
		f1>>t;
		int sum = 0;
		int req=0;
		for(int cases=0; cases<t; cases++)
		{
			f1>>ax;
			sum=0;
			req = 0;
			f1>>a;
			x = a[0] - c;
			for(int i=1;i<ax+1;i++)
			{
				sum += x;
				if(a[i]!='0')
				{
					if(i > sum)
					{
						req += i - sum;
						sum += req;
					}
				}
				x = (a[i] - c);
			}
			f2<<"Case #"<<cases + 1<<": "<<req<<"\n";
		}
	}
	f1.close();
	f2.close();
	return 1;
}
