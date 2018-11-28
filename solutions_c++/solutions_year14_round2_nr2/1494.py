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
#define MOD 1000000007
#define total 500005
#define M 1000000000001
#define NIL 0
#define EPS 1e-5
#define INF (1<<28)
typedef unsigned long long int uint64;
typedef long long int int64;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		cout<<"Case #"<<cas<<": ";
	int64 a,b,k,val=0,i,j;
	cin>>a>>b>>k;
	for(i=0;i<a;i++){
		for(j=0;j<b;j++){
			if((i&j)<k)
			val++;
		}
	}
	cout<<val<<endl;
	}
	fclose(stdout);
	return 0;
}
