#include<iostream>
#include<cstdio>
#include<sstream>
#include<fstream>
#include<cctype>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<cstring>
#include<string>
#include<complex>
#include<bitset>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>
#include<deque>
#include<stack>
#include<iomanip>
#include<utility>

#define pb push_back
#define pp pop_back
#define xx first
#define yy second
#define mp make_pair
#define X real()
#define Y imag()

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef complex<double> point;

const double eps=1e-9;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		long double v,x,r1,r2,c1,c2;
		int n;
		cin>>n>>v>>x;
		cin>>r1>>c1;
		cout<<"Case #"<<l<<": ";
		if(n==1){
			if(abs(c1-x)>eps){
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}
			v/=r1;
			cout<<setprecision(9)<<fixed<<v<<endl;
			continue;
		}
		cin>>r2>>c2;
		if(c1-x>eps && c2-x>eps){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if(x-c1>eps && x-c2>eps){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if(c1>x){
			swap(c1,c2);
			swap(r1,r2);
		}
		if(c1==c2){
			long double ans=v/(r1+r2);
			cout<<setprecision(9)<<fixed<<ans<<endl;
			continue;
		}
		long double cur1=v*(x-c2)/(c1-c2);
		long double ans=max(cur1/r1,(v-cur1)/r2);	
		cout<<setprecision(9)<<fixed<<ans<<endl;	
	}
	return 0;
}
