#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <cassert>

using namespace std;

int main()
{

	int T;
	cin >> T;
	for (auto casen = 1; casen <= T; ++casen) {
		int parties;
		cin >> parties;
		vector<int> party_members(parties);
		int total_members = 0;
		for (int i = 0; i < parties; ++i) {
			cin >> party_members[i];
			total_members += party_members[i];
		}
		cout << "Case #" << casen << ": ";
		int cur_group = 0;
		while (total_members > 2) {
			int max_c = -1, max_p = -1;
			for (int i = 0; i < parties; ++i) {
				if (party_members[i] > max_c) {
					max_c = party_members[i];
					max_p = i;
				}
			}
			cout << static_cast<char>('A' + max_p);
			cur_group++;
			--party_members[max_p];
			--total_members;
			if (cur_group == 2 || (cur_group == 1 && total_members == 2)) {
				cout << ' ';
				cur_group = 0;
			}
		}
		for (int i = 0; i < parties; ++i) {
			if (party_members[i] != 0) {
				assert(party_members[i] == 1);
				cout << static_cast<char>('A' + i);
			}
		}
		cout << endl;
	}
	return 0;
}

