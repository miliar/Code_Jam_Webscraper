#include<iostream>
#include<string>
#include<set>
#include<algorithm>
#include<list>
#include<vector>
#include<ctime>
#include<stack>
#include<cstring>
#include<cassert>
#include<queue>
#include<cmath>
#include<cstdio>
#include<climits>
#include<stack>

using namespace std;
typedef long long Long;
typedef pair<Long,Long> PII;
typedef pair<PII,Long> PPI;

PPI arr[2000];
int main()
{
	freopen("/Users/carlosjosetoribio/Desktop/A-small-attempt0.in","r",stdin);
	freopen("/Users/carlosjosetoribio/Desktop/A-small-attempt0.out","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1; tc<=TC; ++tc)
	{
		Long N,M;
		cin >> N >> M;
		Long tot1 = 0;
		for(int i = 0; i < M; ++i)
		{
			cin >> arr[2*i].first.first >> arr[2*i+1].first.first >> arr[2*i].second;
			arr[2*i+1].second = arr[2*i].second;
			arr[2*i].first.second = 0;
			arr[2*i+1].first.second = 1;
			Long stops = arr[2*i+1].first.first - arr[2*i].first.first;
			tot1 += (stops * N - ((stops-1)*stops)/2) * arr[2*i].second;
			
		}
		sort(arr,arr+2*M);
		Long n = 2*M;
		stack<int> STK;
		Long tot = 0;
		for(int i = 0; i < n; ++i)
		{
			if(arr[i].first.second == 0)
			{
				STK.push(i);
			}
			else
			{
				while(arr[i].second > 0)
				{
					int p = STK.top(); 
					Long mn = min(arr[i].second , arr[p].second);
					arr[i].second -= mn;
					arr[p].second -= mn;
					Long stops = (arr[i].first.first- arr[p].first.first);
					tot += (stops * N - ((stops-1)*stops)/2) * mn;
					if(arr[p].second == 0)
						STK.pop();
				}
			}
		}
		cout <<"Case #"<<tc<<": "<< tot1-tot << endl;
	}
    return 0;
}


