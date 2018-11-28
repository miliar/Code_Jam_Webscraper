#include<fstream>
using namespace std;
ofstream fileout;
ifstream filein;
class arrangement
{
	int a[4][4],b[4][4],r1,r2;
	public:	arrangement();
		void output(int);
};
arrangement::arrangement()
{
	int i,j;
	filein>>r1;
	r1=r1-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			filein>>a[i][j];
		}
	}
	filein>>r2;
	r2=r2-1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			filein>>b[i][j];
		}

	}

}



void arrangement::output(int x)

{

	fileout<<"Case #"<<x<<": ";

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

		fileout<<"Volunteer cheated!";
	}
	else if(count==1)
	{
		fileout<<ret;
	}
	else
	{
		fileout<<"Bad magician!";
	}
	if(x!=100)	{
	fileout<<endl;
	}
}
main()
{
	int n,i;
	arrangement *p;
	fileout.open("upload.txt");
	filein.open("test.in");
	filein>>n;
	p=new arrangement[n];
	for(i=0;i<n;i++)
	{
		p[i].output(i+1);
	}
	return 0;
}
