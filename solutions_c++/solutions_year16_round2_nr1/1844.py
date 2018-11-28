#include <bits/stdc++.h>

using namespace std;

int index(char A)
{
	return A - 'A';
}

void print(int a, int b)
{
	while(b--)
		cout<<a;
}

int main()
{
	int t;
	cin>>t;

	for(int c=1;c<=t;c++)
	{
		string S;
		cin>>S;

		int A[26];
		int C[10];
		memset(A,0,sizeof(A));
		memset(C,0,sizeof(C));

		for(int i=0;i<S.size();i++)
			A[index(S[i])]++;

		C[0] = A[index('Z')];
		A[index('Z')] -= C[0];
		A[index('E')] -= C[0];
		A[index('R')] -= C[0];
		A[index('O')] -= C[0];

		C[2] = A[index('W')];
		A[index('T')] -= C[2];
		A[index('W')] -= C[2];
		A[index('O')] -= C[2];

		C[4] = A[index('U')];
		A[index('F')] -= C[4];
		A[index('O')] -= C[4];
		A[index('U')] -= C[4];
		A[index('R')] -= C[4];

		C[6] = A[index('X')];
		A[index('S')] -= C[6];
		A[index('I')] -= C[6];
		A[index('X')] -= C[6];

		C[8] = A[index('G')];
		A[index('E')] -= C[8];
		A[index('I')] -= C[8];
		A[index('G')] -= C[8];
		A[index('H')] -= C[8];
		A[index('T')] -= C[8];

		C[1] = A[index('O')];
		A[index('O')] -= C[1];
		A[index('N')] -= C[1];
		A[index('E')] -= C[1];

		C[3] = A[index('H')];
		A[index('T')] -= C[3];
		A[index('H')] -= C[3];
		A[index('R')] -= C[3];
		A[index('E')] -= C[3];
		A[index('E')] -= C[3];


		C[7] = A[index('S')];
		A[index('S')] -= C[7];
		A[index('E')] -= C[7];
		A[index('V')] -= C[7];
		A[index('E')] -= C[7];
		A[index('N')] -= C[7];

		C[5] = A[index('V')];
		A[index('F')] -= C[5];
		A[index('I')] -= C[5];
		A[index('V')] -= C[5];
		A[index('E')] -= C[5];

		C[9] = A[index('I')];
		A[index('N')] -= C[9];
		A[index('I')] -= C[9];
		A[index('N')] -= C[9];
		A[index('E')] -= C[9];

		printf("Case #%d: ",c);
		for(int i=0;i<10;i++)
			print(i,C[i]);
		printf("\n"); 
	}
}