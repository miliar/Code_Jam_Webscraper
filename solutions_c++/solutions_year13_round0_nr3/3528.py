#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool palindrome(int param)
{
	char all[50];
	int size = 0;
	if(param < 10)
		return true;
	else
	{
		while(param>10)
		{
			all[size] = param%10;
			param = param/10;
			size++;
		}
		
		all[size] = param;
		size++;

		for(int i=0; i<size; i++)
		{
			if(all[i] == all[size-1-i])
				continue;
			else
				return false;
		}
		return true;
	}
}


int main()
{
	ifstream input("E:\\input1.txt");
	ofstream output("E:\\output.txt");

	vector<int> all;
	for(int i=0; i<40; i++)
	{
		if(palindrome(i) && palindrome(i*i))
			all.push_back(i*i);
	}

	int total;
	input>>total;
	for(int i=0; i<total; i++)
	{
		int a,b,size = 0;
		input>>a>>b;
		for(unsigned int j=0; j<all.size(); j++)
		{
			if(all[j]<=b && all[j]>=a)
			{
				size++;
			}
		}
		output<<"Case #"<<i+1<<": "<<size<<endl;
	}
	return 0;
}