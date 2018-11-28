//#include<iostream>
#include<fstream>
using namespace std;
bool visited[11];

long long cnt(long long N)
{

	bool finished;
	int ret = 0;

	long long i = 0;
	while (true)
	{
		i = i + 1;
		long long temp = N*i;

		while (temp)
		{
			visited[temp % 10] = true;
			temp /= 10;
		}
		int j;
		for ( j = 0; j < 10; j++)
		{
			
			if (!visited[j])
			{
				
				break;
			}
		}
		if (j==10)break;
	}

	return i*N;
}
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	long long T, N;
	cin >> T;
	for (int i = 1; i <= T;i++)
	{
		cin >> N;
		if (N == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl; continue;
		}
		for (int j = 0; j < 11; j++)visited[j] = false;
		cout << "Case #" << i << ": " << cnt(N)<< endl;
		
		
		
	}
	return 0;
}