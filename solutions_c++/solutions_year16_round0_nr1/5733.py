#include <iostream>

using namespace std;

int main(void)
{
	long long N;
	long long answer;
	long long temp;
	int digitfound[10];
	int found;
	int T;
	int t;
	
	cin >> T;
	t = 1;
	while (t <=T)
	{
		cin >> N;
		cout << "Case #" << t << ": ";
		if ( N==0 )
		{
			cout << "INSOMNIA" << endl;
		}
		else
		{
			for (int i=0;i<10;i++)
			{
				digitfound[i] = 0;
			}
			found = 0;
			answer = N;
			while (true)
			{
				temp = answer;
				while (temp>0)
				{
					digitfound[temp%10] = 1;
					temp = temp/10;
				}
				found = 1;
				for (int i=0;i<10;i++)
				{
					if ( digitfound[i] == 0 )
						found = 0;
				}
				if ( found == 1 )
					break;
				answer = answer + N;
			}
			cout << answer << endl;
		}
		t++;
	}
	return 0;
}