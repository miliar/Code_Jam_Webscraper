#include<iostream>
#include<cstring>
using namespace std;
//ifstream cin("A-small-attempt0.in");
//ofstream cout("out.txt");
int main()
{
	int T;
	cin >> T;
	for(int Tcase = 1;Tcase <= T;Tcase++)
	{
		int smax;
		string in;
		int now = 0;
		int ans = 0;
		cin >> smax;
		cin >> in;
		for(int i=0;i<=smax;i++)
		{
			if(in[i] == '0')
				continue;
			if(now < i)
			{
				ans += i - now;
				now = i;
				now += in[i] - '0';
			}
			else 
			{
				now += in[i] - '0';
			}
		}
		cout << "Case #"<< Tcase << ": " << ans << endl;
	}
}
