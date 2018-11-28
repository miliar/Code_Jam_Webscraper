# include <iostream>
# include <fstream>
using namespace std;
int a[10][10];
int main ()
{
	ofstream fout ("b-ioi-1.txt");
	int t;
	cin>>t;
	for (int counter=0;counter<t;counter++)
	{
int n,m,ones=0;
bool final;
cin>>n>>m;
for (int i=0;i<n;i++)
{
	for (int x=0;x<m;x++)
	{
		cin>>a[i][x];
		if (a[i][x]==1)
			ones++;
	}
}
if (ones==0 || m==1 || n==1)
		fout<<"Case #"<<counter+1<<": YES"<<endl;
else
{
bool p;
for (int i=0;i<n;i++)
{
	for (int x=0;x<m;x++)
	{
		if (a[i][x]==1)
		{
			bool r=1,b=1;
			for (int g=0;g<m;g++)
			{
				if (a[i][g]==2)
				{
					r=0;
					break;
				}
			}
			for (int g=0;g<n;g++)
			{
				if (a[g][x]==2)
				{
					b=0;
					break;
				}
			}
			if (b==1 || r==1)
				final=1;
			else
			{
				final=0;
				break;
			}
		}
		else
		{
		final=1;
		
		}
	
	
	}
	if (final==0)
		break;
}
	if (final==0)
		fout<<"Case #"<<counter+1<<": NO"<<endl;
	else
		fout<<"Case #"<<counter+1<<": YES"<<endl;
}
	}

}