#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#define uint long long int
#define MP make_pair
#define PB push_back
using namespace std;
uint pot[60];
int main()
{
	ios_base::sync_with_stdio(0);
	int test;
	cin>>test;
	pot[0] = 1;
	for (int i = 1; i <= 55; i++)
	{
		pot[i] = 2 * pot[i - 1];
	}
	for (int y = 1; y <= test; y++)
	{
		cout<<"Case #"<<y<<": ";
		uint n, p;
		cin>>n>>p;
		uint zaw = pot[n];
		uint acc;
		uint kl = 0, kp = zaw - 1, aktc, faj; 
		while (kl <= kp)
		{
			aktc = (kl + kp) / 2;
			uint moc = aktc;
			uint sl = zaw - 1 - moc;
			uint potega = n - 1;
			uint poz;
			acc = 0;
			while (1)
			{
				if (moc > 0)
				{
					acc += pot[potega];
					moc -= (moc + 2) / 2;
				}
				else
				{
					poz = acc;
					break;
				}
				potega--;
			}
			poz++;
			if (poz > p)
			{
				kp = aktc - 1;
			}
			else
			{
				faj = aktc;
				kl = aktc + 1;
			}
		}
		cout<<faj<<" ";
		kl = 0, kp = zaw - 1;
		while (kl <= kp)
		{
			acc = pot[n] - 1;
			aktc = (kl + kp) / 2;
			uint potega = n - 1;
			uint sl = zaw - aktc - 1;
			uint poz;
			while (1)
			{
				if (sl > 0)
				{
					acc -= pot[potega];
					sl -= (sl + 2) / 2;
				}
				else
				{
					poz = acc;
					break;
				}
				potega--;
			}
			poz++;
			if (poz <= p)
			{
				faj = aktc;
				kl = aktc + 1;
			}
			else
			{
				kp = aktc - 1;
			}
		}
		cout<<faj<<endl;
	}
	return 0;
}