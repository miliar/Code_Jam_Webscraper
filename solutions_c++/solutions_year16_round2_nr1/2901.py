#include <iostream>
#include <algorithm>
#include <bitset>
#include <string.h>
#include <fstream>
#include <vector>

using namespace std;

vector<string> AlphaList;
vector<pair<int, char>> Order;

void CheckAndDelete(
	vector<int>& Alpha, 
	vector<int>& sol, 
	int Target)
{
	auto t = Order[Target];
	int count = Alpha[t.second-'A'];
	for (int i = 0; i < count; i++)
		sol.push_back(t.first);

	auto k = AlphaList[t.first];
	for (int i = 0; i < count; i++)
	{
		for (int j = 0; j < k.size(); j++)
			Alpha[k[j]-'A']--;
	}
}

int main()
{
#ifdef _DEBUG
	istream& in = cin;
	ostream& ot = cout;
#else
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	istream& in = fin;
	ostream& ot = fout;
#endif
	int T;
	in >> T;

	AlphaList.push_back("ZERO");
	AlphaList.push_back("ONE");
	AlphaList.push_back("TWO");
	AlphaList.push_back("THREE");
	AlphaList.push_back("FOUR");
	AlphaList.push_back("FIVE");
	AlphaList.push_back("SIX");
	AlphaList.push_back("SEVEN");
	AlphaList.push_back("EIGHT");
	AlphaList.push_back("NINE");

	Order.push_back({ 0, 'Z' });
	Order.push_back({ 2, 'W' });
	Order.push_back({ 6, 'X' });
	Order.push_back({ 7, 'S' });
	Order.push_back({ 5, 'V' });
	Order.push_back({ 4, 'F' });
	Order.push_back({ 3, 'R' });
	Order.push_back({ 8, 'G' });
	Order.push_back({ 1, 'O' });
	Order.push_back({ 9, 'I' });

	for (int t = 1; t <= T; t++)
	{
		string str;
		in >> str;
		vector<int> Alpha(27, 0);
		for (int i = 0; i < str.size(); i++)
			Alpha[str[i]-'A']++;

		vector<int> sol;
			
		for (int i = 0; i < Order.size(); i++)
			CheckAndDelete(Alpha, sol, i);

		sort(sol.begin(), sol.end());

		string w;
		for (int i = 0; i < sol.size(); i++)
			w += (char)(sol[i] + '0');

		ot << "Case #" << t << ": " << w << endl;
	}

	return 0;
}

