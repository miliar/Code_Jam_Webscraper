/* 
	Problem A. The Repeater
	George Vafiadis
 */

#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
using namespace std;

void solve(int test, int N, const vector<string>& words);

int main()
{
	int T;

	cin >> T;

	for (int ti = 1; ti <= T; ++ti)
	{
		int N;

		cin >> N;

		vector<string> words;

		for(int i = 0; i < N; ++i)
		{
			string word;
			cin >> word;
			words.push_back(word);		
		}

		solve(ti, N, words);
	}

	return 0;
}

void solve(int test, int N, const vector<string>& words)
{
	vector<string> letter(N);
	vector< vector<int>  > freq(N);

	for(int w = 0; w < N; ++w)
	{
		string word = words[w];

		letter[w].push_back(word[0]);
		freq[w].push_back(0);
		int curIndex = 0;

		for(int i = 0; i < word.size(); ++i)
		{
			if (word[i] == letter[w][curIndex])
			{
				++freq[w][curIndex];
			}
			else
			{
				++curIndex;
				letter[w].push_back(word[i]);
				freq[w].push_back(1);
			}
		}
	}

	for(int i = 1; i < N; ++i)
	{
		if (letter[i-1] != letter[i])
		{
			cout << "Case #" << test << ": " << "Fegla Won" << endl;
			return;
		}
	}

	int columns = freq[0].size();
	long minNumMoves = 0;
	
	for(int col = 0; col < columns; ++col)
	{
		long avg = 0;

		for(int r = 0; r < N; ++r)
		{			
			avg += freq[r][col];
		}

		long ideal = avg / N;

		for(int r = 0; r < N; ++r)
		{			
			int diff = abs(freq[r][col] - ideal);
			minNumMoves += diff;
		}

	}

	cout << "Case #" << test << ": " << minNumMoves << endl;
}





