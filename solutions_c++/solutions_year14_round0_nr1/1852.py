#include<fstream>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<set>
using namespace std;

int main()
{
	ifstream in("G:\\job\\google_jam\\data\\A-small-attempt0.in");
	ofstream out("G:\\job\\google_jam\\data\\A-large-practice.out");
	if(!(in && out))
	{
		cout << " Can not open file" << endl;
		return 1;
	}
	int case_num;
	in >> case_num;
	for(int i = 1; i <= case_num; ++i)
	{
		int first, second;
		vector<int> row_first(4), row_second(4);
		// read first records
		in >> first; 
		for(int i = 0; i < first-1; ++i)
		{
			int temp;
			in >> temp >> temp >> temp >> temp;
		}
		in >> row_first[0] >> row_first[1] >> row_first[2] >> row_first[3];
		for(int i = 0; i < 3 - (first -1); ++i)
		{
			int temp;
			in >> temp >> temp >> temp >> temp;
		}
		// read second records
		in >> second;
		for(int i = 0; i < second-1; ++i)
		{
			int temp;
			in >> temp >> temp >> temp >> temp;
		}
		in >> row_second[0] >> row_second[1] >> row_second[2] >> row_second[3];
		for(int i = 0; i < 3 - (second -1); ++i)
		{
			int temp;
			in >> temp >> temp >> temp >> temp;
		}

		// get answer
		//set<int> first_set(row_first.begin(), row_first.end());
		//set<int> second_set(row_second.begin(), row_second.end());
		vector<int>::iterator it;
		vector<int> result(8);
		sort(row_first.begin(), row_first.end());
		sort(row_second.begin(), row_second.end());
		it = set_intersection(row_first.begin(),row_first.end(), row_second.begin(),row_second.end(), result.begin());
		result.resize(it-result.begin());
		out << "Case #" << i << ": ";
		if(result.size() == 0)
		{
			out << "Volunteer cheated!" << endl;
		}
		else if(result.size() > 1)
		{
			out << "Bad magician!" << endl;
		}
		else
		{
			out << result[0] << endl;
		}
	}

	out.close();
	in.close();
}