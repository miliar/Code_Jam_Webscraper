#include <iostream>
using namespace std;

int main()
{
	int testCases = 0,r1=0,r2=0,match,k=0;
	int* a1 = new int[4];
	int* a2 = new int[4];
	cin>>testCases;int n=testCases;
	while(testCases--)
	{
		int count =0;
		cin>>r1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(i+1 == r1)
					cin>>a1[j];
				else
					cin>>k;
			}
		}
		cin>>r2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(i+1 == r2)
					cin>>a2[j];
				else
					cin>>k;
			}
		}

		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a1[i]==a2[j])
				{
					count++;
					match = a1[i];
				}
			}
		}

		if(count < 1)
			cout<<"Case #"<<(n-testCases)<<":"<<" Volunteer cheated!"<<endl;
		else if(count > 1)
			cout<<"Case #"<<(n-testCases)<<":"<<" Bad magician!"<<endl;
		else
			cout<<"Case #"<<(n-testCases)<<":"<<" "<<match<<endl;
	}
	
	return 0;
}