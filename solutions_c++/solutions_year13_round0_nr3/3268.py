#include <iostream>
#include <sstream>
#include <cmath>
#include <string>

using namespace std;

bool palindrome(string s)
{
	int l = s.length();
	int h = l >> 1;
	for (int i = 0; i < h; i++)
		if (s[i] != s[l-i-1])
			return false;
	return true;
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	for (int t = 0; t < T; t++)
	{
		int A, B;
		cin >> A >> B;

		int AL = int(sqrt((double)A)-0.5);
		int BL = int(sqrt((double)B)+0.5);

		int count = 0;
		for (int i = AL; i <= BL; i++)
		{
			int sq = i*i;
			if (sq < A || sq > B) continue;
			stringstream ssl;
			ssl << i;
			stringstream ssh;
			ssh << sq;
			if (palindrome(ssl.str()) && palindrome(ssh.str())) count++;
		}

		cout << "Case #" << (t+1) << ": " << count << endl;
	}

	return 0;
}