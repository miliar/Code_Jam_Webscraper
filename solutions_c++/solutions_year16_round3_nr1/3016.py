#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

bool cmp(const pair<char, int> a, const pair<char, int> b) 
{
	return a.second > b.second;
}

bool ifEnd(vector< pair<char, int> > &partySen) {
	if (partySen.size() >= 3 && partySen[0].second == 1 && partySen[1].second == 1 && partySen[2].second == 1) 
	{
		if (partySen.size() == 3) 
		{
			return true;
		}
		else {
			if (partySen[0].second == 0) 
			{
				return true;
			}
		}

	}
	return false;
}

int main() {
	fstream in;
	in.open("C://1.in", ios::in);
	if (in.fail()){
		cerr << "Open graph file inputfile error!" << endl;
		return false;
	}
	ofstream outfile("C://output1.txt");
	if (!outfile){
		cout << "Unable to open outfile";
		exit(1); 
	}
	const int BUFFER_LENGTH = 100000;
	char buffer[BUFFER_LENGTH] = { 0 };
	int CaseNum = 0;
	in.getline(buffer, BUFFER_LENGTH);
	CaseNum = atoi(buffer);
	
	for (int c = 1; c <= CaseNum; c++) 
	{
		int N;
		in >> N;
		vector< pair<char, int> > partySen;
		for (int i = 0; i < N; i++) 
		{
			pair<char, int> senator;
			senator.first = 'A' + i;
			in >> senator.second;
			partySen.push_back(senator);
		}
		sort(partySen.begin(), partySen.end(), cmp);
		outfile << "Case #" << c << ": ";
		while (partySen[0].second != 0) 
		{
			if (ifEnd(partySen)) {
				outfile << partySen[0].first << " " << partySen[1].first << partySen[2].first;
				break;
			}
			else {
				outfile << partySen[0].first;
				partySen[0].second--;
				if (partySen[0].second >= partySen[1].second) 
				{
					outfile << partySen[0].first;
					partySen[0].second--;
				}
				else {
					outfile << partySen[1].first;
					partySen[1].second--;
				}
				outfile << " ";
				sort(partySen.begin(), partySen.end(), cmp);
			}
		}
		outfile << endl;
	}
	in.close();
	outfile.close();
	return 0;
}