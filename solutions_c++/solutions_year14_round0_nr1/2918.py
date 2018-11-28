#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream is;
	ofstream os;
	is.open("F:\\A-small-attempt1.in");
	os.open("F:\\A-small-attempt1.out");
	int t;
	is>>t;
	int n,m;
	int a[4][4];
	int b[4][4];
	for(int c=1;c<=t;c++)
	{
		is>>n;
		n-=1;
		for(int i=0;i<=3;i++)
			for(int j=0;j<=3;j++)
				is>>a[i][j];
		is>>m;
		m-=1;
		for(int i=0;i<=3;i++)
			for(int j=0;j<=3;j++)
				is>>b[i][j];
		int count=0;
		int answer;
		for(int i=0;i<=3;i++)
		{
			for(int j=0;j<=3;j++)
			{
				if(a[n][i]==b[m][j])
				{
					count++;
					answer=a[n][i];
					break;
				}
			}
		}
		if(count==0)
			os<<"Case #"<<c<<": Volunteer cheated!"<<endl;
		else if(count==1)
			os<<"Case #"<<c<<": "<<answer<<endl;
		else
			os<<"Case #"<<c<<": Bad magician!"<<endl;
	}
	is.close();
	os.close();
	return 0;
}
