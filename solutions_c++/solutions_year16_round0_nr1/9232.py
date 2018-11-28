#include<iostream>
#include<string>
#include<math.h>
#include<set>
#include<vector>
#include<fstream>
#include<sstream>

using namespace std;

bool checkFull(int numbers[])
{
	for(int i = 0; i < 10; i++)
	{
		if(numbers[i]==0)
			return false;
	}
	return true;
}

int main()
{
	int T = 0;
	fstream fin("A.in");
	fstream fout("A.out");

	fin>>T;
	
	int counter = 1;
	
	while (counter <= T)
	{
		int numbers[10]={0};
		int N;
		fin>>N;
		int N_count = 0;
		int recent_num = 0;
		bool flag = false;

		while(!checkFull(numbers))
		{
			int new_num = N*N_count;
			recent_num = new_num;

			while(new_num!=0)
			{
				int rem = new_num % 10;
				
				if (numbers[rem]==0)
					numbers[rem]=1;

				new_num = new_num / 10;
			}
			N_count++;

			if (N == 0)
			{
				flag = true;
				break;
			}
		}
		if (flag)
			fout<<"Case #"<<counter<<": "<<"INSOMNIA"<<endl;
		else
			fout<<"Case #"<<counter<<": "<<recent_num<<endl;
		counter++;
	}
	return 0;
}