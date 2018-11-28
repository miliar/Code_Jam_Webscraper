#include <iostream>

using namespace std;

void magicSolver()
{
	int tests;
	cin>>tests;
	for(int n=1; n<=tests; ++n)
	{
		int l1[4], l2[4];
		int row, waste;
		
		cin>>row;
		for(int i=1; i<=4; i++)
			if(row==i)
			{
				cin>>l1[0];
				cin>>l1[1];
				cin>>l1[2];
				cin>>l1[3];
			}
			else
			{
				cin>>waste;
				cin>>waste;
				cin>>waste;
				cin>>waste;
			}
		
		cin>>row;
		for(int i=1; i<=4; i++)
			if(row==i)
			{
				cin>>l2[0];
				cin>>l2[1];
				cin>>l2[2];
				cin>>l2[3];
			}
			else
			{
				cin>>waste;
				cin>>waste;
				cin>>waste;
				cin>>waste;
			}
		
		int res = -2, op;
		for(int i=0; i<4 && res; i++)
			for(int j=0; j<4; j++)
				if(l1[i] == l2[j])
				{
					res++;
					if(!res)
						break;
					else
						op = l1[i];
				}
		
		switch(res)
		{
			case 0:
				cout<<"Case #"<<n<<": Bad magician!\n";
				break;
			case -1:
				cout<<"Case #"<<n<<": "<<op<<"\n";
				break;
			case -2:
				cout<<"Case #"<<n<<": Volunteer cheated!\n";
				break;			
		}
	}
}