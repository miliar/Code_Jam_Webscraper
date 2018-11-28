#include <iostream>
#include <vector>
using namespace std;

int groupAndCal(std::string seq) {
	std::vector<char> seqVec;
	if (seq.length() == 0)
		return 0;

	int end = 0;
	seqVec.push_back(seq.at(0));
	for (int i = 1; i < seq.length(); i++)
	{
		if (seq.at(i) != seqVec[end])
		{
			seqVec.push_back(seq.at(i));
			end++;
		}
	}
	int i = seqVec.size() - 1;
	while (seqVec[i] != '-' && i >= 0)
	{
		i--;
	}
	return i+1;
}

int main() {
	int T;
	string seq;
	std::cin >> T;
	int res = 0;
	for (int i = 1; i <= T; i++) 
	{
		std::cin >> seq;
		res = groupAndCal(seq);
		cout << "Case #" << i << ": " << res << endl;
	}

}

