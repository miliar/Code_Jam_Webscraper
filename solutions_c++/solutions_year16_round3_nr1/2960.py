#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <utility>

using namespace std;

bool cmp(pair<char, int> i, pair<char, int> j) {
	return (i.second < j.second);
}

int main() {
	ifstream in("A-small-attempt2.in");
	ofstream out("smalloutput.txt");
	int caseNum;
	in >> caseNum;
	for (int i = 1; i <= caseNum; ++i) {
		int N;
		in >> N;
		vector<pair<char, int>> parties;
		for (int j = 0; j < N; ++j) {
			int p;
			in >> p;
			parties.push_back(pair<char, int>(j + 'A', p));
		}

		sort(parties.begin(), parties.end(), cmp);
		
		out << "Case #" << i << ": ";
		int p = N - 1;
		int pre = parties[p].second;
		while (true) {
			if (p == N - 1) {
				if (parties[p].second == 0)
					break;
				if (parties[p].second == 1 && p == 2) {
					out << parties[p].first << " " << parties[p - 1].first << parties[p - 2].first << " ";
					break;
				}
				pre = parties[p].second;
				if (parties[p].second == parties[p - 1].second) {
					out << parties[p].first << parties[p - 1].first << " ";
					parties[p].second--;
					parties[p - 1].second--;
					if (p == 1){
						p = N - 1;
					}
					else
						p -= 2;
				}
				else {
					out << parties[p].first << " ";
					parties[p].second--;
					p--;
				}
			}
			else {
				if (parties[p].second != pre) {
					p = N - 1;
				}
				else{
					if (parties[p].second == 1 && p == 2) {
						out << parties[p].first << " " << parties[p - 1].first << parties[p - 2].first << " ";
						break;
					}
					if (p == 0) {
						out << parties[p].first << " ";
						parties[p].second--;
						p=N-1;
					}
					else{
						if (parties[p].second == parties[p - 1].second) {
							out << parties[p].first << parties[p - 1].first << " ";
							parties[p].second--;
							parties[p - 1].second--;
							p -= 2;
						}
						else {
							out << parties[p].first << " ";
							parties[p].second--;
							p--;
						}
					}
				}
			}
		}
		out << endl;
	}
	return 0;
}
