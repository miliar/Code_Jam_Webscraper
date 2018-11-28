#include <cstdio>
#include <vector>
#include <algorithm>

const int MAXN = 1005;
int t,n;
double Nblocks[MAXN],Kblocks[MAXN];

int calcCheating();
int calcNormal();

int main()
{
	scanf("%d", &t);
	for(int test = 1; test <= t; ++test)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%lf", &Nblocks[i]);
		for(int i = 0; i < n; ++i)
			scanf("%lf", &Kblocks[i]);
		
		std::sort(Nblocks,Nblocks+n);
		std::sort(Kblocks,Kblocks+n);

		printf("Case #%d: %d %d\n", test, calcCheating(), calcNormal());
	}
}

int calcCheating()
{
	int result = 0, Kleft = 0, Kright = n-1;
/*
	for(int i = 0; i < n; ++i)
		printf("%.3lf ", Nblocks[i]);
	printf("\n");
	for(int i = 0; i < n; ++i)
		printf("%.3lf ", Kblocks[i]);
	printf("\n");
*/	
	for(int Nleft = 0; Nleft < n; Nleft++)
	{
		if(Nblocks[Nleft] > Kblocks[Kleft])
			{ result++; Kleft++; }
		else Kright--;
	}

	return result;
}

bool NaomisBlock(double weight, int itrN, int itrK)
{
	if(Nblocks[itrN+1] == weight) return true;
	if(Kblocks[itrK+1] == weight) return false;
	printf("Something went wrong...\n");
}

int calcNormal()
{
	int itrN = -1, itrK = -1;
	std::vector<double> blocks;

	for(int i = 0; i < n; ++i) blocks.push_back(Nblocks[i]);
	for(int i = 0; i < n; ++i) blocks.push_back(Kblocks[i]);

	std::sort(blocks.begin(), blocks.end());

	int points = 0;
	for(int i = 0; i < blocks.size(); ++i)
	{
		if(NaomisBlock(blocks[i],itrN,itrK))
			{ itrN++; points++; }
		else
		{
			itrK++; points--;
			points = std::max(points,0);
		}
	}

	return points;
}
