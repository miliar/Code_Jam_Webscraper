#include <cstdio>
#include <set>

using namespace std;

int main(int argc, char const *argv[])
{
	int T,x;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		int row;
		scanf("%d", &row);
		set<int> v;
		for (int i = 1; i <= 4; ++i)
		{
			for (int j = 1; j <= 4; ++j)
			{
				scanf("%d", &x);
				if(i == row){
					v.insert(x);
				}
			}
		}
		scanf("%d", &row);
		int card = -1;
		bool bad = false;

		for (int i = 1; i <= 4; ++i)
		{
			for (int j = 1; j <= 4; ++j)
			{
				scanf("%d", &x);
				if(i == row && v.find(x) != v.end()){
					if(card < 0){
						card = x;
					}
					else if(card > 0){
						bad = true;
					}
				}
			}
		}
		if(bad)	printf("Case #%d: Bad magician!\n", t);
		else if(card > 0)	printf("Case #%d: %d\n", t, card);
		else if(card < 0)	printf("Case #%d: Volunteer cheated!\n", t);
	}
	return 0;
}