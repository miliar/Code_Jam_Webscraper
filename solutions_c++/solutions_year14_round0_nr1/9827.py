#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	
	int T, A1, cards1[4][4], A2, cards2[4][4];
	
	cin>>T;
	int i=0;
	
	while(i<T)
	{
		cin>>A1;
		
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				cin>>cards1[j][k];
			}
			
		}
		
		cin>>A2;
		
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				cin>>cards2[j][k];
			}
		}
		
		int temp1 = A1-1;
		int temp2 = A2-1;
		int counter = 0;
		int valueFound;
		for(int j=0; j<4; j++)
		{
			for(int k = 0; k<4; k++)
			{
				if(cards1[temp1][j] == cards2[temp2][k])
				{
					valueFound = cards1[temp1][j];
					counter++;
				}
			}
		}
		
		
		cout<<"Case #"<<i+1<<": ";
		if(counter ==1)
		{
			cout<<valueFound;
		}else if(counter >= 2)
		{
			cout<<"Bad magician!";
		}else if(counter ==0)
		{
			cout<<"Volunteer cheated!";
		}
		cout<<endl;
		i++;
	}
	
	return 0;
}
