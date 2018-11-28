#include<fstream>
using namespace std;

int main()
{
	ifstream cin;
	ofstream cout;
	
	cin.open("BYO.txt");
	cout.open("output.txt");
	int t,i,j,win=0,a,b,k;
	cin>>t;
	
	for(int uy=1;uy<=t;uy++)
	{
		cin>>a>>b>>k;
		win=0;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					win++;
				}
			}
		}
		cout<<"Case #"<<uy<<": "<<win<<endl;
	}
	cin.close();
	cout.close();
	return 0;
}