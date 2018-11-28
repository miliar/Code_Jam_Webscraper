#include <cstdio>
#define ll long long
using namespace std;

ll solve(ll n)
{
	ll numeroOriginale = n;
	ll m;
	bool cifre[10]={0,0,0,0,0,0,0,0,0,0};
	int nCifre = 0;
	while(true)
	{
		m = n;
		while(m>0)
		{
			if(!cifre[m%10])
			{
				nCifre++;
				cifre[m%10]=true;
			}
			m/=10;
		}
		if(nCifre==10)
			return n;
		n+=numeroOriginale;
	}
}

int main()
{
	ll numero;
	int t;
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	fscanf(in, "%d", &t);
	for(int i=0; i<t; i++)
	{
		fscanf(in,"%lld", &numero);
		fprintf(out,"Case #%d: ", i+1);
		if(numero == 0)
			fprintf(out,"INSOMNIA");
		else
			fprintf(out,"%lld", solve(numero));
		fprintf(out,"\n");
	}
	return 0;
}
