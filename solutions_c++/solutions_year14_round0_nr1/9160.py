#include <iostream>
#include <stack>
#include <string>
#include <fstream>
#include <set>
#include <algorithm>

using namespace std;




int main()
{
	int arr[5][5];
	int n,line1,line2;
	int time;

	ifstream fin("e:\\A-small-attempt1.in");
	ofstream fout("e:\\A-small-attempt1.out");


	fin>>n;



	for (int c=0;c<n;c++)
	{

	fin>>line1;

	set<int> intersect;
	set<int> s1;
	for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++)
		{
			fin>>arr[i][j];
			if (line1==i)
			{
				s1.insert(arr[i][j]);
			}
		}
	fin>>line2;
	set<int> s2;

	for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++)
		{
			fin>>arr[i][j];
			if (line2==i)
			{
				s2.insert(arr[i][j]);
			}
		}



	std::set_intersection( s1.begin(), s1.end(), s2.begin(), s2.end(),std::inserter( intersect, intersect.begin() ) );
	if (intersect.size()==1)
	{
		fout<<"Case #"<<c+1<<": "<<*(intersect.begin())<<endl;
	}
	else if (intersect.empty())
	{
		fout<<"Case #"<<c+1<<": Volunteer cheated!"<<endl;
	}
	else
	{
		fout<<"Case #"<<c+1<<": Bad magician!"<<endl;
	}

	}

	return 0;
}
