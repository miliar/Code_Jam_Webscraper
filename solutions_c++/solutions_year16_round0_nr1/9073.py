#include<stack>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;

bool check(int*arr)
{
	for (int i = 0;i < 10;i++)
	{
		if (arr[i] != i)
			return false;
	}
	return true;
}

void main()
{
	fstream f;
	fstream file;
	f.open("A-large.in");
	//if(f)
		//cout << "hello";
	int tCases;
	f >> tCases;
	file.open("output.txt",ios::app);
	//cout << "hello";
	long int N;
	int rem;
	long int quo=-1;
	int arr[10] = {-1,-1, -1, -1, -1, -1, -1, -1, -1, -1 };
	
	for (int i = 1;i <= tCases; i++)
	{
		while (!f.eof())
		{
			
			f >> N;
			if (N == 0)
			{
				file << "Case #" << i << ":" << " INSOMNIA"<<endl;
				break;
			}

		
			int k = 1;
			while (!check(arr))
			{
				
				long int num = N*k;
				quo = num;

				while (quo != 0)
				{
					
					rem = quo % 10;
					arr[rem] = rem;
					if (check(arr))
					{
						file << "Case #" << i << ": " << num<<endl;
						break;
					}
					else
					{
						quo = quo / 10;
					}
				}
				if (check(arr))
				{
					for (int j = 0;j < 10;j++)
						arr[j] = -1;
					break;
				}
				k++;
			}

			
			i++;
			if (i == 101)
				break;

		}

	}
	
	

	
}