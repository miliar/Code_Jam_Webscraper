#include <iostream>
#include <set>

using namespace std;

set<double> NB, KB;
int N;

int War()
{
	int NP = 0;
	set<double>::iterator i = NB.begin(), j=KB.begin();
	while( i!=NB.end() && j!=KB.end() )
	{
		while(*j < *i)
		{
			++j;
			++NP;
			if(j==KB.end())
				return NP;
		}
		++j;
		++i;
	}
	return NP;
}

int DeceitfulWar()
{
	int NP=0;
	set<double>::iterator i = NB.begin();
	set<double>::reverse_iterator k=KB.rbegin();
	set<double>::iterator j = KB.begin();
	for(; k != KB.rend(); ++k)
	{
		for( i = NB.begin(); i!=NB.end() && *i < *k ; ++i)
			;
		if(i!=NB.end() && *i > *k )
		{
			NB.erase(i);
			KB.erase(*k);
			++NP;
			if(KB.size())
			{
				k = KB.rbegin();
			}
			else
			{
				return NP;
			}
		}
	}
	for(i = NB.begin(),k=KB.rbegin(); i!=NB.end() && k!=KB.rend() && *i < *k ; ++i, ++k)
		;
	set<double>::iterator jend;
	if(k!=KB.rend())
		jend = ++(KB.find(*k));
	else
		jend = KB.begin();
	j = KB.begin();
	while( i!=NB.end() && j!=jend )
	{
		while(*j < *i)
		{
			++j;
			++NP;
			if(j==jend)
			{
				/*while( i!=NB.end() )
				{
					++NP;
					++i;
				}*/
				return NP;
			}
		}
		++j;
		++i;
	}/*
	while( i!=NB.end() )
	{
		++NP;
		++i;
	}*/
	return NP;
}

int main(int argc, char *argv[])
{
	int T, Cases = 0, i, res;
	double tmp[1000];
	scanf("%d", &T);
    do
    {
		scanf("%d", &N);
		for(i=0;i<N;++i)
			scanf("%lf", &tmp[i]);
		NB.insert(tmp, tmp+N);
		for(i=0;i<N;++i)
			scanf("%lf", &tmp[i]);
		KB.insert(tmp, tmp+N);
		res = War();
		if( N == 1)
		{
			printf("Case #%d: %d %d\n", ++Cases, res, res );
		}
		else
		{
			printf("Case #%d: %d %d\n", ++Cases, DeceitfulWar(), res );
		}
		NB.clear();
		KB.clear();
	}while(--T); 
}