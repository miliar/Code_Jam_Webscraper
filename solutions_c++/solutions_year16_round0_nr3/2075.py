#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define ll long long
using namespace std;

bool b[32];
int j,n;
FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

ll power(int base, int exp)
{
	if(exp==0)
		return 1;
	if(exp%2==1)
		return base*power(base, exp-1);
	ll r = power(base, exp/2);
	return r*r;
}

ll trasforma(ll base)
{
	ll ris = 0;
	for(int i=0; i<n; i++)
		if(b[i])
			ris+=power(base,i);
	return ris;
}

ll trovaDivisore(ll numero)
{
	for(ll i = 2; i*i<=numero; i++)
	{
		if(numero%i==0)
			return i;
	}
	return -1;
}

void prova(int pos)
{
	if(j<=0)
		return ;
	if(pos==n-1)
	{
		b[pos]=1;
		vector<ll> divisori;
		for(int base = 2; base<=10; base++)
		{
			divisori.push_back(trovaDivisore(trasforma(base)));
			if(divisori[divisori.size()-1]==-1)
				return ;
		}
		for(int i=n-1; i>=0; i--)
			fprintf(out, "%d", (int) b[i]);
		fprintf(out, " ");
		for(int i=0; i<(int)divisori.size(); i++)
			fprintf(out, "%lld ", divisori[i]);
		fprintf(out, "\n");
		j--;
	}
	else
	{
		if(pos!=0)
		{
			b[pos]=0;
			prova(pos+1);
		}
		b[pos] = 1;
		prova(pos+1);
		
	}
}

int main()
{
	int t;
	
	fscanf(in, "%d %d %d", &t, &n, &j);
	fprintf(out, "Case #1:\n");
	prova(0);
	return 0;
}
