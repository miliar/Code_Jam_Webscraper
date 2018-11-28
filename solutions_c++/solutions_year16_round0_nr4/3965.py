#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 100000

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

void solve(int primer){
	int n;
	scanf("%d%*d%*d",&n);
	printf("Case #%d: ",primer);
	FOR(i,n)printf("%d%c",i+1,(i==n-1?'\n':' '));
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)solve(i+1);
	return 0;
}
