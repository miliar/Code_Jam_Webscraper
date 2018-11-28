#include <cstdio>
#include <set>

using namespace std;

int main()
{
	int a, tn, i, t, ti = 0;
	scanf("%d",&tn);
	while(tn--)
	{
		set<int> s;
		scanf("%d",&a);
		for(int i = 0; i < 16; ++i)
		{
			scanf("%d",&t);
			if(i/4 == a-1) s.insert(t);
		}
		scanf("%d",&a);
		for(int i = 0; i < 16; ++i)
		{
			scanf("%d",&t);
			if(i/4 != a-1) s.erase(t);
		}
		printf("Case #%d: ", ++ti);
		if(s.size() == 0) printf("Volunteer cheated!\n");
		else if(s.size() > 1) printf("Bad magician!\n");
		else printf("%d\n", *(s.begin()));
	}
}
