#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main (int argc, char const* argv[])
{
	#ifndef ONLINE_JUDGE
		freopen("in","r",stdin);
		freopen("out","w",stdout);
		freopen("out_err","w",stderr);
	#else
	 //submision online
	#endif
	std::ios_base::sync_with_stdio(0);cin.tie(0);
	int t;std::cin >> t;
	for (int x = 1; x <= t; x += 1)
	{
		int sumParty;
		std::cin >> sumParty;
		priority_queue<ii,vii> data;
		int sum=0;
		for (int i = 0; i < sumParty; i += 1)
		{
			int temp;std::cin >> temp;
			sum+=temp;
			data.push(make_pair(temp,i));
		}
		std::cout << "Case #" <<x<<":";
		while (!data.empty())
		{
			ii firstMax = data.top();
			data.pop();
			ii secondMax = data.top();
			data.pop();
			ii curr = data.top();
			if(!data.empty() && firstMax.first>=2 && secondMax.first<=(sum-2)/2)
			{
				firstMax.first-=2;
				sum-=2;
				std::cout << ' ' << (char)(firstMax.second+'A')<<(char)(firstMax.second+'A');
			}
			else if (curr.first<=(sum-2)/2 || data.empty())
			{
				firstMax.first--;
				secondMax.first--;
				sum-=2;
				std::cout << ' ' <<  (char)(firstMax.second+'A')<< (char)(secondMax.second+'A');
			}
			else
			{
				firstMax.first--;sum--;
				std::cout << ' ' << (char)(firstMax.second+'A');
			}
			if(firstMax.first>0)data.push(firstMax);
			if(secondMax.first>0)data.push(secondMax);
		}
		std::cout << '\n' ;
		
	}
	
	return 0;
}
