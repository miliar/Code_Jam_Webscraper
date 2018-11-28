#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <math.h>
#include <assert.h>

using namespace std;
typedef vector<int> vint;

vint convert(string s) {
	vint result;
	if (s.length() < 1)
		return result;

	if (s.length() == 1)
	{
		result.push_back( 1 );
		return result;
	}

	char ch = s[0];
	int seq = 1;
	for(int i = 1; i< s.length(); i++) 
	{
		if (s[i] != ch)
		{
			result.push_back( seq );
			seq = 1;
		}
		else
			seq++;

		ch = s[i];
	}
	result.push_back( seq );
	return result;
}

string stripequal(string s) {
	if (s.length() <= 1)
		return s;

	char ch = s[0];
	string result;
	for(int i = 1; i< s.length(); i++) 
	{
		if (s[i] != ch)
			result += ch;

		ch = s[i];
	}
	result += ch;
	return result;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t<T; t++) 
	{
		int N;
		cin >> N;
		vector<string> input;

		for(int n=0;n<N;n++) 
		{
			string s;
			cin >> s;
			// cout << s << " : " << stripequal( s ) << " : " ;
			input.push_back(s);
		}

		cout << "Case #" << (t+1) << ": ";
		string result;
		string s0 = stripequal( input[0] );
		for(int n=1;n<N;n++) 
		{
			string s1 = stripequal( input[n] );
			if (s0 != s1)
				result = "Fegla Won";
		}
		if (result != "") 
			cout << result;
		else {
			// Do it
			vector<vint> matrix;

			for(int n = 0;n<N;n++)
			{
				string s = input[n];
				vint r = convert(s);
				for(int i = 0; i < r.size(); i++)
				{
					while (i >= matrix.size())
					{
						vint temp;
						matrix.push_back( temp );
					}
					matrix[i].push_back( r[i] );
				}
			}

			for(int r = 0; r < matrix.size(); r++)
			{
				assert( matrix[0].size() == matrix[r].size());
			}
			int rows = matrix.size();
			int cols = matrix[0].size();

			long moves = 0;

			for(int r = 0; r < rows; r++)
			{
				long long sum = 0;
				for(int c = 0; c < cols; c++)
					sum += matrix[r][c];
				// cout << "SUM:"<<sum << endl;

				double avg = sum / (1.0 *cols);
				// cout << "AVG: " << avg << endl;

				int test1 = avg;
				int test2 = avg+1;

				int moves1 = 0;
				int moves2 = 0;
				for(int c = 0; c < cols; c++)
				{
					moves1 += fabs( matrix[r][c] - test1 );
					moves2 += fabs( matrix[r][c] - test2 );
				}

				moves += min ( moves1, moves2 );
				// cout << "M:" << moves << endl;

				/*
				for(int c = 0; c < cols; c++)
						cout << " " << matrix[r][c];
				cout << endl;
				*/
			}

			cout << moves;
		}

		cout << endl;
	}
	return 0;
}
