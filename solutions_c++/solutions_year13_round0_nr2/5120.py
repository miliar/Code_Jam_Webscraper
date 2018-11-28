#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>
#include <queue>
#include <cstring>

#define pb push_back
#define VI vector<int>
#define VS vector<string>
#define sz(v) v.size()
#define len(s) s.length()
#define full(v) v.begin(),v.end()

#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)

typedef long long ll;

const int INF = 1<<30;

using namespace std;

int main(void){
	int t;
	cin>>t;
	int cnt=1;
	while(t--){
		int n,m;
		cin>>n>>m;
		int high=-1;
		int input[100][100];
		int curr[100][100];
		rep(i,n){
			rep(j,m){
				cin>>input[i][j];
				high=max(high,input[i][j]);
			}
		}
		rep(i,n)
			rep(j,m)
				curr[i][j]=high;
		
		int rowmax[100];
		int colmax[100];
		rep(i,n){
			int rm=-1;
			rep(j,m){
				rm=max(rm,input[i][j]);
			}
			rowmax[i]=rm;
		}
		
		rep(j,m){
			int cm=-1;
			rep(i,n){
				cm=max(cm,input[i][j]);
			}
			colmax[j]=cm;
		}
		
		//row
		rep(i,n){
			rep(j,m){
				curr[i][j]=min(rowmax[i],curr[i][j]);
				curr[i][j]=min(colmax[j],curr[i][j]);
			}
		}
		int f=1;
		rep(i,n)
			rep(j,m)
				if(curr[i][j]!=input[i][j])
					f=0;
		cout<<"Case #"<<cnt++<<": ";
		if(f){
			cout<<"YES\n";
		}
		else
			cout<<"NO\n";
	}
	return 0;
}
