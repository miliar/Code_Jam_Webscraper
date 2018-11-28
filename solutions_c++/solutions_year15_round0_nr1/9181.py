#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool checkstandingovation(int extraguests, int smax, vector<int> t)
{
	bool lastguestreached = true;
	int standingguestcount = 0;
	for (int i = 0; i <= smax; ++i)
	{
		if((standingguestcount + extraguests) >= i)
		{
			standingguestcount += t.at(i);
		}
		else lastguestreached = false;
	}
	return lastguestreached;
}

int main(int argc, char const *argv[])
{
	ifstream in("large.in");
	ofstream out("out.txt");
	int T;
	in >> T;
	vector<vector<int > > t;
	vector<int> smax;
	vector<int> extraguests;
	for (int i = 0; i < T; ++i)
	{
		t.push_back(vector<int>());
		int temp;
		in >> temp;
		smax.push_back(temp);
		string temp2;
		in >> temp2;
		for (int j = 0; j <= smax.at(i); ++j)
		{
			t.at(i).push_back(temp2[j] - 48);
		}
	}
	for (int i = 0; i < T; ++i)
	{
		extraguests.push_back(0);
		while(!checkstandingovation(extraguests.at(i),smax.at(i),t.at(i)))
		{
			extraguests.at(i) = extraguests.at(i) + 1;
		}
		out << "Case #" << i+1 << ": " << extraguests.at(i) << endl;	
	}
	return 0;
}