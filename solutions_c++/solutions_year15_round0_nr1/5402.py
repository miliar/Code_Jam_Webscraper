#include <iostream>
#include <fstream>
#include <vector>
#include <cassert>

using namespace std;

#define PANCAKES 0
#define AUDIANCE 1


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
int main()
{
	vector<int> pancakes;

	ifstream in("test.txt");
	ofstream out("out.txt");
	assert(!in.fail());
	assert(!out.fail());
	int ncase; in >> ncase;
	for (int icase = 0; icase < ncase; icase++)
	{
		out << "Case #" << icase + 1 << ": ";
		pancakes.clear(); int N; in >> N;
		pancakes = vector<int>(N);

		vector<int> options;

		for (int i = 0; i < N; i++)
			in >> pancakes[i];
		int minute = 0;
		while (!over(pancakes))
		{
			//push back eat out
			int most = max(pancakes);
			options.push_back(pancakes[most]+ minute);
			if (pancakes[most] > 2)
			{
				if (pancakes[most] % 2 == 1)
				{
					pancakes.push_back(pancakes[most] / 2);
					pancakes[most] = pancakes[most] / 2 + 1;
				}
				else
				{
					pancakes.push_back(pancakes[most] / 2);
					pancakes[most] = pancakes[most] / 2;
				}
				minute ++;
			}
			else
			{
				break;
			}
		}
		options.push_back(minute + pancakes[max(pancakes)]);
		out << options[min(options)] << endl;
	}
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
