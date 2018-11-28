#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>

#define FN(i, n) for(int i = 0; i < n; i++)
#define FE(x) for(typeof(x.begin()) itr = x.begin(); itr!=x.end(); itr++)
#define BE(x) x.begin(), x.end()

using namespace std;
int T;
int N,M;

const long long MOD = 1000002013ll;

struct Truc
{
	int pos, type, nb, autre;
	
	Truc() { }
	
	bool operator < (const Truc& autre) const
	{
		if(pos==autre.pos) return type > autre.type;
		
		return pos > autre.pos;
	}
};

vector<Truc> tab;

long long cout(int a, int b)
{
	long long sz = b-a;
	if(sz==0) return 0;
	if(sz==1) return (long long)N;
	long long res=(sz*(long long)(2*N-sz+1)/2)%MOD;
	return res;
}

int main()
{
	scanf("%d", &T);
	
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d", &N, &M);
		tab.clear();
		
		FN(i,M)
		{
			int deb,fin,nb;
			scanf("%d%d%d", &deb,&fin,&nb);
			
			Truc t;
			t.pos=deb;
			t.type=0;
			t.nb=nb;
			t.autre=fin;
			
			tab.push_back(t);
			
			t.pos=fin;
			t.type=1;
			t.nb=nb;
			t.autre=deb;
			
			tab.push_back(t);
		}
		
		sort(BE(tab));
		long long res = 0;
		priority_queue<Truc> tas;
		
		FN(i, tab.size())
		{
			if(tab[i].type==1)
			{
				//swap(tab[i].autre, tab[i].pos);
				tas.push(tab[i]);
			}
			else
			{
				long long int rest=tab[i].nb;
				
				while(rest>0)
				{
					Truc t = tas.top();
					tas.pop();
					
					//if(t.pos < tab[i].autre) printf("wtf");
					long long vc = cout(tab[i].pos, tab[i].autre) - cout(tab[i].pos, t.pos);
					//if(vc < 0) printf("WTF because %d vs %d ?\n", tab[i].autre-tab[i].pos, t.pos-tab[i].pos);
					vc = vc % MOD;
					
					if(t.nb > rest)
					{
						vc = (vc*rest)%MOD;
						res = (res+vc)%MOD;
						t.nb-=rest;
						tas.push(t);
						rest=0;
					}
					else
					{
						vc = (vc*t.nb)%MOD;
						res=(res+vc)%MOD;
						rest-=t.nb;
					}
				}
			}
		}
		
		printf("Case #%d: %lld\n", t, res);
	}
	
	return 0;
}

