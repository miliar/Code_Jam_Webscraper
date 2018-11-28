#include<iostream>
#include<cstring>
#include<deque>
#include<algorithm>

using namespace std;

char str[2010];
deque<char> dq;
void input() {
	cin >> str;
}


void proccess() {
	dq.push_back(str[0]);

	int leng = strlen(str);
	for (int i = 1; i < leng; i++)
	{
		if (dq.front() <= str[i])
		{
			dq.push_front(str[i]);
		}
		else
		{
			dq.push_back(str[i]);
		}

	}

}

void output() {
	while (!dq.empty())
	{
		cout << dq.front();
		dq.pop_front();
	}
	cout << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		input();
		proccess();
		cout << "CASE #" << i + 1 << ": ";
		output();
	}
}
