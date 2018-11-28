#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;
#define pb push_back
#define pob pop_back
#define pf push_front
#define pof pop_front
#define mp make_pair
#define all(a) a.begin(),a.end()
#define bitcnt(x) __builtin_popcountll(x)
#define MOD 1000000000
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;
 
int main(){
	int t,n,i;
	string s;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>n>>s;
		int ans=0,pep=0;
		for(i=0;i<s.length();i++){
			if(pep<i){
				ans+=(i-pep);
				pep+=(i-pep);
			}
			pep+=s[i]-'0';
		}
		printf("%d\n",ans);
	}
	fclose(stdout);
	return 0;
}
