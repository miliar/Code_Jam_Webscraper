#include<fstream>
using namespace std;
ofstream testout;
ifstream testin;
class array
{
	int a[4][4],b[4][4],r1,r2;
	public:	array();
		void output(int);
};
array::array()
{
	int i,j;
	testin>>r1;
	r1=r1-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			testin>>a[i][j];
		}
	}
	testin>>r2;
	r2=r2-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			testin>>b[i][j];
		}

	}

}



void array::output(int x)

{

	testout<<"Case #"<<x<<": ";

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

		testout<<"Volunteer cheated!";
	}
	else if(count==1)
	{
		testout<<ret;
	}
	else
	{
		testout<<"Bad magician!";
	}
	if(x!=100)	{
	testout<<endl;
	}
}
main()
{
	int n,i;
	array *p;
	testout.open("output.txt");
	testin.open("test.in");
	testin>>n;
	p=new array[n];
	for(i=0;i<n;i++)
	{
		p[i].output(i+1);
	}
	return 0;
}
