#include<iostream>
#include <fstream>
using namespace std;


int main()
{
	int test,a,b,count,ans,z;
	ofstream myfile;
	int ar[5][5] = {0};
	int ar1[5][5] = {0};

	cin >> test;
	myfile.open ("example.txt");
	z = test;
	while(test)
	{
		int x[17]={0};
		count = 0;
		ans = 0;
		cin >> a;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				cin >> ar[i][j];
			}
		}
		cin >> b;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				cin >> ar1[i][j];
			}
		}
		for(int i=1;i<5;i++)
		{
			x[ar[a][i]]++;
		}
		for(int i=1;i<5;i++)
		{
			x[ar1[b][i]]++;
		}
		for(int i=1;i<17;i++)
		{
			if(x[i]==2)
			{
				
				count=count+5;
				ans = i;
				//cout << "Abhimanyu";
			}
			else if(x[i]==1)
			{
				count++;
			}
		}
		if(count == 11)
		myfile << "Case #"<<z-(test-1)<<": "<<ans<<"\n";
		else if(count == 8)
		myfile << "Case #"<<z-(test-1)<<": "<<"Volunteer cheated!"<<"\n";
		else if(count != 11 && count != 8)
		myfile << "Case #"<<z-(test-1)<<": "<<"Bad magician!"<<"\n";
		//cout << "Abhimanyu";
		
		test--;
	}
		
		return 0;
	
}
			
		
