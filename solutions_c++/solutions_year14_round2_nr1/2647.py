#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

int sum(std::vector< std::vector < int> > mat)
{
	int aux = 0;
	for (int i = 0; i < mat[0].size(); i++)
	{
		int min = 100000000;
		int max = -1;
		for (int j = 0; j < mat.size(); j++)
		{
			if (mat[j][i] < min) min =  mat[j][i];
			if (mat[j][i] > max) max =  mat[j][i];
		}
		aux += (max-min);
	}
	return aux;
}

std::string reduc(std::string s)
{
	std::string res;
	for (int i = 0; i < s.length(); i++)
	{
		if ((i == 0) or (s[i]!=s[i-1])) 
			res += s[i];
	}
	return res;
}

std::vector<int> times(std::string s)
{
	std::vector<int> aux;
	bool equal;
	int tim = 0;
	for (int i = 0; i < s.length(); i++)
	{
		if (i == 0)
			equal = true;
		else 
			equal = s[i] == s[i-1];
		if (equal)
			tim++;
		else
		{
			aux.push_back(tim);
			tim = 1;
			if ((i == s.length() -1))
					aux.push_back(tim);
		}
		if (equal and (i == s.length() -1))
			aux.push_back(tim);
	}	
	return aux;
}

bool eq_list(std::vector<string> l)
{
	bool aux = true;
	int i = 0;
	while (aux and i < l.size() - 1)
	{
		aux = aux and l[i] == l[i+1];
		i++;
	}
	return aux;
}

int main()
{
		
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T; // test cases
	scanf("%d",&T);
			
	for (int i = 0; i < T; i++)
	{
		int N;
		string word;
		std::vector<string> words, reduc_words;
		std::vector< std::vector <int> > tim_words;
		scanf("%d",&N);
		for (int i = 0; i < N; i++)
		{
			cin >> word;
			words.push_back(word);
		}
		for (int i = 0; i < words.size(); i++)
		{
			reduc_words.push_back(reduc(words[i]));
			tim_words.push_back(times(words[i]));
		}	
		bool is_ok = eq_list(reduc_words);
		int sol;
		if (is_ok) 
			sol = sum(tim_words);
		cout << "Case #" << i + 1 << ": ";	
		if (is_ok) cout << sol << endl;
		else cout << "Fegla Won" << endl;		
	}
	

	return 0;
};

