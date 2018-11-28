#include<iostream>

using namespace std;

int N;
long long M;
int T;
long long SIZE;
long long TWO = 2;
long long POW[111];
long long ret1, ret2;

int main(void)
{
	int l0, l1, l2;
	long long loop;

	POW[0] = 1;
	for(l1 = 1; l1 <= 55; l1++ ) POW[l1] = POW[l1-1] + POW[l1-1];

	cin >> T;
	for(l0 = 1; l0 <= T; l0++)
	{
		cin >> N >> M;
		SIZE = POW[N];

		long long acc = 0;
		long long adder = SIZE;
		for(loop = 1; ; loop = loop+loop)
		{
			adder = adder / TWO;
			if(loop <= M)
			{
				ret2 = acc;
			}
			else
			{
				break;
			}
			acc += adder;
		}

		long long rank;
		acc = 0;
		long long yuki = SIZE;

		for(loop = 1; ; loop = loop+loop)
		{
			rank = SIZE - (yuki - 1);
//			cout << ".." << rank << endl;
			yuki /= TWO;
			if(rank <= M)
			{
				ret1 = acc;
			}
			else
			{
				break;
			}
			acc += loop + loop;
		}
				
		if(ret1 >= SIZE) ret1 = SIZE - 1;
		if(ret2 >= SIZE) ret2 = SIZE - 1;

		cout << "Case #" << l0 << ": " << ret1 << " " << ret2 << endl;
	}
}
