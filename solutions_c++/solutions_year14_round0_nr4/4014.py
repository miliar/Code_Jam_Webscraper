#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

double p2_strat(double p1_pick, vector<double> &p2)
{
	double p2_pick;

	vector<double>::iterator it = upper_bound(p2.begin(), p2.end(), p1_pick);
	if(it==p2.end())
	{
		// pick smallest
		p2_pick = p2[0];
		p2.erase(p2.begin());
	}
	else
	{
		p2_pick = *it;
		p2.erase(it);
	}

	return p2_pick;
}


int random_check_once(int N, vector<double> &p1, vector<double> &p2)
{
	int score = 0;

	for(int i=0; i<N; i++)
	{
		// pick p1's smallest
		double p1_pick = p1[0];
		p1.erase(p1.begin());

		// make optimal pick for p2
		double p2_pick = p2_strat(p1_pick, p2);

		if(p1_pick>p2_pick)
		{
			score++;
		}
	}


	return score;
}


int random_check(int N, vector<double> &p1, vector<double> &p2)
{
	int score = 0;

	for(int i=0; i<1000; i++)
	{

	}

	return score;
}

int deceitful_war(int N, vector<double> &p1, vector<double> &p2)
{
	vector<double> p1_copy(p1), p2_copy(p2);

	int score = 0;

	for(int i=0; i<N; i++)
	{
		// if p1's max is less than p2's max

		if(p1[0] < p2[0])
		{
			p1.erase(p1.begin());
			p2.erase(p2.end()-1);
		}
		else
		{
			p1.erase(p1.begin());
			p2.erase(p2.begin());

			score++;
		}
	}

	int score2 = random_check(N, p1_copy, p2_copy);

	if(score2>score)
	{
		cout << "OH NO OH NO OH NO" << endl;
		cout << "OH NO OH NO OH NO" << endl;
		cout << "OH NO OH NO OH NO" << endl;
	}

	return score;
}

int war(int N, vector<double> &p1, vector<double> &p2)
{
	int score = 0;

	for(int i=0; i<N; i++)
	{
		// pick p1's smallest
		double p1_pick = p1[0];
		p1.erase(p1.begin());

		// make optimal pick for p2
		double p2_pick = p2_strat(p1_pick, p2);

		if(p1_pick>p2_pick)
		{
			score++;
		}
	}


	return score;
}

int main(int argc, char const *argv[])
{
	int T;

	cin >> T;

	for(int i=0; i<T; i++)
	{
		int N;
		cin >> N;

		vector<double> naomi(N), ken(N);

		for(int j=0; j<N; j++)
		{
			cin >> naomi[j];
		}

		for(int j=0; j<N; j++)
		{
			cin >> ken[j];
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		vector<double> p1_1(naomi);
		vector<double> p1_2(naomi);
		vector<double> p2_1(ken);
		vector<double> p2_2(ken);

		int x,y,z;

		x = i+1;
		y = deceitful_war(N, p1_1, p2_1);
		z = war(N, p1_2, p2_2);

		cout << "Case #" << x << ": " << y << " " << z << endl;
	}

	return 0;
}