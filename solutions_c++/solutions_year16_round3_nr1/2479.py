#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Party
{
	Party() {}
	Party(int n, int na) : num(n), name(na) {}
	int num;	// num of members of this party
	char name;
};

bool comp(const Party& a, const Party& b)
{
	return a.num > b.num;	// decreasing sorting
}

int main()
{
	FILE *ifp = fopen("A-large.in", "r");
	FILE *ofp = fopen("output.txt", "w");
	int T;
	fscanf(ifp, "%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		int N;
		fscanf(ifp, "%d", &N);	// num of parties
		int total = 0;
		vector<Party> parties;
		for (int i = 0; i < N; ++i)
		{
			int num;
			fscanf(ifp, "%d", &num);
			parties.push_back(Party(num, (char)i + 'A'));
			total += num;
		}
		sort(parties.begin(), parties.end(), comp);

		fprintf(ofp, "Case #%d: ", t);
		if (N == 2)	// special case
		{
			while (parties[0].num > parties[1].num)
			{
				fprintf(ofp, "%c", parties[0].name);
				parties[0].num -= 1;
				if (parties[0].num > parties[1].num)
				{
					fprintf(ofp, "%c ", parties[0].name);
					parties[0].num -= 1;
				}
			}

			while (parties[0].num)
			{
				fprintf(ofp, "%c%c ", parties[0].name, parties[1].name);
				parties[0].num -= 1;
				parties[1].num -= 1;
			}
			// end
		}
		else // general case
		{
			int evacuate_num = 0;
			while (evacuate_num < total)
			{
				int now_ev = 0;
				while (now_ev < 2 && parties[0].num > parties[1].num)
				{
					parties[0].num -= 1;
					fprintf(ofp, "%c", parties[0].name);
					now_ev++;
				}

				if (now_ev == 0)
				{
					// TODO
					if (parties[1].num > parties[2].num)
					{
						parties[0].num -= 1;
						parties[1].num -= 1;
						fprintf(ofp, "%c%c", parties[0].name, parties[1].name);
						now_ev += 2;
					}
					else
					{
						parties[0].num -= 1;
						fprintf(ofp, "%c", parties[0].name);
						now_ev++;
					}
				}
				else if (now_ev == 1)
				{
					if (parties[1].num == parties[2].num)	// 세 개가 같았던 상황
					{
						parties[0].num -= 1;
						fprintf(ofp, "%c", parties[0].name);
						now_ev++;
					}
				}

				evacuate_num += now_ev;
				sort(parties.begin(), parties.end(), comp);
				fprintf(ofp, " ");
			}
		}
		fputs("\n", ofp);
	}
	return 0;
}