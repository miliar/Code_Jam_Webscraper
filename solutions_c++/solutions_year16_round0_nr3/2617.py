#include<iostream>

using namespace std;

long long D[11];
const int RANGE = 100000000;
char Check[RANGE+1];
long long P[RANGE+1], PN;

int main(void)
{
	int from = (1 << 15) + 1;
	int to = (1 << 16) - 1;
	int cnt = 0;
	int l1, l2;
	long long val;
	long long exp;
	
	cout << "Case #1:" << endl;

	PN = 0;
	for(l1 = 2; l1 <= RANGE; l1++)
	{
		if(Check[l1] == 0)
		{
			P[PN++] = l1;
			for(l2 = l1+l1; l2 <= RANGE; l2 += l1) Check[l2] = 1;
		}
	}

//	cout << PN << endl;
//	cout << P[PN-1] << endl;
//	for(int i = 0; i < 10; i++) cout << P[i] << endl;
//	return 1;

	for(int flag = from; flag <= to; flag+=2)
	{
		int base;
		for(base = 2; base <= 10; base++)
		{
			val = 0;
			exp = 1;
			for(int i = 0; i < 16; i++)
			{
				if(flag & (1 << i)) val += exp;
				exp *= (long long)base;
			}

//			cout << val << " ";
			for(l1 = 0; l1 < PN && P[l1] * P[l1] <= val; l1++)
			{
				if(val % P[l1] == 0)
				{
					D[base] = P[l1];
					goto maki;
				}
			}

			break;
maki:
			continue;
		}
		if(base > 10)
		{
			cout << val;
			for(l1 = 2; l1 <= 10; l1++) cout << " " << D[l1];
			cout << endl;
			cnt++;
			if(cnt == 50) return 0;
		}
	}

	return 0;
}
