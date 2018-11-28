#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	vector<int> res;
	int T;
	fin >> T;
	for(int t=0; t<T; t++)
	{
		res.clear();
		int tmp;
		int a1, a2;
		int nums[4];
		fin >> a1;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				fin >> tmp;
				if(i==a1-1)
					nums[j] = tmp;
			}
		}
		fin >> a2;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				fin >> tmp;
				if(i==a2-1)
				{
					for(int k=0; k<4; k++)
					{
						if(nums[k]==tmp)
							res.push_back(tmp);
					}
				}
			}
		}
		if(res.size()==0)
		{
			fout<< "Case #" << t+1 << ": Volunteer cheated!\n";
		}
		if(res.size()==1)
		{
			fout<< "Case #" << t+1 << ": " << res[0] << "\n";
		}
		if(res.size()>1)
		{
			fout<< "Case #" << t+1 << ": Bad magician!\n";
		}
	}
	fout.close();
	return 0;
}
