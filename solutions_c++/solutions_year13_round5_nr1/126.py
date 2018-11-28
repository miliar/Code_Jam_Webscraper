#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int T;
long long B;
long long you[37], me[37], bak[37];
int N;
long double ret;

vector<long long> event;

void Go(long long input)
{
	int index;
	int l1, l2;

	long double prob;
	long double gain;

	index = 0;
	for(l2 = 0; l2 < 37; l2++)
	{
		if(me[l2] + you[l2] < me[index] + you[index])
		{
			index = l2;
		}
	}
	prob = 0;
	for(l2 = 0; l2 < 37; l2++)
	{
		if(me[l2] + you[l2] == me[index] + you[index])
		{
			prob = prob + (long double)1;
		}
	}
	prob = (long double)1 / prob;

	gain = 0;
	for(l2 = 0; l2 < 37; l2++)
	{
		if(me[l2] + you[l2] == me[index] + you[index])
		{
			gain += prob * (long double)me[l2] * (long double)36;
		}
	}

	if(ret < gain - (long double)input)
	{
		ret = gain - (long double)input;
	}
}

int main(void)
{
	int l0, l1, l2;

	cin >> T;
	for(l0 = 1; l0 <= T; l0++)
	{
		cin >> B >> N;
		for(l1 = 0; l1 < 37; l1++) you[l1] = me[l1] = 0;

		event.clear();
		for(l1 = 0; l1 < N; l1++)
		{
			cin >> you[l1];
			event.push_back(you[l1] - 1);
			event.push_back(you[l1]);
			event.push_back(you[l1] + 1);
		}
		event.push_back(0);
		event.push_back(1);

		sort(event.begin(), event.end());

		ret = 0;


		for(l1 = 0; l1 < (int)event.size(); l1++)
		{
			if(event[l1] < 0) continue;
			if(l1 + 1 < (int)event.size())
			{
				if(event[l1] == event[l1+1])
				{
					continue;
				}
			}

			for(l2 = 0; l2 < 37; l2++) me[l2] = 0;

			long long acc =0;
			for(l2 = 0; l2 < 37; l2++)
			{
				if(you[l2] + me[l2] < event[l1])
				{
					me[l2] = event[l1] - you[l2];
					acc += me[l2];
				}
			}

			if(acc > B) break;
			Go(acc);

			long long bakacc = acc;
			for(l2 = 0; l2 < 37; l2++) bak[l2] = me[l2];

			long long more = B - acc;
			if(more > 100) more = 100;
			while(more > 0)
			{
					int index = 0;
					for(l2 = 0; l2 < 37; l2++)
					{
						if(me[l2] + you[l2] < me[index] + you[index])
						{
							index = l2;
						}
						if(me[l2] + you[l2] == me[index] + you[index])
						{
							if(you[l2] > you[index]) index = l2;
						}
					}
					me[index]++;
					acc++;
					Go(acc);
					more--;
			}

			acc = bakacc;
			for(l2 = 0; l2 < 37; l2++) me[l2] = bak[l2];







			long long down = 0;
			for(l2 = 0; l2 < 37; l2++)
			{
				if(you[l2] + me[l2] == event[l1])
				{
					down++;
				}
			}
			if(down > 0)
			{
				long long plus = (B - acc) / down;
				plus--;
				if(plus < 0) plus = 0;
				if(plus > 0)
				{
					for(l2 = 0; l2 < 37; l2++)
					{
						if(you[l2] + me[l2] == event[l1])
						{
							me[l2] += plus;
						}
					}
				}
				Go(acc + plus * down);

				acc += plus * down;

				long long final = B - acc;
				if(final > 100) final = 100;
				while(final > 0)
				{
					int index = 0;
					for(l2 = 0; l2 < 37; l2++)
					{
						if(me[l2] + you[l2] < me[index] + you[index])
						{
							index = l2;
						}
						if(me[l2] + you[l2] == me[index] + you[index])
						{
							if(you[l2] > you[index]) index = l2;
						}
					}
					me[index]++;
					acc++;
					Go(acc);
					final--;
				}
			}
		}


		printf("Case #%d: %.12Lf\n", l0, ret);
	}
}
