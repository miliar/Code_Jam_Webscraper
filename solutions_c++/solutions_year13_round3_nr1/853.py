#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

char v[] = "aeiou";

class node
{
	public:
	int i,c;
};

bool isv(char x)
{
	for (int i=0;i<5;i++)
		if (x==v[i])
			return true;
	return false;
}

int main ()
{
	freopen ("A-large.in","r",stdin);
	freopen ("output.txt","w",stdout);
	int t,c=1;
	scanf ("%d",&t);

	while (t--)
	{
		char x[1001000];
		int i,j,k,n;
		scanf ("%s %d",x,&n);
		string s = x;
		
		int count = 0;
		vector <node> r;

		for (i=0;i<s.size();i++)
		{
			if (isv(s[i]))
			{
				if (count>=n)
				{
					node nd;
					nd.i = i-count;
					nd.c = count;
					r.push_back(nd);
				}
				count = 0;
				continue;
			}
			count++;
		}
		if (count>=n)
		{
			node nd;
			nd.i = i-count;
			nd.c = count;
			r.push_back(nd);
		}
		//printf ("%d\n",r.size());
		long long ret = 0LL;
		int last = 0;
		for (i=0;i<r.size();i++)
		{
			int ind = r[i].i;
			long long count = (long long)(r[i].c);
			//printf ("%d %d\n",ind,count);
			int oc = count;
			count-=n;
			count++;
			//count += (ind-last);
			ret += count*(long long)(s.size()-n+1) - count*(count-1LL+(long long)(ind)*2LL)/2LL;
			ret += (long long) (ind-last) * (long long)(s.size()-ind-n+1);
			last = ind + count;
			//printf ("%d\n",ret);
			//if (ret<0)
			//	printf ("ERROR\n");
		}
		printf ("Case #%d: %lld\n",c++,ret);
	}
	return 0;
}
