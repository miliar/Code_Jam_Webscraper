#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int hash[10]={0};

bool check()
{
	for(int i = 0; i <= 9; i++)
		if (!hash[i])
			return false;
	return true;
} 

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i,j,t,n;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> n;
		memset(hash, 0, sizeof(hash));		
		if (!n)
	 		cout << "Case #" << i << ": "<< "INSOMNIA" << endl;
		else
		{
			j = 1;
			while(1)
			{
				int tmp = j * n;
				while(tmp)
				{
					hash[tmp%10] = 1;
					tmp /= 10;
				}
				if (check())
					break;	
				j++;
			}
	 		cout << "Case #" << i << ": "<< j * n << endl;
		}
	}
	return 0;
}

