#include <iostream>
#include <string.h>
using namespace std;


#define N	40
#define P	50000
char s[N];
int n,j,ctr;

int fact[12];
char aa[25][20];
char bb[20][20];


long long GetCoin(int base)
{
	long long v=0;
	for(int i=0 ; i<n ; ++i)
		v = v*base + (s[i]-'0');
	return v;
}

void dfs1(int off, int end)
{
	if(ctr >= end)
		return;
	if(off<n)
	{
		s[off] = '0';		dfs1(off+1,end);
		s[off] = '1';		dfs1(off+1,end);
		return;
	}
	
	int i,k;
	for(i=2 ; i<=10 ; ++i)
	{
		long long coin = GetCoin(i);
		if(coin%11)
			return;
	}

//	cout << "aa " << ctr << " " << s << endl;
	strncpy(&aa[ctr][0], s, n);
	ctr++;
	return;

}


void dfs2(int off, int end)
{
	if(ctr >= end)
		return;
	if(off<n-1)
	{
		s[off] = '0';		dfs2(off+1,end);
		s[off] = '1';		dfs2(off+1,end);
		return;
	}
	
	int i,k;
	for(i=2 ; i<=10 ; ++i)
	{
		long long coin = GetCoin(i);
#if 0
		fact[i] = 0;
		for(k=0 ; primes[k] ; ++k)
		{
			if(!(coin%primes[k]))
				fact[i] |= 1<<k;
		}
		if(!fact[i])
			return;
#endif
		if(coin%11)
			return;
	}
//	cout << "bb " << ctr << " " << s << endl;
	strncpy(&bb[ctr][0], s, n);
	ctr++;
#if 0
	for(k=0 ; primes[k] ; ++k)
	{
		for(i=2 ; i<=10 ; ++i)
			if(!(fact[i]|(1<<k)))
				break;
		if(i>10)
		{
			cout << s;
			for(i=2 ; i<=10 ; ++i)
				cout << " " << primes[k];
			cout << endl;
			ctr++;
		}
	}
#endif
}

int main()
{
	int tc,tst;
	
	cin >> tst;
	for(tc=1 ; tc<=tst ; ++tc)
	{
		cout << "Case #" << tc << ":\n";

		cin >> n >> j;

		s[0] = '1';	s[n] = 0;	ctr = 0;	dfs1(1,25);
		s[n-1]='1';	s[n] = 0;	ctr = 0;	dfs2(0,20);
		
		int i,k;
		for(i=0 ; i<25 ; ++i)
			for(k=0 ; k<20 ; ++k)
			{
				cout << aa[i] << bb[k] << " 11 11 11 11 11 11 11 11 11" << endl;
			}
	}
	return 0;
}
