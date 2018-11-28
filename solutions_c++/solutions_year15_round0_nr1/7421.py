#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int main()
{
	ifstream inc("input.txt", ios::in);
	ofstream ouc("output.txt", ios::out);
	int T,n,k,answer;
	string a;
	inc >> T;
	
	for (int z = 0; z < T; z++)
	{
		k = 0;
		inc >> n >> a;
		answer = 0;
		k += a[0]-'0';
		for (int i = 1; i <= n; i++)
		{
			if (k < i)
			{
				answer += i - k;
				k = i;
			}
			k += a[i]-'0';
		}
		ouc <<"Case #"<<z+1<<": "<< answer << endl;
	}
	return 0;
}