#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

bool check_horizontal(int i, int j, vector<vector<int>>& pattern) {
	auto row = pattern.at(i);
	int target = row.at(j);
	for(auto h : row) {
		if(h > target) return false;
	}

	return true;
}

bool check_vertical(int i, int j, vector<vector<int>>& pattern) {
	int target = pattern.at(i).at(j);
	for(auto row : pattern) {
		if(row.at(j) > target) return false;
	}

	return true;
}

int main(int argc, char const *argv[])
{
	ifstream ifs(argv[1]);
	int ncases;
	ifs >> ncases;

	for (int casenum = 1; casenum < ncases+1; ++casenum) {
		int width, height;
		ifs >> height >> width;

		vector<vector<int>> pattern;
		set<int> heights;

		for(int i=0; i<height; ++i) {
			pattern.push_back( vector<int>() );
			for (int j = 0; j < width; ++j)
			{
				int tmp;
				ifs >> tmp;
				pattern.at(i).push_back(tmp);
				heights.insert(tmp);
			}
		}

		vector<int> sorted_heights(heights.begin(), heights.end());
		sort(sorted_heights.begin(), sorted_heights.end());
		reverse(sorted_heights.begin(), sorted_heights.end());

		bool solvable=true;
		for (int i = 0; i < sorted_heights.size(); ++i)
		{
			int current_height = sorted_heights.at(i);
			for (int i = 0; i < height; ++i)
			{
				for (int j = 0; j < width; ++j)
				{
					if(pattern.at(i).at(j) == current_height && !(check_horizontal(i,j,pattern) || check_vertical(i,j,pattern))) {
						solvable = false;
						goto nextcase;
					}
				}
			}
		}

nextcase:
		if(solvable) {
			cout << "Case #" << casenum << ": YES" << endl;
		} else {
			cout << "Case #" << casenum << ": NO" << endl;
		}
	}

	return 0;
}

