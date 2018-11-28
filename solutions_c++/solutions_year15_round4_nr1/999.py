#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;
typedef unsigned int uint;



int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;


	uint r, c;
	ull ans;
	char a[100][100],b[100][100];
	for (int t = 0; t < T; ++t)
	{
		input >> r>>c;
		//cin >> r>>c;
		
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				//cin >> b[i][j];
				input >> b[i][j];
				a[i][j] = b[i][j];
			}
		}

		for (int i = 0; i < r; ++i)
		{
			int j = 0;
			while ((j < c) && (a[i][j] == '.'))
				++j;
			if (j < c)
			{
				if (a[i][j] == '<')
				{
					int x = i - 1;
					while ((x >= 0) && ((a[x][j] == '.') /*|| (a[x][j] == '^')*/))
						--x;
					if (x >= 0)
						a[i][j] = '^';
					else
					{
						x = i + 1;
						while ((x < r) && ((a[x][j] == '.') /*|| (a[x][j] == 'v')*/))
							++x;
						if (x < r)
							a[i][j] = 'v';
						else
						{
							int y = j + 1;
							while ((y < c) && ((a[i][y] == '.') /*|| (a[i][y] == '>')*/))
								++y;
							if (y < c)
								a[i][j] = '>';
						}
					}
				}
			}
		}


		for (int i = 0; i < r; ++i)
		{
			int j = c-1;
			while ((j >= 0) && (a[i][j] == '.'))
				--j;
			if (j >=0)
			{
				if (a[i][j] == '>')
				{
					int x = i - 1;
					while ((x >= 0) && ((a[x][j] == '.') /*|| (a[x][j] == '^')*/))
						--x;
					if (x >= 0)
						a[i][j] = '^';
					else
					{
						x = i + 1;
						while ((x < r) && ((a[x][j] == '.') /*|| (a[x][j] == 'v')*/))
							++x;
						if (x < r)
							a[i][j] = 'v';
						else
						{
							int y = j - 1;
							while ((y >= 0) && ((a[i][y] == '.') /*|| (a[i][y] == '<')*/))
								--y;
							if (y >=0)
								a[i][j] = '<';
						}
					}
				}
			}
		}

		for (int j = 0; j < c; ++j)
		{
			int i = 0;
			while ((i <r) && (a[i][j] == '.'))
				++i;
			if (i < r)
			{
				if (a[i][j] == '^')
				{
					int y = j - 1;
					while ((y >= 0) && ((a[i][y] == '.') /*|| (a[i][y] == '<')*/))
						--y;
					if (y >= 0)
						a[i][j] = '<';
					else
					{
						y = j + 1;
						while ((y < c) && ((a[i][y] == '.') /*|| (a[i][y] == '>')*/))
							++y;
						if (y < c)
							a[i][j] = '>';
						else
						{
							int x = i + 1;
							while ((x < r) && ((a[x][j] == '.') /*|| (a[x][j] == 'v')*/))
								++x;
							if (x <r)
								a[i][j] = 'v';
						}
					}
				}
			}
		}

		for (int j = 0; j < c; ++j)
		{
			int i = r-1;
			while ((i >=0) && (a[i][j] == '.'))
				--i;
			if (i >=0)
			{
				if (a[i][j] == 'v')
				{
					int y = j - 1;
					while ((y >= 0) && ((a[i][y] == '.') /*|| (a[i][y] == '<')*/))
						--y;
					if (y >= 0)
						a[i][j] = '<';
					else
					{
						y = j + 1;
						while ((y < c) && ((a[i][y] == '.') /*|| (a[i][y] == '>')*/))
							++y;
						if (y < c)
							a[i][j] = '>';
						else
						{
							int x = i - 1;
							while ((x >= 0) && ((a[x][j] == '.') /*|| (a[x][j] == '^')*/))
								--x;
							if (x >=0)
								a[i][j] = '^';
						}
					}
				}
			}
		}




		/////////////////////////////////////////////////////////////////////////////////////////////////////////
		bool res = 1;

		for (int i = 0; i < r; ++i)
		{
			int j = 0;
			while ((j < c) && (a[i][j] == '.'))
				++j;
			if (j < c)
			{
				if (a[i][j] == '<')
					res = 0;
			}
		}


		for (int i = 0; i < r; ++i)
		{
			int j = c - 1;
			while ((j >= 0) && (a[i][j] == '.'))
				--j;
			if (j >= 0)
			{
				if (a[i][j] == '>')
					res = 0;
			}
		}

		for (int j = 0; j < c; ++j)
		{
			int i = 0;
			while ((i <r) && (a[i][j] == '.'))
				++i;
			if (i < r)
			{
				if (a[i][j] == '^')
					res = 0;
			}
		}

		for (int j = 0; j < c; ++j)
		{
			int i = r - 1;
			while ((i >= 0) && (a[i][j] == '.'))
				--i;
			if (i >= 0)
			{
				if (a[i][j] == 'v')
					res = 0;
			}
		}

		
		int ans = 0;
		if (res)
		{

			for (int i = 0; i < r; ++i)
			{
				for (int j = 0; j < c; ++j)
				{
					if (a[i][j] != b[i][j])
						++ans;
				}
			}
		}

		output << "Case #" << t + 1 << ": ";
		if (!res)
			//cout << "IMPOSSIBLE" << endl;
			output << "IMPOSSIBLE" << endl;
		else
			output << ans << endl;

		//output << "Case #" << t + 1 << ": " << ans << endl;

	}

	input.close();
	output.close();
	//	system("pause");
	return 0;
}
