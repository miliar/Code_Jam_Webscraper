/*
 * Compiled and tested with g++ (GCC) 4.9.2 on Linux x86_64.
 * Run with ./executable < input > output
 */
#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int main()
{
	int T, S;
	char c;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cin >> S;
		int friends = 0;
		int standing = 0;
		for(int s = 0; s < S+1; s++)
		{
			cin >> c;
			int num = c - '0';
			if(num && standing < s)
			{
				friends += s-standing;
				standing = s;
			}
			standing += num;
		}
		cout << "Case #" << t << ": ";
        cout << friends << endl;
	}
}
