#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <complex>

using namespace std;

#define rep(a,b,c) for(int a=b;a<=c;a++)
#define per(a,b,c) for(int a=b;a>=c;a--)
#define max(a,b) ((a>b)?(a):(b))
#define min(a,b) ((a<b)?(a):(b))
#define pb push_back
#define mp make_pair
#define PII pair<int,int>
#define X first
#define Y second

typedef long long ll;

ll T,n,p,ans1,ans2;

int main(){
	freopen("2.in","r",stdin);freopen("2.out","w",stdout);
	cin >>T;
	rep	(vv,1,T){
		cin >>n >>p;
		if	((1<<n)==p){
			ans1=ans2=p-1;
			cout <<"Case #" <<vv <<": " <<ans1 <<" " <<ans2 <<endl;
			continue;
		}
		ll te=1<<n,cnt=0,all=(1<<n)-1;
		while	(te>p){
			cnt++;te/=2;
		}
		if	(cnt==0)	ans2=0;
		else{
			ans2=1;
			rep(i,1,cnt)	ans2<<=1;
			ans2--;
		}
		ans2=all-ans2;
		ans1=1;te=0;all=1<<(n-1);
		while	(te<p){
			//cout <<te <<" " <<p <<endl;
			te=te+all;
			ans1*=2;all/=2;
		}
		ans1-=2;
		cout <<"Case #" <<vv <<": " <<ans1 <<" " <<ans2 <<endl;
	}
}

