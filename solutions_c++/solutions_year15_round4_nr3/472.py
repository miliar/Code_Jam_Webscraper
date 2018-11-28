#include <cstdio>
#include <set>
#include <cstring>
#include <cstdlib>
#include <deque>
#include <string>
#include <map>
#include <bitset>
using namespace std;

bitset<3000> sent[200];
char buffer[1000000];
map<string,int> hash;

int get_id(string str)
{
	if(hash.find(str)==hash.end())
	{
		int s = hash.size();
		hash[str] = s;
		return s;
	}
	return hash[str];
}

int rec(int pos, int n, bitset<3000> en, bitset<3000> fr)
{
	//printf("%d\n",pos);
	if(pos==n)
	{
		return (en&fr).count();
	}
	return min(rec(pos+1,n,en|sent[pos],fr),rec(pos+1,n,en,fr|sent[pos]));
}

int main()
{
	//return 0;
	int t;
	scanf("%d",&t);

	for(int casenum=1; casenum<=t; casenum++)
	{
		int n;
		scanf("%d",&n);

		hash.clear();

		gets(buffer);

		for(int i=0; i<n; i++)
		{
			sent[i].reset();
			gets(buffer);
			char *c = strtok(buffer," ");
			while(c)
			{
				string str(c);
				sent[i][get_id(str)] = true;
				c = strtok(0," ");
			}
		}

		//puts("HURRAH");

		printf("Case #%d: %d\n",casenum,rec(2,n,sent[0],sent[1]));
	}

	return 0;
}