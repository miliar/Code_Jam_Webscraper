#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include <climits>
#include<cmath>
#include<string>
#include <functional>
#include<sstream>
#include<map>
#include<set>


#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MAXM              1001
#define     MOD               1000000007
#define     Dbug             cout<<"";
#define     EPS              1e-15
typedef long long ll;
typedef pair<int,int> pii;
int n, a1[4][4], a2[4][4];
vector<int> v1, v2;
int main(){
	ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, t=1, f, s;
	cin>>tc;
	while (tc--)
	{
		v1.clear(), v2.clear();
		cin>>f;
		Rep(i, 4) Rep(j, 4) cin>>a1[i][j];
		cin>>s;
		Rep(i, 4) Rep(j, 4) cin>>a2[i][j];
		Rep(i, 4) v1.push_back(a1[f-1][i]);
		Rep(i, 4) v2.push_back(a2[s-1][i]);
		int cnt=0, ans=0;
		Rep(i, 4) Rep(j, 4) if(v1[i]==v2[j]) ans=v1[i], cnt++;
		if(cnt==1) cout<<"Case #"<<t++<<": "<<ans<<endl;
		else if(cnt) cout<<"Case #"<<t++<<": Bad magician!"<<endl;
		else cout<<"Case #"<<t++<<": Volunteer cheated!"<<endl;
	}
	return 0;
}