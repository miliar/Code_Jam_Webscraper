#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <numeric>
#include <queue>
#include <iostream>
#include <string>
#include <cstring>
#include <utility>
#define sz(a) int((a).size())
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define Rep(i,j,k) for (int i=(j); i<=(k); i++)
#define Repd(i,j,k) for (int i=(j); i>=(k); i--)
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define SUM(a) accumulate(all(a),string())
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;

int n, A[100], B[100];
int used[100], num[100];

bool dfs(int i){
	if (i==n+1){
		Repd(i,n,1){
			int f=1;
			Rep(j,i+1,n)
				if (num[i]>num[j])
					f=max(f, B[j]+1);
			if (f!=B[i])
				return 0;
		}
		Rep(i,1,n) cout<<num[i]<<" ";
		cout<<endl;
		return 1;
	}
	Rep(x,1,n) if (!used[x]){
		used[x]=1;
		num[i]=x;

		int f=1;
		Rep(j,1,i-1)
			if (num[j]<x)
				f=max(f,A[j]+1);
		if (f==A[i])
			if (dfs(i+1))
				return 1;
		used[x]=0;
	}
	return 0;
}

int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);

    int TC;
    cin>>TC;
    Rep(tc,1,TC){
		printf("Case #%d: ",tc);

		cin>>n;
		Rep(i,1,n) cin>>A[i];
		Rep(i,1,n) cin>>B[i];

		memset(used,0,sizeof used);

		dfs(1);
    }

    return 0;
}
