#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <utility>
#include <functional>
#include <algorithm>

using namespace std;

int main ()
{
	int T;
	int N;
	int tot;
	int ppl;
	int e;

	vector<pair<int,char> > pq;

	scanf ("%d",&T);

	for (int j=0;j<T;j++)
	{
		tot = 0;
		scanf ("%d",&N);

		for (int i=0;i<N;i++)
		{
			scanf ("%d",&ppl);
			pq.push_back (make_pair(ppl,'A'+(char)i));

			tot += ppl;
		}

		printf ("Case #%d: ",j+1);

		e = 0;
		char f,s;
		int flag;

		int tot_temp = tot;

		while (e < tot_temp)
		{
			flag = 0;

			sort (pq.begin(),pq.end(),std::greater<pair<int,char> >());

			pair<int,char> temp = pq[0];

			// printf ("GOT %c %d when tot = %d\n",temp.second,temp.first,tot);

			f = temp.second;

			tot -= 1;

			e++;

			pq[0].first -= 1;

			sort (pq.begin(),pq.end(),std::greater<pair<int,char> >());

			temp = pq[0];

			// printf ("GOT %c %d when tot = %d\n",temp.second,temp.first,tot);

			if ((temp.first/(double)tot) > 0.5)
			{
				s = temp.second;
				flag = 1;
				e++;
				tot -= 1;

				pq[0].first -= 1;
			}

			

			if (flag)
			{
				// printf ("OUT -->> ");
				printf ("%c%c ",f,s);
			}
			else
			{
				// printf ("OUT -->> ");
				printf ("%c ",f);
			}

		}

		printf ("\n");

		pq.clear ();

	}

	return 0;
}