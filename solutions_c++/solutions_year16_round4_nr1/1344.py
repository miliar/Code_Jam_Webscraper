#include <bits/stdc++.h>

using namespace std;

int A[3][15][3]; //0R 1P 2S 
string S;

void init();
void print(int, int);
void work(int, int);

int main()
{
	init();

	int t;
	cin>>t;

	for(int c=0;c<t;c++)
	{
		S.clear();

		int n,r,p,s;
		cin>>n>>r>>p>>s;

		printf("Case #%d: ",c+1);
		if(A[0][n][0] == r && A[0][n][1] == p && A[0][n][2] == s)
		{
			print(0,n);
			// cout<<S<<endl;
			work(0,(1<<n));
			cout<<S;
		}
		else if(A[1][n][0] == r && A[1][n][1] == p && A[1][n][2] == s)
		{
			print(1,n);
			// cout<<S<<endl;
			work(0,(1<<n));
			cout<<S;
		}
		else if(A[2][n][0] == r && A[2][n][1] == p && A[2][n][2] == s)
		{
			print(2,n);
			// cout<<S<<endl;
			work(0,(1<<n));
			cout<<S;
		}
		else
			printf("IMPOSSIBLE");

		printf("\n");
	}
}

void init()
{
	memset(A,0,sizeof(A));
	A[0][0][0] = 1;
	A[1][0][1] = 1;
	A[2][0][2] = 1;

	for(int i=1;i<15;i++)
	{
		A[0][i][0] += A[0][i-1][0] + A[2][i-1][0];
		A[0][i][1] += A[0][i-1][1] + A[2][i-1][1];
		A[0][i][2] += A[0][i-1][2] + A[2][i-1][2];

		A[1][i][0] += A[0][i-1][0] + A[1][i-1][0];
		A[1][i][1] += A[0][i-1][1] + A[1][i-1][1];
		A[1][i][2] += A[0][i-1][2] + A[1][i-1][2];

		A[2][i][0] += A[1][i-1][0] + A[2][i-1][0];
		A[2][i][1] += A[1][i-1][1] + A[2][i-1][1];
		A[2][i][2] += A[1][i-1][2] + A[2][i-1][2];
	}
}

void print(int x, int n)
{
	if(n)
	{
		switch(x)
		{
			case 0: print(0,n-1); print(2,n-1); break;
			case 1: print(1,n-1); print(0,n-1); break;
			case 2: print(1,n-1); print(2,n-1); break;
		}
	}
	else
	{
		switch(x)
		{
			case 0: S.push_back('R'); break;
			case 1: S.push_back('P'); break;
			case 2: S.push_back('S'); break;
		}
	}
}

void work(int l, int r)
{
	if(l+1<r)
	{
		// printf("%d-%dWorking on: ",l,r);
		// for(int i=l;i<r;i++)
			// cout<<S[i];

		int m = (l+r)/2;
		
		int A[3];
		int B[3];
		memset(A,0,sizeof(A));
		memset(B,0,sizeof(B));

		for(int i=l;i<m;i++)
		{
			switch(S[i])
			{
				case 'P': A[0]++; break;
				case 'R': A[1]++; break;
				case 'S': A[2]++; break;
			}
		}

		for(int i=m;i<r;i++)
		{
			switch(S[i])
			{
				case 'P': B[0]++; break;
				case 'R': B[1]++; break;
				case 'S': B[2]++; break;
			}
		}

		// printf("Stats\n %d %d \n %d %d \n %d %d\n",A[0],B[0],A[1],B[1],A[2],B[2]);
		if(A[0]<B[0] || (A[0]==B[0] && A[1]<B[1]))
		{
			// printf("Reversing\n");
			for(int i=l;i<m;i++)
				swap(S[i],S[r+l-i-1]);
		}

		// printf("Final: ");
		// for(int i=l;i<r;i++)
			// cout<<S[i];
		// cout<<endl;
		work(l,m);
		work(m,r);
	}
}