#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;


int main(int argc, char const *argv[])
{
	freopen("al.in","r",stdin);
freopen("al.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	for(int c=1;c<=cases;c++)
	{
		int len;
		char data[1002];
		scanf("%d %s",&len, data);
		int res=0;
		int s=0;
		for(int i=0;i<=len;i++)
		{
			if(s<i)
			{
				s++;
				res++;
			}
			s+=data[i]-'0';
		}
		printf("Case #%d: %d\n",c,res);
	}
	return 0;
}