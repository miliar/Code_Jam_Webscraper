#include<iostream>

using namespace std;

int X[2222], A[2222], B[2222];
int N, T;
int done;

void Go(int l1)
{
	int l2, l3;
	if(done) return;
	if(l1 == N+1)
	{
		done = 1;
	}
	else
	{
		for(l2 = 0; l2 < N; l2++) // position
		{
			if(X[l2] != 0) continue;
			int leftbig = 0;
			for(l3 = 0; l3 < l2; l3++)
			{
				if(X[l3] == 0) continue;
				if(X[l3] < l1 && A[l3] > leftbig) leftbig = A[l3];
			}

			if(leftbig + 1 != A[l2]) continue;

			int rightbig = 0;
			for(l3 = l2 + 1; l3 < N; l3++)
			{
				if(X[l3] == 0) continue;
				if(l1 > X[l3] && B[l3] > rightbig) rightbig = B[l3];
			}

			if(rightbig + 1 != B[l2]) continue;

			X[l2] = l1;

			Go(l1+1);
			if(done) return;

			X[l2] = 0;
		}
	}
}

int main(void)
{
	int l0, l1, l2, l3;

	cin >> T;
	for(l0 = 1; l0 <= T; l0++)
	{
		cin >> N;
		for(l1 = 0; l1 < N; l1++) cin >> A[l1];
		for(l1 = 0; l1 < N; l1++) cin >> B[l1];
		for(l1 = 0; l1 < N; l1++) X[l1] = 0;

		done = 0;
		Go(1);

		cout << "Case #" << l0 << ":";
		for(l1 = 0; l1 < N; l1++) cout << " " << X[l1];
		cout << endl;
	}
}
