#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <fstream>
#include <sstream>
#include <istream>
#include <unordered_map>
#include <set>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for (int i = 0; i<numCases; i++)
	{
		int numSenator;
		cin >> numSenator;

		vector<int> senators;
		int tmp;
		for (int i = 0; i < numSenator; i++){
			cin >> tmp;
			senators.push_back(tmp);
		}

		set<pair<int, int>> set_senators;
		for (int i = 0; i < numSenator; i++){
			set_senators.insert(make_pair(senators[i], i));
		}

		auto it = set_senators.rbegin();
		auto it2 = set_senators.rbegin();
		it2++;

		string res;

		int diff = it->first - it2->first;
		while (diff != 0){
			diff--;
			res += 'A' + it->second;
			res += " ";
		}

		it2++;
		while (it2 != set_senators.rend()){
			int tmp = it2->first;
			while (tmp != 0 && tmp!=1){
				res += 'A' + it2->second;
				res += 'A' + it2->second;
				res += " ";
				tmp -= 2;
			}
			if (tmp == 1){
				res += 'A' + it2->second;
				res += " ";
			}
			it2++;
		}

		it2 = set_senators.rbegin();
		it2++;

		int tmpNum = it2->first;
		while (tmpNum != 0){
			res += 'A' + it->second;
			res += 'A' + it2->second;
			res += " ";
			tmpNum--;
		}

		int size = res.size();
		string finalRes = res.substr(0, size - 1);
		

		cout << "Case #" << i + 1 << ": " << finalRes << endl;
	}

	return 0;
}