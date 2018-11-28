#include <iostream>
#include <map>
using namespace std;

long long C = 1000002013;

int main()
{
	int T;
	cin >> T;
	for(int c=1;c<=T;c++)
	{
		long long N,M;
		cin >> N >> M;
		map<long long, long long> in, out;
		long long result = 0;
		for(int i=0;i<M;i++)
		{
			long long o,e,p;
			cin >> o >> e >> p;
			in[o] += p;
			out[e] += p;
			long long cost = (N + (N - (e-o) + 1)) * (e-o) / 2;
			cost %= C;
			cost *= p;
			cost %= C;
			result += cost;
			result %= C;
		}
		for(auto it = out.begin(); it!= out.end(); it++)
		{
			auto it2 = in.begin();
			while(it2 != in.end())
			{
				if(it2->first > it->first)
					break;
				it2++;
			}
			while(it->second > 0)
			{
				it2--;
				long long small = min(it2->second, it->second);
				it->second -= small;
				it2->second -= small;
				long long cost = (N + (N - (it->first - it2->first) + 1)) * (it->first - it2->first) / 2;
				cost %= C;
				cost *= small;
				cost %= C;
				result -= cost;
				result = (result + C) % C;
			}
		}
		cout << "Case #" << c << ": " << result << endl;
	}
}