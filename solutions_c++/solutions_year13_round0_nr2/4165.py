#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <iostream>
#include <stack>
#include <cmath>
#include <map>
#include <queue>
#include <vector>
#define FOR(x,b,e) for(long long x=b;x<e;x++)
#define FORD (x,b,e) for(int x=b-1;x>=e;x--)
typedef int LL;
void wczytaj(LL *z)
{
		register char c=0;
		while(c<33) c=getc_unlocked(stdin);
		(*z)=0;
		while(c>32) {(*z)=(*z) *10LL+(c-'0');c=getc_unlocked(stdin);}
}
using namespace std;
struct ulamek{
	LL licznik;
	LL mianownik;
};
int main()
{
	LL t;
	LL tab[200][200];
	wczytaj(&t);
	FOR(i,0,t)
	{
		LL a,b;
		wczytaj(&a);wczytaj(&b);
		FOR(x,0,a)
		{
			FOR(y,0,b)
			{
				wczytaj(&tab[x][y]);
			}
		}
		LL foo=0;
		LL p=0,d=0;
		FOR(x,0,a) 
		{
			FOR(y,0,b)
			{
				FOR(z,0,a)
				{
					if(tab[z][y]> tab[x][y])
					{
						p=1;
						break;
					}
				}
				FOR(z,0,b)
				{
					if(tab[x][z] > tab[x][y]) 
					{
						
						d=1;
						break;
					}
				}
				if(p==1 && d==1) {foo=1;break;}
				p=0;d=0;
			}
			if(foo) break;
		}
		if(foo==1) printf("Case #%d: NO\n",i+1);
		else printf("Case #%d: YES\n",i+1);
		foo=0;p=0;d=0;
	}
    return 0;
}
     
