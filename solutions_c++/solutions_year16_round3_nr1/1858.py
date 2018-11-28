#include <iostream>
#include <stdio.h>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int N;
int arr[31];
int total;
deque<pair<int, int> > vp;


bool rec1()
{
	
	if (total == 0)
	{
		while (!vp.empty())
		{
			pair<int, int> pi = vp.front();
			vp.pop_front();

			if (pi.second != -1)
			{
				char c1 = pi.first + 'A';
				char c2 = pi.second + 'A';
				cout << c1 << c2 << " ";
			}
			else
			{
				char c1 = pi.first + 'A';
				cout << c1 << " ";
			}
		}
		cout << endl;
		return true;
	}

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			if (arr[i] == 0 || arr[j] == 0) continue;
			if (i == j && arr[i] <= 1) continue;
			//시도해본다
			arr[i]--;
			arr[j]--;
			total -= 2;

			bool b = false;
			for (int k = 0; k < N; ++k)
			{
				double ttmp = (double)arr[k] / (double)total;
				if (ttmp > 0.5){
					b = true;
					break;
				}
			}
			if (!b)
			{
				//되었을때
				vp.push_back(make_pair(i, j));
				if (rec1())
					return true;
				vp.pop_back();

				arr[i]++;
				arr[j]++;
				total += 2;
			}
			else
			{
				arr[i]++;
				arr[j]++;
				total += 2;
			}
		}
	}

	for (int i = 0; i < N; ++i)
	{
		if (arr[i] == 0) continue;
		arr[i]--;
		total -= 1;

		bool b = false;
		for (int k = 0; k < N; ++k)
		{
			double ttmp = (double)arr[k] / (double)total;
			if (ttmp > 0.5){
				b = true;
				break;
			}
		}

		if (!b)
		{
			//되었을때
			vp.push_back(make_pair(i, -1));
			if (rec1())
				return true;
			vp.pop_back();

			arr[i]++;
			total += 1;
		}
		else
		{
			arr[i]++;
			total += 1;
		}
	}

	return false;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T;
	scanf("%d", &T);
	int ts = 1;
	while (T--)
	{
		cout << "Case #" << ts++ << ": ";

		total = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
		{
			int tmp;
			scanf("%d", &tmp);
			arr[i] = tmp;
			total += tmp;
		}

		rec1();
	}

}