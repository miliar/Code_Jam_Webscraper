#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

long long a[1024];
pair<long long, int> sorted[1024];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++)
	{
		int N;
		cin >> N;
		
		for(int i=0; i<N; i++)
		{
			cin >> a[i];
			sorted[i]=make_pair(a[i], i);
		}
		sort(sorted, sorted+N);
		
		long long ans=0;
		for(int i=0; i<N; i++)
		{
			int act=sorted[i].second;
			int d1=0;
			for(int j=0; j<act; j++)
			{
				if(a[act]<a[j]) d1++;
			}
			
			int d2=0;
			for(int j=act+1; j<N; j++)
			{
				if(a[act]<a[j]) d2++;
			}
			
			ans+=min(d1,d2);
		}
		
		cout << "Case #" << tc << ": " << ans << endl;
	}
}
