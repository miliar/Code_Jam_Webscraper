#include <iostream>
#include<string>
using namespace std;

int main() {
	freopen("in2.txt","r", stdin);
	freopen ("output.txt", "w", stdout);
	int T, smax, needed, cnt, cur;
	string s;
	
	cin >> T;
	for (int c = 1; c <= T; c++)
	{
		cin >> smax;
		cin >> s;
		needed = cnt = 0;
		for (int i=0; i< s.size(); i++)
		{
			cur = s[i] - '0';
			if (cnt < i)
			{
				needed += i-cnt;
				cnt += i-cnt;
			}
			cnt += cur;
		}
		
		cout << "Case #" << c << ": " << needed << endl;
	}
	
	return 0;
}