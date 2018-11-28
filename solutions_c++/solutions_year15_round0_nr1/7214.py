#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	fstream f1("input.txt",ios::in);
	fstream f2("output.txt",ios::out);	
	int t;
	int i = 1;
	f1 >> t;
	while(true)
	{
		if(i > t) break;
		int smax;
		f1 >> smax;
		int sum = 0;
		int count = 0;
		for(int j = 0; j <= smax; j++)
		{
			char temp;
			int temp1;
			f1 >> temp;
			temp1 = temp - int('0');
			if(j == 0)
			{
				sum = temp1;
				//cout << temp1;
			}
			else
			{
				if(sum < j)
				{
					count += j - sum;
					sum = j;
				}
				sum += temp1;
			}
		}
		f2 << "Case #" << i << ": " << count<<endl;
		i++;
	}
}