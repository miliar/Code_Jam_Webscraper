#include<fstream>

using namespace std;

ofstream myout;
ifstream myin;

class matrix
{
	int a[4][4],b[4][4],r1,r2;
	
	public:
		matrix();
		void output(int);
};

matrix::matrix()
{
	int i,j;
	
	myin>>r1;
	r1=r1-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			myin>>a[i][j];
		}
	}
	
	myin>>r2;
	r2=r2-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			myin>>b[i][j];
		}
	}
}

void matrix::output(int x)
{
	myout<<"Case #"<<x<<": ";
	int c[4],d[4],j,count=0,i,ret;
	
	for(j=0;j<4;j++)
	{
		c[j]=a[r1][j];
		d[j]=b[r2][j];
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
		myout<<"Volunteer cheated!";
	}
	
	else if(count==1)
	{
		myout<<ret;
	}
	
	else
	{
		myout<<"Bad magician!";
	}
	
	if(x!=100)
	{
		myout<<endl;
	}
}

main()
{
	int n,i;
	
	matrix *p;
	
	myout.open("Output-small1.txt");
	myin.open("A-small-attempt1.in");
	myin>>n;
	
	p=new matrix[n];
	
	for(i=0;i<n;i++)
	{
		p[i].output(i+1);
	}
	
	return 0;
}

