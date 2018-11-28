#include<iostream>
#include<fstream>

using namespace std;

int main(void)
{
	int t;
	ifstream input ("input.txt");
	ofstream output ("output.txt");
	
	if(input.is_open() && output.is_open())
	{
		input >> t;
		int test=t;
		while(t--)
		{
			int ra,rb;
			int a[4][4],b[4][4];
			input>>ra;
			ra--;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					input>>a[i][j];
				}
			}
			
			input>>rb;
			rb--;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					input>>b[i][j];
				}
			}
			
			int count =0;int ans=0;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
				//	cout<<a[ra][j] <<" " <<b[rb][i]<<endl;
					if(a[ra][j]==b[rb][i])
					{
						count++;
						ans=a[ra][j];
					}
				}
			}
			
			if(count==1)
			{
				output << "Case #"<<test-t<<": "<<ans<<"\n";
			}
			else if(count>1)
			{
				output <<"Case #"<<test-t<<": "<<"Bad magician!"<<"\n";
			}
			else if(count==0)
			{
				output << "Case #"<<test-t<<": "<<"Volunteer cheated!"<<"\n";
			}
			
			
		}
	}
	else
	{
		cout<<"error";
	}
	return 0;
}