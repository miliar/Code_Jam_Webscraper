#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool bad(vector <pair<int, string> > votes) {
	if (votes.size() == 2)
		return (votes[0].first == votes[1].first);
	return votes[0].first == votes[1].first && votes[2].first == 0;
}

struct cmp_obj {
    bool operator()(pair<int, string> a, pair<int, string> b) {
    	if (a.first == b.first)
    		return a.second < b.second;
        return a.first > b.first;
    }
} cmp_func;

int main() {
	int tests, N;
	cin >> tests;
	for (int case_no = 1; case_no <= tests; ++case_no) {
		cin >> N;
		vector <pair <int, string> > votes;
		vector <string> answer;
		int vote;
		string s = " ";
		for (int i = 0; i < N; ++i) {
			cin >> vote;
			s[0] = i + 'A';
			votes.push_back(make_pair(vote, s));
		}

		while (true) {
			sort(votes.begin(), votes.end(), cmp_func);
			if (votes[0].first == 0)
				break;
			if (bad(votes)) {
				votes[0] = make_pair(votes[0].first - 1, votes[0].second);
				votes[1] = make_pair(votes[1].first - 1, votes[1].second);
				answer.push_back(votes[0].second + "" + votes[1].second);
			} else {
				votes[0] = make_pair(votes[0].first - 1, votes[0].second);
				answer.push_back(votes[0].second);
			}
		}
		string answer_str = "";
		for (int i = 0; i < answer.size(); ++i) {
			if (i > 0) answer_str += " ";
			answer_str += answer[i];
		}
		cout << "Case #" << case_no << ": " << answer_str << endl;
	}
}