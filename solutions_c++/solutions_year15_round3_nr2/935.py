#include <iostream>
#include <string>
#include <vector>
#include <iomanip>    
using namespace std;

int max_answer;
double possible_answer;
int different;

int count(const vector<char> & s, const string& t)
{
	int answer = 0;
	for (int i = 0; i < s.size(); ++i)
	{
		if (i + t.size() <= s.size())
		{
			int j = 0;
			for (j = 0; j < t.size(); ++j)
			{
				if (t[j] != s[i + j])
					break;
			}
			if (j == t.size())
				answer ++;
		}
	}
	return answer;
}

void brute(const string& s, const string& text, int len, vector<char>& part)
{
	if (len == 0)
	{
		int cur_answer = count(part, text);
		//cout << cur_answer << '!' << endl;
		possible_answer += cur_answer;
		different++;
		max_answer = max(max_answer, cur_answer);
		return ;
	}

	for (int i = 0; i < s.size(); ++i)
	{
		part.push_back(s[i]);
		brute(s, text, len - 1, part);
		part.pop_back();
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		long long answer = 0;
		different = 0;
		max_answer = 0;
		possible_answer = 0;
		string letters, word;
		int K, L, S;
		cin >> K >> L >> S;
		cin >> letters >> word;
		//sort(letters.begin(), letters.end());
		vector<char> part;
		brute(letters, word, S, part);
		//cout << "!!!" << different << endl;
		cout << setprecision(25);
		cout << "Case #" << t + 1 << ": " << max_answer * 1.0 - possible_answer / different << endl;
	}
	return 0;
}