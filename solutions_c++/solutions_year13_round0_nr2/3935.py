#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int garden[101][101];

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int C;
	scanf("%d",&C);

	for (int test=1;test<=C;test++) {
		
		int M, N;
		cin >> M >> N;

		// Read the Garden
		for (int i=0; i<M;i++)
			for (int j=0; j<N;j++)
			{
				cin >> garden[i][j];
			}

		// Check if garden trimming is possible
		bool possible = true;
		for (int i=0; i<M && possible;i++)
			for (int j=0; j<N;j++)
			{
				int row=0, col=0, rowOK, colOK;

				// All elements left must be lower or same
				row=i; col=j; rowOK=1;
				while (--row >= 0)
					if (garden[row][col] > garden[i][j])
						rowOK=0;

				// All elements right must be lower or same
				row=i; col=j;
				while (++row < M)
					if (garden[row][col] > garden[i][j])
						rowOK=0;

				// All elements below must be lower or same
				row=i; col=j; colOK=1;
				while (--col >= 0)
					if (garden[row][col] > garden[i][j])
						colOK=0;

				// All elements right must be lower or same
				row=i; col=j;
				while (++col < N)
					if (garden[row][col] > garden[i][j])
						colOK=0;

				// if both row or columns are not possible, we are stuck
				if (rowOK==0 && colOK==0)
					possible = false;
			}

			cout << "Case #" << test << ": " << (possible ? "YES" : "NO" ) << endl;
	}
}
