#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <iostream>
#include <stack>
#include <cmath>
#include <map>
#include <sstream>
#include <queue>
#include <vector>
#define FOR(x,b,e) for(long long x=b;x<e;x++)
#define FORD(x,b,e) for(int x=b-1;x>=e;x--)
typedef long long LL;
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
bool pal(int a)
{
	ostringstream ss;
	ss<<a;
	string str=ss.str(),str2;
	str2.reserve(50000);
	FORD(i,str.size(),0)
	{
		str2=str2+str[i];
	}
	if(str.compare(str2)==0) return 1;
	else return 0;
}
int main()
{
	LL t,a,b,tab[2000];
	wczytaj(&t);
	FOR(i,0,34)
	{
		if(pal(i))
		{
			if(pal(i*i)) tab[i*i]=1;
		} 
	}
	FOR(i,1,1200)
	{
		tab[i]=tab[i-1]+tab[i];
	}
	FOR(i,0,t)
	{
		wczytaj(&a);
		wczytaj(&b);
		printf("Case #%d: %d\n",i+1,tab[b]-tab[a-1]);
	}
    return 0;
}
     
