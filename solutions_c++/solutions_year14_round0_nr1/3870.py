#include<iostream>
#include<map>

using namespace std;

int main()
{
	map<int, int> hash;
	int num = 0;
	cin >> num;
	int cases = 1;
	while(cases <= num)
	{
		hash.clear();
		int row = 0;
		cin >> row;
		int num;
		for(int i = 1; i <= 4; i++)
			for(int j = 0; j < 4; j++)
			{
				cin>> num;
				if(i == row)
					hash[num] = 1;
			}

		row = 0;
		cin >> row;
		num = 0;
		int count = 0, foundNum = 0, result = 0;
		for(int i = 1; i <= 4; i++)
			for(int j = 0; j < 4; j++)
			{
				cin>> num;
				if(i == row)
				{
					if(hash.find(num) != hash.end())
					{
						count++;
						foundNum = num;
					}
				}
			}

		if(count == 1)
			cout<<"Case #"<<cases<<": "<< foundNum<<endl;
		else if (count == 0)
			cout<<"Case #"<<cases<<": Volunteer cheated!"<<endl;
		else if (count > 1)
			cout<<"Case #"<<cases<<": Bad magician!"<<endl;

			
		cases++;
	}
	return 0;
}
