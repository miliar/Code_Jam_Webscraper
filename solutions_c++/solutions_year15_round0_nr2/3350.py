
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <ctime>
typedef long long ll;
#define clr(x,a) memset(x,a,sizeof(x))
#define sz(x) (int)x.size()
#define see(x) cerr<<#x<<" "<<x<<endl
#define se(x) cerr<<" "<<x 
#define pb push_back
#define mp make_pair
#define rep(i,l,r) for (long long i=l;i<=r;i++)
using namespace std;
int T,cnt,ans;
int n;
int a[100000];
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>T;
	while (T--){
		cnt++;
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			scanf("%d",&a[i]);
		}
		int ans=1001000;
		for (int i=1;i<=1000;i++){
			int tmp=0;
			for (int j=1;j<=n;j++){
				tmp+=(a[j]+i-1)/i-1;
			}
			tmp+=i;
			ans=min(ans,tmp);
		}
		
		printf("Case #%d: %d\n",cnt,ans);
	}
	return 0;
}

