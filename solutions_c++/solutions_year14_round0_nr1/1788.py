#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream fout;
	fout.open ("results.txt");
	int cases, row, item1, item2, item3, item4;
	int numbers[4];
	int count, answer, test;

	cin>>cases;
	test = 1;

	while(test <= cases)
	{
		cin>>row;
		count = 0;

		for(int k = 1; k < 5; k++)
		{
			cin>>item1>>item2>>item3>>item4;

			if(k == row)
			{
				numbers[0] = item1;
				numbers[1] = item2;
				numbers[2] = item3;
				numbers[3] = item4;
			}
		}

		cin>>row;
		for(int k = 1; k < 5; k++)
		{
			cin>>item1>>item2>>item3>>item4;

			if(k == row)
			{
				for(int i = 0; i < 4; i++)
				{
					if(numbers[i] == item1)
					{
						answer = numbers[i];
						count++;
					}
					if(numbers[i] == item2)
					{
						answer = numbers[i];
						count++;
					}
					if(numbers[i] == item3)
					{
						answer = numbers[i];
						count++;
					}
					if(numbers[i] == item4)
					{
						answer = numbers[i];
						count++;
					}

				}
			}
		}

		fout<<"Case #"<<test<<": ";

		if(count == 0)
			fout<<"Volunteer cheated!"<<endl;
		else if(count > 1)
			fout<<"Bad magician!"<<endl;
		else
			fout<<answer<<endl;

		test++;
	}


	return 0;
}
