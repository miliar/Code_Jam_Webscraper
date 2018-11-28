#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <ctime>
using namespace std;

typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int>::iterator vit;
typedef map<int,int>::iterator mit;

const LL P = 1000002013;

struct tic
{
	int st,ed,num;
	tic(){}
	tic(int stt,int edd,int numm)
	{
		st = stt;
		ed = edd;
		num = numm;
	}
};
vector<tic> peo;
int n;

inline LL calc(int st,int ed)
{
	LL tt = ed - st + 1;
	return (2 * tt * n - tt * tt + tt) / 2;
}

bool cmp(const tic &a,const tic &b)
{
	if (a.st == b.st) return a.ed < b.ed;
	return a.st < b.st;
}

bool better(const tic &a,const tic &b)
{
	return min(a.ed,b.ed) >= max(a.st,b.st) && calc(a.st,a.ed) + calc(b.st,b.ed) > calc(a.st,b.ed) + calc(b.st,a.ed);
}

void work(int no)
{
	int m;
	LL org = 0;
	scanf("%d%d",&n,&m);
	peo.clear();
	for (int i = 0;i < m;++i)
	{
		int s,t,p;
		scanf("%d%d%d",&s,&t,&p);
		peo.push_back(tic(s,t,p));
		org += calc(s,t) % P * p % P;
		org %= P;
	}
	bool found = 1;
	while (found)
	{
		found = 0;
		for (int i = 0;i < peo.size();++i)
		{
			for (int j = 0;j < peo.size();++j)
			{
				if (i != j && better(peo[i],peo[j]))
				{
					found = 1;
					int p = min(peo[i].num,peo[j].num);
					tic t1(peo[i].st,peo[j].ed,p);
					tic t2(peo[j].st,peo[i].ed,p);
					tic t3;
					if (peo[i].num < peo[j].num)
					{
						t3 = peo[j];
						t3.num -= p;
						peo.push_back(t3);
					}
					else if (peo[i].num > peo[j].num)
					{
						t3 = peo[i];
						t3.num -= p;
						peo.push_back(t3);
					}
					peo[i] = t1;
					peo[j] = t2;
				}
			}
		}
	}
	LL now = 0;
	for (int i = 0;i < peo.size();++i)
	{
		now += calc(peo[i].st,peo[i].ed) % P * peo[i].num % P;
		now %= P;
	}
	printf("Case #%d: %lld\n",no,(org + P - now) % P);
}

int main()
{
	int times;
	scanf("%d",&times);
	for (int i = 1;i <= times;++i) work(i);
	return 0;
}
