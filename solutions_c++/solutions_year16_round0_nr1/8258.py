#include <iostream>
using namespace std;
long long int times, num, val, i;
bool got_num[10];

bool got()
{
	for (int i = 0; i < 10; i++) 
		if (got_num[i] == false) return false;
	return true;
}

int main()
{
	cin >> times;
	for (long long int j = 0; j < times; j++)
	{
		cin >> num;
		if (num == 0) cout <<"Case #"<< j+1 << ": INSOMNIA" << endl;
		else
		{
			for (i = 1; !got(); i++)
			{
				val = num*i;
				for (long long int t = val; t > 0; t /= 10) got_num[t % 10] = true;
			}
			cout << "Case #"<<j+1<<": " <<val << endl;
			for (int i = 0; i < 10; i++) got_num[i] = false;
		}
	}
	
	
	return 0;
}