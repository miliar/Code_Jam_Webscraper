#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("A.txt");
	ofstream out("A_ans.txt");

	int testnum;
	in >> testnum;
	for (int t = 0; t < testnum; t++)
	{
		vector<int> first;
		int a1, temp;
		in >> a1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				in >> temp;
				if (i+1 == a1)
					first.push_back(temp);
			}

		vector<int> second;
		int a2;
		in >> a2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				in >> temp;
				if (i+1 == a2)
					second.push_back(temp);
			}

		
		sort(first.begin(), first.end());
		sort(second.begin(), second.end());
		vector<int> v(4);
		set_intersection (first.begin(), first.end(), second.begin(), second.end(), v.begin());

		out << "Case #" << t+1 << ": ";
		if (v[1] != 0)
			out << "Bad magician!" << endl;
		else
		if (v[0] == 0)
			out << "Volunteer cheated!" << endl;
		else
			out << v[0] << endl;
	}
	return 0;
}


