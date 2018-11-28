#include <iostream>

using namespace std;

int main()
{
	int **arr;
	int inputcases;
	int n,m;
	int i,j;
	int cases;
	int Max;
	int EQUAL, POSSIBLE;

	cases = 1;
	cin>>inputcases;

	while(cases <= inputcases)
	{
		cin>>n>>m;

		arr = (int **)new int*[n+1];
		for(i=0;i<=n;i++)
			arr[i] = new int[m+1];
	
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				cin>>arr[i][j];
			}
		}

		for(i=0;i<n;i++)
		{
			Max = -1;
			for(j=0;j<m;j++)
			{
				if ( arr[i][j] > Max )
				{
					Max = arr[i][j];
				}
			}
			arr[i][m] = Max;
		}

		for (j=0;j<m;j++)
		{
			Max = -1;
			for(i=0;i<n;i++)
			{
				if ( arr[i][j] > Max )
				{
					Max = arr[i][j];
				}
			}
			arr[n][j] = Max;
		}
	
/*		cout<<"Case #"<<cases<<": \n";
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				cout<<arr[i][j]<<" ";
			}
			cout<<"\n";
		} */

		for(i=0;i<n;i++)
		{
			EQUAL = 1 ;
			for ( j=0; j<m-1; j++ )
			{
				if ( arr[i][j] != arr[i][j+1] )
				{
					EQUAL = 0;
					break;
				}
			}

			if ( EQUAL == 0 )
			{
				for ( j=0; j<m; j++ )
				{
					if ( arr[i][j] == arr[i][m] || arr[i][j] == arr[n][j] )
					{
						POSSIBLE = 1;
					}
					else
					{
						POSSIBLE = 0;
						break;
					}
				}
				if ( POSSIBLE == 0 )
				{
					cout<<"Case #"<<cases<<": NO\n";
					break;
				}
			}
			else
				POSSIBLE = 1;
		}

		if ( POSSIBLE == 1 )
			cout<<"Case #"<<cases<<": YES\n";

		cases = cases + 1;
	}

	return 0;
}
