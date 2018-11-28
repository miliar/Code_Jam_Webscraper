#include<iostream>

using namespace std;

int main()
{
	int no_of_tests, user_input[100][2];
	bool a[100][16][2];
	
	int num;	
	cin>>no_of_tests;
	for(int i = 0; i < no_of_tests; i++)
	{
		for(int l = 0; l < 2; l++)
		{
			cin>>user_input[i][l];
			for(int j = 0; j < 4; j++)
			{
				for(int k = 0; k < 4; k++)			
				{
					cin>>num;
					if(j+1 == user_input[i][l])
						a[i][num-1][l] = true;
					else
						a[i][num-1][l] = false;
				}
			}		
		}

		int count = 0;	
		int chosen_num;
		for(int j = 0; j < 16; j++)
		{
			if(a[i][j][0] && a[i][j][1])
			{
				count++;
				chosen_num = j+1;
			}	
		}

		if(count == 1)
			cout<<"Case #"<<i+1<<": "<<chosen_num<<'\n';
		else if(count == 0)
			cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		else
			cout<<"Case #"<<i+1<<": Bad magician!\n";
		
	}

	return 0;
}
