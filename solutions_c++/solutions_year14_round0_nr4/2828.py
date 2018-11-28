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
#define MOD 5000000007
#define total 500005
#define M 1000000007
typedef unsigned long long int uint64;
typedef long long int int64;
vector<double>naomi,ken,n1,k1;
double val;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,n,j;
	cin>>t;
	for(int ans=1;ans<=t;ans++){
		cout<<"Case #"<<ans<<": ";
		cin>>n;
		for(i=0;i<n;i++){
			cin>>val;
			naomi.pb(val);
		}
		sort(all(naomi));
		for(i=0;i<n;i++){
			cin>>val;
			ken.pb(val);
		}
		sort(all(ken));
		n1=naomi;
		k1=ken;
		int w=0,l=0;
		for(i=0;i<n;i++){
			val=n1[i];
			for(j=0;j<n;j++){
				if(k1[j]>val){
					k1[j]=0;
					break;
				}
			}
			if(j==n)
			w++;
		}
		//reverse(all(ken));
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(ken[j]==-1)
				continue;
				if(naomi[i]>ken[j]){
					l++;
					ken[j]=-1;
					break;
				}
			}
			if(j==n){
				for(j=n-1;j>=0;j--){
					if(ken[j]==-1)
					continue;
					ken[j]=-1;
					break;
				}
			}
		}
		cout<<l<<" "<<w<<endl;
		naomi.clear();
		ken.clear();
	}
	fclose(stdout);
	return 0;
}
