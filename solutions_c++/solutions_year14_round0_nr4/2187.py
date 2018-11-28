#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> naomi, ken;
int N;

int deceit();
int war();
bool checkAll(int start);

int main()
{
	ifstream cin("DeceitfulWar.in");
	ofstream cout("DeceitfulWar.txt");

	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		naomi.clear();
		ken.clear();
		cin >> N;
		for(int i = 0; i < N; i++)
		{
			double temp;
			cin >> temp;
			naomi.push_back(temp);
		}
		for(int i = 0; i < N; i++)
		{
			double temp;
			cin >> temp;
			ken.push_back(temp);
		}

		cout << "Case #" << t + 1 << ": " << deceit() << " " << war() << endl;
	}

	return 0;
}

int deceit()
{
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	reverse(ken.begin(), ken.end());

	for(int i = 0; i < N; i++)
	{
		if(naomi[i] > ken[i] || checkAll(i))
			return N - i;
	}

	return 0;
}

int war()
{
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	reverse(naomi.begin(), naomi.end());
	reverse(ken.begin(), ken.end());

	int count = 0;
	for(int i = 0; i < N; i++)
	{
		if(naomi[i] > ken[i - count]) count++;
	}

	return count;
}

bool checkAll(int start)
{
	for(int i = start, j = N - 1; i < N; i++, j--)
	{
		if(naomi[i] < ken[j]) return false;
	}

	return true;
}
