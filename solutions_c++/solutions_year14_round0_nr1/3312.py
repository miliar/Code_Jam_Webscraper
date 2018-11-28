#include <iostream>
using namespace std;

int T;
int n = 4;
int answer1, answer2;
int a[5][5];
int b[5][5];
int res;

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;

	int S = 0;

	for(int tmp = 0; tmp < T; ++tmp)
	{
		S = 0;

		cin >> answer1;

		for(int i = 1; i <= n; ++i )
			for(int j = 1; j <= n ; ++ j )
				cin>>a[i][j];

		cin >> answer2;

		for(int i = 1; i <= n; ++i )
			for(int j = 1; j <= n ; ++ j )
				cin>>b[i][j];

		for(int i = 1; i <= n; ++ i )
			for(int j = 1; j <= n; ++ j)
				if(b[answer2][i] == a[answer1][j])
					S++;

		cout << "Case #" << tmp+1 << ": ";

		if( S == 0 )
			cout<<"Volunteer cheated!"<<endl;
		else if ( S == 1)
		{
			for(int i = 1; i <= n; ++ i )
				for(int j = 1; j <= n; ++ j)
					if(b[answer2][i] == a[answer1][j])
					{
						res = b[answer2][i];
						break;
					}

			cout<<res<<endl;
		}
		else cout << "Bad magician!" <<endl;


	}

	return 0;
}