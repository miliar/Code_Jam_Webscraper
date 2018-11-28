
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

int T,cnt,n,ans,tmp;
char s[2000];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>T;
	cnt=0;
	while (T--){
		cnt++;
		scanf("%d",&n);
		scanf("%s",&s);
		ans=0;
		tmp=s[0]-'0';
		for (int i=1;i<=n;i++){
			if (tmp<i) ans+=(i-tmp),tmp=i;
			tmp+=s[i]-'0';
		}
		printf("Case #%d: %d\n",cnt,ans);
	}
	return 0;
}

