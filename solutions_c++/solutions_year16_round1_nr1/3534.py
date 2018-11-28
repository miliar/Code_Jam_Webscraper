#include <iostream>
#include <string>

using namespace std;

int main()
{
	string in,res[100],x;
	int T;
	cin >> T;
	for(int i = 0; i<T; i++)
	{
		cin >> in;
		res[i] = in[0];
		for(int j = 1; j < in.length(); j++)
		{
			if(res[i][0]<=in[j])
			{
				x = in[j] + res[i];
				res[i] = x;
			}
			else
				res[i] = res[i] + in[j];
		}
	}
	for(int i = 0; i<T; i++)
	{
		cout << "Case #"<<i+1<<": "<<res[i] <<endl;

	}
	return 0;
}