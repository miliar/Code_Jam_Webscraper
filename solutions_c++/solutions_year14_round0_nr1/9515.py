#include<fstream>

using namespace std;

ofstream out;
ifstream in;

class matrix
{
	int a[4][4],b[4][4],n,m;

	public:
		void input();
		void output(int);
};

void matrix::input()
{
	int i,j;

	in>>n;
	n=n-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
		in>>a[i][j];
		}
	}

	in>>m;
	m=m-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			in>>b[i][j];
		}
	}
}

void matrix::output(int x)
{
	out<<"Case #"<<x<<": ";
	int c[4],d[4],j,count=0,i,ret;

	for(j=0;j<4;j++)
	{
		c[j]=a[n][j];
		d[j]=b[m][j];
	}

	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(c[i]==d[j])
			{
				ret=c[i];
				count++;
			}
		}
	}

	if(count==0)
	{
		out<<"Volunteer cheated!";
	}

	else if(count==1)
	{
		out<<ret;
	}

	else
	{
		out<<"Bad magician!";
	}

	if(x!=100)
	{
	out<<endl;
	}
}

int main()
{
	int n,i;

	matrix *p;

	out.open("Output-small9.txt");
	in.open("A-small-attempt0 (1).in");

	in>>n;

	p=new matrix[n];

	for(i=0;i<n;i++)
	{
		p[i].input();
		p[i].output(i+1);
	}

	return 0;
}
