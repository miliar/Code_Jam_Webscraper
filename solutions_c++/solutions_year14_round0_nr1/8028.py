#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
	ifstream ifs("A-small-attempt3.in");
	ofstream ofs("result.txt");
	cin.rdbuf(ifs.rdbuf());
	cout.rdbuf(ofs.rdbuf());
    int T;
	int a[4][4];
	int b[4][4];
	int first,second;
	int result;
    cin>>T;
    for(int j=0;j<T;j++)
    {
		cin>>first;
	 	int count=0;
		int i=0;
		for(;i<4;i++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>a[i][k];					
			}		
		}

		cin>>second;
	
		for(i=0;i<4;i++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>b[i][k];					
			}	
		}
	
		for(i=0;i<4;i++)
		{
			for(int k=0;k<4;k++)
			{
				if(a[first-1][i]==b[second-1][k])
				{
					count++;
					result=a[first-1][i];
				}
			}
		}

		if(count==1)
		{
			cout<<"Case #"<<(j+1)<<": "<<result<<endl;
		}else if(count==0)
		{
			cout<<"Case #"<<(j+1)<<": "<<"Volunteer cheated!"<<endl;
		}else 
		{
			cout<<"Case #"<<(j+1)<<": "<<"Bad magician!"<<endl;
		}

	}
	ifs.close();
	ofs.close();
	return 0;
}