#include <iostream>
#include <algorithm>
using namespace std;
//int two[]={1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576};
#define eps 1e-7
//string mas[]={"", "gun", "lightning", "astrolabe", "dragon", "water", "air", "paper", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire", "rock"};
int mas[20]={0};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	double c, f, x;
	double res=0;
	double a=0, b=0;
	for (int i=1; i<=t; ++i)
	{
		a=0, b=0;
		cin >> c >> f >> x;
		res = x/2;
		int kol=0;
		while (1)
		{
			a += c / (kol*f+2);
			b = x / ((kol+1)*f+2);
			if (eps<(res-(a+b)))
			{
					kol++;
					res = a+b;
			}
			else
				break;
		}
		printf("Case #%d: %.7lf\n", i, res);
	}
}