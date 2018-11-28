#include <iostream>
#include <algorithm>
using namespace std;
//int two[]={1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576};
//#define eps 1e-5
//string mas[]={"", "gun", "lightning", "astrolabe", "dragon", "water", "air", "paper", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire", "rock"};
int mas[20]={0};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	int a, b;
	int q;
	for (int i=1; i<=t; ++i)
	{
		for (int ii=1; ii<=16; ii++)
			mas[ii]=0;
		cin >> a;
		for (int j=1; j<=4; ++j)
			for (int k=1; k<=4; ++k)
			{
				cin >> q;
				if (j==a)
					mas[q]++;

			}
		cin >> b;
		for (int j=1; j<=4; ++j)
			for (int k=1; k<=4; ++k)
			{
				cin >> q;
				if (j==b)
					mas[q]++;

			}
		cout << "Case #" << i << ": ";
		int kol=0;
		int p=0;
		for (int j=1; j<=16; ++j)
		{
			if (mas[j]==2)
				{
					kol++;
					p=j;
				}
		}
		if (kol>1)
				cout << "Bad magician!";
		else if (kol==0)
			cout << "Volunteer cheated!";
		else
			cout << p;
		cout << "\n";

	}
}