#pragma comment(linker, "/STACK:36777216")
#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <ctime>

#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define vint vector<int>
#define rep(i,n) for (int i=0; i<n; i++)
#define ll long long

using namespace std;

const int INF=~(1<<31);
const double EPS=1;
const double PI=3.141592653589793;

int main() {
#ifdef _DEBUG
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
#endif
  int T;
  cin>>T;
  rep(t,T) {
	  int n,m;
	  cin>>n>>m;
	  vector<vint>a(n,vint(m));
	  rep(i,n) {
		  rep(j,m) {
			cin>>a[i][j];
		  }
	  }
	  rep(i,100) {
		  if (i==99) {
			  printf("Case #%d: YES\n",t+1);
			  break;
		  }
		  vector<vint>b=a;
		  rep(j,n) {
			  bool br=0;
			  rep(l,m) {
				  if (a[j][l]!=i) {
					  br=1;
					  break;
				  }
			  }
			  if(!br) {
				  rep(l,m) {
					b[j][l]=i+1;
				  }
			  }
		  }
		  rep(j,m) {
			  bool br=0;
			  rep(l,n) {
				  if (a[l][j]!=i) {
					  br=1;
					  break;
				  }
			  }
			  if(!br) {
				  rep(l,n) {
					b[l][j]=i+1;
				  }
			  }
		  }
		  bool br=0;
		  rep(j,n) {
			  rep(l,m) {
				  if (b[j][l]==i) {
					  printf("Case #%d: NO\n",t+1);
					  br=1;
					  break;
				  }
			  }
			  if (br) break;
		  }
		  if(br) break;
		  a=b;
	  }
  }
  return 0;
}