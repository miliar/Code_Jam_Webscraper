#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int n, temp, count;
	int row1, row2;
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("A-small-attempt0.out");
	vector<int> v1, v2, re(4, 0);
	vector<int>::iterator it;
	in >> n;
	for(int i=0;i<n;++i)
	{
		in >> row1;
		count = 0;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				in >> temp;
				if(row1==j+1)
				{
					v1.push_back(temp);
				}
			}
		}
		in >> row2;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				in >> temp;
				if(row2==j+1)
				{
					v2.push_back(temp);
				}
			}
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		it = set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), re.begin());
		re.resize(it-re.begin()); 
		if(re.size() == 1)
			out << "Case #" << i+1 << ": " << re[0] << endl;
		else if(re.size()>1)
			out << "Case #" << i+1 << ": Bad magician!" << endl;
		else 
			out << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		v1.clear();
		v2.clear();
		re.resize(4);
	}
	return 0;
}