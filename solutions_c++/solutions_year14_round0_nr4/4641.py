#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int war(const vector<double>& naomi, const vector<double>& ken);
int dwar(const vector<double>& naomi, const vector<double>& ken);

int main()
{
	int T;
	cin >> T;

	for (int test = 1; test <= T; test++)
	{
		int N;
		cin >> N;

		vector<double> naomi, ken;

		for (int i = 0; i < N; i++)
		{
			double mass;
			cin >> mass;

			naomi.push_back(mass);
		}

		for (int i = 0; i < N; i++)
		{
			double mass;
			cin >> mass;

			ken.push_back(mass);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int score_war = war(naomi, ken);
		int score_dwar = dwar(naomi, ken);

		cout << "Case #" << test << ": " << score_dwar << " "
			<< score_war << endl;	
	}

	return 0;
}

void print(const string& s, const vector<double>& v)
{
	int size = v.size();

	cout << s << ": ";

	for (int i = 0; i < size; i++)
		cout << "[" << v[i] << "]";

	cout << endl;
}

int 
war(const vector<double>& naomi, const vector<double>& ken)
{
	int size = naomi.size();
	int score = 0;

	vector<double> k(ken);

//	cout << "\n=======\n";
	for (int i = size - 1; i >= 0; i--)
	{
		int pos = i;
//		cout << "\n -> pos = " << pos << endl;
//		print("naomi", naomi);
//		print("ken", k);

//		cout << "naomi = " << naomi[i] << endl;

		if (k[pos] < naomi[i])
		{
//			cout << "ken lose = " << k[0] << endl;
			k.erase(k.begin());
			score++;
			continue;
		}

		while (pos >= 0 and k[pos] > naomi[i])
			pos--;
		pos++;

//		cout << "Choice = " << pos << endl;
//		cout << "ken win = " << k[pos] << endl;
		k.erase(k.begin() + pos);	
	}

	return score;
}

int 
dwar(const vector<double>& naomi, const vector<double>& ken)
{
	int size = naomi.size();
	int score = 0;

	vector<double> n(naomi), k(ken);

//	cout << "\n=======\n";
	while (size > 0)
	{
		int max = size - 1;
		size--;

//		print("naomi", n);
//		print("ken", k);

		if (n[0] < k[0])
		{
//			cout << "naomi = " << n[0] << endl;
//			cout << "ken win = " << k[max] << endl;
			
			n.erase(n.begin());
			k.erase(k.begin() + max);	
			continue;
		}

//		cout << "ken lose = " << k[0] << endl;
//		cout << "naomi = " << n[0] << endl;
		k.erase(k.begin());
		n.erase(n.begin());
		score++;
	}

	return score;
}

