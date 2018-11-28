#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int T,Smax,cum_sum,ans;
	
	string p_s;
	cin >> T;
	for (int i=0;i<T;i++)
	{
		cin >> Smax;
		p_s.clear ();
		cin >> p_s;
		cout << "Case #" << (i+1) <<": ";
		cum_sum = (int)(p_s[0]-'0');
		ans = 0;
		for (int j = 1;j < ((int)p_s.length());j++)
		{
			if(cum_sum<j)
			{
				ans = max(ans,(j-cum_sum));
			}
			cum_sum += (int)(p_s[j]-'0');			
		}
		cout << ans <<"\n";
	}
	return 0;
}
