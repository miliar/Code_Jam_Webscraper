#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
#include <numeric>
using namespace std;

 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 typedef long long ll;
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
 #define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 

int arr[10010];
bool vis[10010];

int main ()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int TC;
	cin >> TC;
	int CC=1;
	
	while (TC--)
	{
		int ans = 0;
		int N,M;
		cin >> N >> M;
		memset(vis,0,sizeof vis);
		
		for (int i=0 ; i<N ; i++) cin >> arr[i];
		
		sort(arr,arr+N);
		int last=N-1;
		
		for (int i=0 ; i<N ; i++)
		{
			if (vis[i]) continue;
			vis[i] = 1;
			ans ++;
			
			for (int j=last ; j>i ; j--)
			{
				if (vis[j]) continue;
				if (arr[i] + arr[j] <= M)
				{
					vis[j] = 1;
					last = j-1;
					break;
				}
				last = -1;
			}
		}
		
		printf("Case #%d: %d\n",CC++,ans);
	}
}
