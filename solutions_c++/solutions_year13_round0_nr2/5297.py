#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	int t, m, n, i, j, min;
	int lwn[100][100];
	bool possible;
	cin >> t;
	for(int c=1; c<=t; c++)
	{
		scanf_s("%d %d", &m, &n);
		for(i=0; i<m; i++)
			for(j=0; j<n; j++)
				scanf_s("%d", &lwn[i][j]);
		cout << "Case #" << c << ": ";
		for(;;)
		{
			possible=false;
			min=lwn[0][0];
			for(i=0; i<m; i++)
			{
				for(j=0; j<n; j++)
					if(lwn[i][j]!=min)
						break;
				if(j<n)
					break;
			}
			if(i==m)
			{
				possible=true;
				break;
			}
			for(i=0; i<m; i++)
				for(j=0; j<n; j++)
					if(lwn[i][j]<min)
						min=lwn[i][j];
			for(i=0; i<m; i++)
				if(lwn[i][0]==min)
				{
					for(j=1; j<n; j++)
						if(lwn[i][j]!=min)
							break;
					if(j==n)
					{
						possible=true;
						for(j=0; j<n; j++)
						{
							if(i>0 && lwn[i-1][j]>lwn[i][j])
								lwn[i][j]=lwn[i-1][j];
							if(i<m-1 && lwn[i+1][j]>lwn[i][j])
								lwn[i][j]=lwn[i+1][j];
						}
					}
				}
			for(j=0; j<n; j++)
				if(lwn[0][j]==min)
				{
					for(i=1; i<m; i++)
						if(lwn[i][j]!=min)
							break;
					if(i==m)
					{
						possible=true;
						for(i=0; i<m; i++)
						{
							if(j>0 && lwn[i][j-1]>lwn[i][j])
								lwn[i][j]=lwn[i][j-1];
							if(j<n-1 && lwn[i][j+1]>lwn[i][j])
								lwn[i][j]=lwn[i][j+1];
						}
					}
				}
			if(!possible)
				break;
		}
		if(possible)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}