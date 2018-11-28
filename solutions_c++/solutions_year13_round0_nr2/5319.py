#include<fstream>
using namespace std;

int n,m;
int a[100][100];
ifstream infile("PB.in");
ofstream ofile("PB.txt");

void init()
{
	n=0;
	m=0;
	for (int i=0; i!=100; ++i)
		for (int j=0; j!=100; ++j)
			a[i][j]=100;
}
void read()
{
	infile>>n>>m;
	for (int i=0; i!=n; ++i)
		for (int j=0; j!=m; ++j)
			infile>>a[i][j];
}


string calc()
{
	bool f1, f2;
	for (int i=0; i!=n; ++i)
	{
		for (int j=0; j!=m; ++j)
		{
			f1=false;
			f2=false;
			for (int k=0; k!=n; ++k)
				if (a[k][j]>a[i][j])
				{
					f1=true;
					break;
				}
			for (int k=0; k!=m; ++k)
				if (a[i][k]>a[i][j])
				{
					f2=true;
					break;
				}
			if (f1&&f2)
				return "NO";
		}
	}
	return "YES";
}
void print(int i,string s)
{
	ofile<<"Case #"<<i<<": "<<s<<endl;
}


int main()
{

	int t;
	infile>>t;

	for (int i=0; i!=t; ++i)
	{
		init();
		read();
		string s=calc();
		print(i+1,s);
	}

	return 0;
}
