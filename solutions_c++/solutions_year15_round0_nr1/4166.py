#include<cstdio>
#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<cmath>
#include<map>
using namespace std;

const int MAX_S = 1e3+7;
int t, S, noc=1;
int number[MAX_S];

main()
{
	ios_base::sync_with_stdio(0);
	cin >> t;
	while(t--)
	{
		cin >> S;
		string quantity;
		cin >> quantity;
		int res=0, num=0;
		for(int i=0; i<(int)(quantity.length()); ++i)
		{
			if((int)(quantity[i]-'0')>0)
			{
				if(num<i) {res+=(i-num); num+=(i-num);}
			}
			num+=(quantity[i]-'0');
			//cout << num << " " << res << endl;
		}
		cout << "Case #" << noc++ << ": " << res << endl;
	}
	return 0;
}