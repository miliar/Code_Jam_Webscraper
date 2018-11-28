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
	double t,c,f,x;
	cin>>t;
	for(int ans=1;ans<=t;ans++){
		cout<<"Case #"<<ans<<": ";
		cin>>c>>f>>x;
		double pre,tot=0;
		pre=(x*1.0)/2;
		double st=2.0;
		for(int farm=1;farm<=100005;farm++){
			double tmp=(x*1.0)/st;
			if((tmp+tot)<=pre){
				pre=tmp+tot;
			}
			else{
				break;
			}
			tot+=(c*1.0)/st;
			st+=f;
			//cout<<farm<<" "<<tmp<<" "<<tot<<" "<<tmp+tot<<endl;
		}
		printf("%.7lf\n",pre);
	}
	fclose(stdout);
	return 0;
}
