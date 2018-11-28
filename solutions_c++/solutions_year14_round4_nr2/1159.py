#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
#include<iomanip>
using namespace std;

#define MAXN 10005

int arr[MAXN];
int num[MAXN];
int tmparr[MAXN];

int main()
{
	freopen("d:\\2.in", "r", stdin);
	freopen("d:\\2-ans.txt", "w", stdout);
	
	int T;
	cin>>T;
	for(int kase = 1; kase <= T; ++kase)
	{
		int n;
		cin>>n;
		for(int i = 0; i < n; ++i)
		{
			cin>>arr[i];
			num[i] = arr[i];
		}
		
		sort(num, num+n);
		int ans = 0x3f3f3f3f;
		do
		{
			
			for(int i = 0; i < n; ++i)
			{
				bool ok = true;
				for(int j = i-1; j >= 0; --j)
					if(num[j] > num[j+1])
						ok = false;
				for(int j = i+1; j < n; ++j)
					if(num[j] > num[j-1])
						ok = false;
				
				if(ok)
				{
					for(int i = 0; i < n; ++i)
						tmparr[i] = arr[i];
					
					int cur = 0;
					for(int i = 0; i < n; ++i)
					{
						int idx = i;
						for(; idx< n; ++idx)
							if(tmparr[idx] == num[i])
								break;
								
						cur += idx - i;
						int tmpnum = tmparr[idx];
						for(int j = idx-1; j >= i; --j)
							tmparr[j + 1] = tmparr[j];
						tmparr[i] = tmpnum;
					}
					ans = min(ans, cur);
				}
			}
		}while(next_permutation(num, num+n));
		cout<<"Case #"<<kase<<": "<<ans<<endl;
	}
	
	return 0;
}
