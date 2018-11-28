#include <iostream>
#include <string>
#include <queue>
#include <set>

using namespace std;

long long int bfs(string src, string dest);
string switchreverse(string str, int start, int end);
long long int greedy(string src);

int main()
{
	int T;
	string dest;
	string src;
	int cse = 1;

	cin>>T;
	while(T--)
	{
		cin>>src;
		cout<<"Case #"<<cse<<": "<<greedy(src)<<endl;
		cse++;

	}

	return 0;
}

long long int greedy(string src)
{
	int i = 0;
	int j;
	long long int count = 0;
	char ch;
	char lastchar;

	i = 0;
	while(i<src.size())
	{
		j = 0;
		ch = src[j];
		while(j<src.size() && src[j] == ch)
		{
			lastchar = src[j];
			if(src[j] == '+')
			{
				src[j] = '-';
			}
			else
			{
				src[j] = '+';
			}
			j++;
		}
		count++;
		i = j;
	}

	if(lastchar == '+')
	{
		return count-1;
	}
	else
	{
		return count;
	}

	return count;
}

long long int bfs(string src, string dest)
{
	if (src == dest)
	{
		return 0;
	}

	queue<pair<string, long long int> > que;
	pair<string, long long int> front;
	set<string> dict;
	set<string>::iterator itr;

	que.push(make_pair(src, 0));
	dict.insert(src);

	while(!que.empty())
	{
		front = que.front();
		que.pop();
		if(front.first == dest)
		{
			return front.second;
		}
		for(int i = 0; i<front.first.size(); i++)
		{
			string word = switchreverse(front.first, 0, i);
			itr = dict.find(word);
			if(itr == dict.end())
			{
				dict.insert(word);
				que.push(make_pair(word, front.second+1));
			}
			else
			{
				//cout<<word<<" already in the dictionary."<<endl;
			}
		}
	}

	return -1;
}

string switchreverse(string str, int start, int end)
{
	string ans = str;
	char one, two;

	while(start <= end)
	{
		one = (ans[start] == '+') ? '-' : '+';
		two = (ans[end] == '+') ? '-' : '+';
		ans[start] = two;
		ans[end] = one;
		start++;
		end--;
	}

	return ans;
}
