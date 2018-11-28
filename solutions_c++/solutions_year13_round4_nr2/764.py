#include <iostream>
#include <map>
using namespace std;
int st[2000];
int init(int n)
{
	int top=1;
	int ed=0;
	st[0]=0;
	n--;
	while (n>=0)
	{
		for (int i=0;i<=ed;i++)
		{
			st[top++]=st[i]+(1<<n);
		}
		ed=top-1;
		n--;
	}
}
int main()
{
    long long a;
    int tt;
    scanf("%d",&tt);
    for (int ri=1;ri<=tt;ri++)
    {
    	int n,p;
    	scanf("%d %d",&n,&p);
    	init(n);
    	map<int,int> mp;
    	mp.clear();
    	for (int i=0;i<p;i++)
			mp[st[i]]=1;
		int pr=-1,min=(1<<n)-1;
		for (map<int,int> :: iterator j=mp.begin();j!=mp.end();j++)
		{
			if (j->first-pr!=1) break;
			pr=j->first;
		}
		min=pr;
		int max=-1;
		for (map<int,int> :: iterator j=mp.begin();j!=mp.end();j++)
		{
			if ((j->first)>max) max=j->first;
		}
		printf("Case #%d: %d %d\n",ri,min,max);
    }


    return 0;
}
