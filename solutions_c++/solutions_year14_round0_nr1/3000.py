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
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int r1,i,j,t,val;
	cin>>t;
	for(int ans=1;ans<=t;ans++){
		cout<<"Case #"<<ans<<": ";
		int cnt[17]={0};
		cin>>r1;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				cin>>val;
				if(i==r1){
					cnt[val]++;
				}
			}
		}
		cin>>r1;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				cin>>val;
				if(i==r1){
					cnt[val]++;
				}
			}
		}
		int tot=0;
		for(i=1;i<=16;i++){
			if(cnt[i]==2){
				val=i;
				tot++;
			}
		}
		if(tot>1)
		cout<<"Bad magician!"<<endl;
		if(tot==0)
		cout<<"Volunteer cheated!"<<endl;
		if(tot==1)
		cout<<val<<endl;
	}
	fclose(stdout);
	return 0;
}
