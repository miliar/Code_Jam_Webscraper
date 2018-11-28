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
#define MOD 1000000000069
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;


vector<int64>v;

int main(){
	int64 t,c,d,num,val;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>c>>d>>num;
		v.clear();
		for(int i=0;i<d;i++){
			cin>>val;
			v.pb(val);
		}
		sort(all(v));
		int64 req=0;
		int64 sum=0;
		int64 idx=0;
		v.pb(MOD);
		while(req<num){
			if(req+1>=v[idx])
			req+=v[idx++]*c;
			else{
				req+=(req+1)*c;
				sum++;
			}
		}
		cout<<sum<<endl;
	}
	fclose(stdout);
	return 0;
}
