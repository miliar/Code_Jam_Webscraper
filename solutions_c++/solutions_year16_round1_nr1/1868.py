#include <iostream>
#include <deque>

using namespace std;

void lastWord(string word)
{
	int length = word.length();
	deque<char> last;
	last.push_front(word[0]);
	for(int i = 1; i < length; i++)
	{
		if(last.front() <= word[i])
			last.push_front(word[i]);
		else
			last.push_back(word[i]);
	}
	for(int i = 0; i < length; i ++)
	{
		cout << last.front();
		last.pop_front();
	}
	cout << endl;
}

int main()
{
	string word;
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> word;
	    cout << "Case #" << i << ": ";
	    lastWord(word);
	}
}