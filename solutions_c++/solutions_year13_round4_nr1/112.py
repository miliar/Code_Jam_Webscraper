#include<cstdio>
#include<algorithm>
#include<stack>
using namespace std;
struct str
{
	int v;
	int p;
	bool end;
};

int n, m;
str t[2010];
const long long INF = 1000002013LL;
stack <str> s;
inline long long sum(long long x);

bool operator< (str a, str b)
{
	if(a.v < b.v) return 1;
	if(a.v > b.v) return 0;
	if(a.end == 0) return 1;
	return 0;
}

inline long long price(long long i)
{
	return sum(n) - sum(n-i);
}

inline long long sum(long long x)
{
	return x*(x+1)/2;
}

int main()
{
int T;
scanf("%d", &T);
for (int tt=1; tt<=T; tt++)
{
	while(!s.empty())
		s.pop();
	printf("Case #%d: ", tt);
	int i, o, e, p;
	scanf("%d%d", &n, &m);
	long long exp = 0;
	for (i=0; i<m; i++)
	{
		scanf("%d%d%d", &o, &e, &p);
		t[2*i].v = o;
		t[2*i].p = p;
		t[2*i].end = 0;
		
		t[2*i+1].v = e;
		t[2*i+1].p = p;
		t[2*i+1].end = 1;
		
		exp += price(e-o)*p % INF;
		exp %= INF;
//		printf("%lld\n", exp);
	
	}
//	printf("%lld\n", exp);
	
	long long act = 0;
	int pom;
	str temp;
	sort(t, t+2*m);
	for (i=0; i<2*m; i++)
	{
		if(t[i].end == 0)
		{
			//printf("aaa\n");		
			s.push(t[i]);
		}
		else 
		{
			//printf("bbb\n");
			pom = t[i].p;
			while(pom)
			{
				if(!s.empty())
				{
					temp = s.top();
					s.pop();
					int ilosc = min(temp.p, pom);
					//printf("%d\n", ilosc);
					act += (price(t[i].v - temp.v) * ilosc) % INF;
					act %= INF;
					pom -= ilosc;
					if(pom == 0)
					{
						temp.p -= ilosc;
						s.push(temp);
					}
				}
				else break;
			}
		}
	}
	
	//printf("%lld %lld\n", exp, act);
	printf("%lld\n", exp - act);	
	
}
return 0;
}
