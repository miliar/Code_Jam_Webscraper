#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <queue>
#include <vector>
#include <stack>
#include <list>
#include <cmath>
#include <ctime>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<vi> vvi;
typedef long long int lli;

#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
#define TESTS wez(testow)while(testow--)
#define modfun 1000000007
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define INF 2147483647
#define REP(x,a,b) for(int (x) = (a);(x)<=(b);(x)++)
#define rep(x,n)   for(int (x)=0;(x)<(n);(x)++)
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin();!= (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mset(a,b) memset((a),(b),sizeof(a))
#define printDoubeArr(arr,n,m) for(int i=0;i<n;i++,printf("\n")) for(int j=0;j<m;j++) printf("%d ",arr[i][j])
#define printArr(arr,n) for(int (j)=0;(j)<(m);(j)++) printf("%d ",arr[j])
#define debug(vari) cout<<#vari<<" = "<<(vari)<<endl;
#define MAXN 10005

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	#endif
	int t;
	cin>>t;
	for(int testea=1;testea<=t;testea++)
	{
		vector<int> a;
		int n,x,temp;
		cin>>n>>x;
		rep(i,n){
			cin>>temp;
			a.pb(temp);
		}
		sort(a.rbegin(),a.rend());
		int spaceLeftCounter[1000];
		memset(spaceLeftCounter,0,sizeof(spaceLeftCounter));
		set<int> myset;
		int counter=0;
		for(int i=0;i<n;i++)
		{
			set<int>::iterator it;
			it=myset.lower_bound(a[i]);
			if(it!=myset.end())
			{

				spaceLeftCounter[*it]--;
				if(spaceLeftCounter[*it]==0)
					myset.erase(it);
			}
			else
			{
		// cout<<"dfbjdsf "<<x<<" "<<a[i]<<" "<<i<<endl;
				counter++;
				if(x-a[i]>0){
				myset.insert(x-a[i]);
				spaceLeftCounter[(x-a[i])]++;
				}
			}
		}
		cout<<"Case #"<<testea<<": "<<counter<<endl;
	}
	return 0;
}