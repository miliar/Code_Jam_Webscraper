#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;

int main() {
	int A[1001];
	int T, N, r=0, acc=0;
	string S;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin>>T;
	for(int t=0; t<T; t++)
	{
		r=acc=0;
		cin>>N>>S;
		for(int i=0; i<=N; i++)
		{
			if (i!=0)
				A[i] = A[i-1] + S[i] - '0';
			else
				A[i] = S[i] - '0';
		}
		
		for(int i=0; i<=N; i++)
		{
			acc = max(0, (i+1) - (A[i] + r));
			r += acc;
			A[i] += acc;
		}
		
		printf("Case #%d: %d\n", t+1, r);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}