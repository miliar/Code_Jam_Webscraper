#include<iostream>
#include<stdio.h> 
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<stdlib.h>
#include<string.h>
#include<queue>
#include<stack>
#include<assert.h>
#include<limits.h>
#define tr(i) for(typeof(i.begin()) it=i.begin(); it!=i.end();it++)
#define pb push_back
#define mp make_pair
#define REP(i,n) for(int i=0;i<n;i++)
#define rep(i,s,n) for(int i=s;i<n;i++)
#define s(n) scanf("%d",&n)
#define XX first
#define X first
#define Y second
#define all(a) a.begin(),a.end()
#define YY second.first
#define ZZ second.second
#define fill(a,b) memset(a,b,sizeof(a))
#define DREP(a) sort(all(a)); a.erase(unique(all(a)),a.end());
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
#define SZ(x) (int)(x.size())
#define lin(val,j) (DP[j]-val*D[j])
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
#define MN 10000000
#define MAXP 200000000
vector<int> primes;
int sieve[MAXP];
void runsieve() {
	sieve[1]=true;
	primes.pb(2);
	primes.pb(3);
	for(int i=0;(6*i+5)<MAXP;i++) {
		for(int k=1;k<=5;k+=4) {
			int cur=6*i+k;
			if(sieve[cur]) continue;
			primes.pb(cur);
			for(int j=2;j*cur<MAXP;j++) sieve[j*cur]=true;
		}
	}
}
long long check(long long in) {
	long long lim =ceil(sqrt(in));
	if(in%2==0) return 2;
	for(int i=0; primes[i]<=lim; i++) {
		if(in%primes[i]==0) return primes[i];
	}
	return -1;
}
int main()
{	
	runsieve();
	int T; s(T);
	int J, N; s(N); s(J);
	cout<<"Case #1:\n";
	vector<vector<long long> > out;
	REP(i, (1<<(N-1))){
		if(i%2==0) continue;
		vector<long long> now;
		bool good=true;
		for(int j=2;good&&j<=10;j++) {
			long long num=0;
			long long pw=1;
			int temp=i;
			REP(kk,N-1) {
				num+=(temp%2)*pw;
				pw*=j;
				temp/=2;
			}
			num+=pw;
			int ret=check(num);
			if(ret<0) good=false;
			else now.pb(ret);
			//cout<<num<<" "<<ret<<endl;
			if(j==10) now.pb(num);
		}
		if(good) out.pb(now);
		if(SZ(out)==J) break;
	}
	REP(i, SZ(out)) {
		cout<<out[i][9]<<" ";
		REP(j,9) cout<<out[i][j]<<" ";
		cout<<endl;
	}
	return 0;
}