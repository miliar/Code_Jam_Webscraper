#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

struct Outfil
{
	int j, p, s;
};

int T, J, P, S, K;

vector<Outfil> outfils;
vector<Outfil> answer;

bool v[3 * 3 * 3];
int pair_jp[3][3];
int pair_js[3][3];
int pair_ps[3][3];

void func(int node, int count)
{
	if (node == outfils.size())
	{
		if (count < answer.size())
			return;

		memset(pair_jp, 0, sizeof(pair_jp));
		memset(pair_js, 0, sizeof(pair_js));
		memset(pair_ps, 0, sizeof(pair_ps));

		for (int i = 0; i < outfils.size(); ++i)
		{
			if (!v[i]) continue;

			Outfil o = outfils[i];
			pair_jp[o.j - 1][o.p - 1]++;
			pair_js[o.j - 1][o.s - 1]++;
			pair_ps[o.p - 1][o.s - 1]++;

			if (K < pair_jp[o.j - 1][o.p - 1]) return;
			if (K < pair_js[o.j - 1][o.s - 1]) return;
			if (K < pair_ps[o.p - 1][o.s - 1]) return;
		}

		answer.clear();
		for (int i = 0; i < outfils.size(); ++i)
		{
			if (!v[i]) continue;
			answer.push_back(outfils[i]);
		}

		return;
	}

	v[node] = false;
	func(node + 1, count);
	
	v[node] = true;
	func(node + 1, count + 1);
}

int main()
{

	FILE *in = fopen("input.txt", "rt");
	FILE *out = fopen("output.txt", "wt");

	fscanf(in, "%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		fscanf(in, "%d %d %d %d", &J, &P, &S, &K);
		
		outfils.clear();
		answer.clear();

		for (int j = 1; j <= J; ++j)
		{
			for (int p = 1; p <= P; ++p)
			{
				for (int s = 1; s <= S; ++s)
				{
					Outfil o;
					o.j = j;
					o.p = p;
					o.s = s;

					outfils.push_back(o);
				}
			}
		}

		func(0, 0);

		fprintf(out, "Case #%d: %d\n", t, answer.size());
		for (int i = 0; i < answer.size(); ++i)
			fprintf(out, "%d %d %d\n", answer[i].j, answer[i].p, answer[i].s);
	}

	fclose(in);
	fclose(out);

	return 0;
}