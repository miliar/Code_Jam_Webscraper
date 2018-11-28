#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define AL(x) x.begin(),x.end()
#define pw(x) (1ll<<(x))
#define M 1000000007
using namespace std;
typedef pair<int,int> pt;
typedef vector<int> vt;

int n;
long long x,y;

long long solve(long long x){
	if (x==0)return -1;
	long long ans=0,p=0;
	for (int i=0;i<n;i++)if (p+pw(i)<x)p+=pw(i),ans+=pw(n-i-1);
	return ans;
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int T=0;
	cin >> T;
	for (int E=1;E<=T;E++){
		cin >> n >> x;
		cout << "Case #" << E << ": " << pw(n)-solve(pw(n)-x)-2 << " " << solve(x) << endl;
	}
	return 0;
}


