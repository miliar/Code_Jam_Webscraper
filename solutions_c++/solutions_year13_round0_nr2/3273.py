#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <cassert>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;

int a[111][111],tate[111],yoko[111];

int main() {
	// freopen ("input.txt", "r", stdin);
	// freopen ("output.txt", "w", stdout);
	int t,n,m;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n>>m;
		memset(tate,0,sizeof(tate));
		memset(yoko,0,sizeof(yoko));
		for(int x=0;x<n;x++){
			for(int y=0;y<m;y++){
				cin>>a[x][y];
				tate[x]=max(tate[x],a[x][y]);
				yoko[y]=max(yoko[y],a[x][y]);
			}
		}
		bool flag=true;
		for(int x=0;x<n;x++){
			for(int y=0;y<m;y++){
				if(a[x][y]<tate[x] && a[x][y]<yoko[y]){
					flag=false;
					goto out;
				}
			}
		}
out:
		cout<<"Case #"<<(i+1)<<": "<<(flag?"YES":"NO")<<endl;
	}
}