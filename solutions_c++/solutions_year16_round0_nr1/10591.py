#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<map>
#include<stack>
#include<queue>
#include<vector>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int z=0;z<t;z++)
	{
		int n;
		int visited = 0;
		cin >> n;
		if(n==0)
		{
			visited = 1;
			cout << "Case #" << z+1 << ": INSOMNIA\n";
		}
		else
		{
			vector<int> ispresent(10,0);
			long long int k,s,l;
			long long int count = 1;
			while(count < 10000000000)
			{
				k = count*n;
				s = k;
				l = 0;
				while(k)
				{
					ispresent[k%10] = 1;
					k = k/10;
				}
				for(int i=0;i<10;i++)
				{
					l += ispresent[i];
				}
				if(l==10)
				{
					visited = 1;
					cout << "Case #" << z+1 << ": " << s << endl;
					break;
				}
				count++;
			}
			if(visited==0)
			{
				cout << "Case #" << z+1 << ": INSOMNIA\n";
			}
		}
	}
	return 0;
}
