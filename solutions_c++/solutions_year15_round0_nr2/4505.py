#include <iostream>
#include <functional>
#include <fstream>
#include <vector>
#include <cassert>

using namespace std;

#define PANCAKES 1
#define AUDIANCE 0


#if PANCAKES

bool over(vector<int>&cakes)
{
	for (int i = 0; i < cakes.size(); i++)
	{
		if (cakes[i] != 0) return false;
	}
	return true;
}

int min(vector<int>&vec)
{
	assert(vec.size() > 0);
	int min = vec[0]; int indx = 0;
	for (int i = 1; i < vec.size(); i++)
	{
		if (vec[i] < min)
		{
			min = vec[i]; indx = i;
		}
	}
	return indx;
}


#include <queue>

priority_queue<int, std::vector<int>, std::greater<int> > options;
vector<int> pancakes;


int minute;

int max(vector<int>&vec)
{
	assert(vec.size() > 0);
	int max = vec[0]; int indx = 0;
	for (int i = 1; i < vec.size(); i++)
	{
		if (vec[i] > max)
		{
			max = vec[i]; indx = i;
		}
	}
	return indx;
}

void split(vector<int> &cakes, int m,int num)
{
	cakes[m] -= num;
	cakes.push_back(num);
}

void eat(vector<int> &cakes)
{
	for (int i = 0; i < cakes.size(); i++)
		cakes[i]--;
}

void solve(vector<int>&cakes, int m)
{
	vector<int> c2;
	int mx = max(cakes);
	if (cakes[mx] == 0)
	{
		options.push(m);
//		cout << m << endl;
		return;
	}
	if (options.size() > 0 && m >= options.top())
	{
		return;
	}
	c2 = cakes;
	eat(c2);
	solve(c2, m + 1);


	if (cakes[mx] > 3)
	{
		for (int i = cakes[mx] -2 ; i >= sqrt(cakes[mx]); i--)
		{
			c2 = cakes;
			split(c2, mx,i);
			solve(c2, m + 1);
		}
	}
}


int main()
{
	

	ifstream in("input.in");
	ofstream out("out.txt");
	assert(!in.fail());
	assert(!out.fail());
	int ncase; in >> ncase;
	for (int icase = 0; icase < ncase; icase++)
	{
		options = priority_queue<int,std::vector<int>, std::greater<int>>();
		out << "Case #" << icase + 1 << ": ";
		pancakes.clear(); int N; in >> N;
		pancakes = vector<int>(N);

		for (int i = 0; i < N; i++)
			in >> pancakes[i];
		minute = 0;
		solve(pancakes,0);
		out << options.top() << endl;
	}
	system("pause");
}



#endif

#if AUDIANCE

bool all_up(vector<int> aud)
{
	if (aud.size() < 1)
		return true;
	int total = aud[0];
	for (int i = 1; i < aud.size() || total < aud.size(); i++)
	{
		if (total >= i)
		{
			total += aud[i];
		}
		else
		{
			return false;
		}
	}
	return true;
}


int main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
	assert(!in.fail());
	assert(!out.fail());
	int ncase; in >> ncase;
	for (int icase = 0; icase < ncase; icase++)
	{
		out << "Case #" << icase + 1 << ": ";
		int N; in >> N;
		N++;
		char c;
		vector<int> aud(N);
		for (int i = 0; i < N; i++)
		{
			in >> c;
			aud[i] = c - '0';
		}
		int tot = 0;
		while (!all_up(aud))
		{
			tot++;
			aud[0]++;
		}
		out<<tot<<endl;
	}
}


#endif
