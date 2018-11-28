#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <cstdio>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <cmath>
#include <bitset>
#include <limits.h>
#include <limits>
#include <utility>
#include <set>
#include <numeric>
#include <functional>
#define LL long long int
#define R(i) freopen(i,"r",stdin)
#define W(i) freopen(i,"w",stdout)
#define R_W R("i.txt"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define oo (LL)numeric_limits<int>::max()
#define readVector(n,in,v) r(n){cin>>in;v.push_back(in);}
#define readGrid(n,m,data) r(n)FOR(j,0,m){cin>>data[i][j];}
#define all(x) x.begin(),x.end()
#define DFS_WHITE -1
#define DFS_BLACK 1
using namespace std;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
vector< vi > AdjList;
int main(){
	////R_W;
	int t;
	int cases=1;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;
		vi data;
		int _max=0,_min,add;
		r(n){
			int in;
			cin>>in;
			data.push_back(in);
			_max=max(_max,in);

		}
		_min=_max;

        FOR(i,1,_max+1){
            add = i ;
            FOR(j,0,n){
                if( data[j] > i ) {
                    if( data[j]%i == 0 )
                        add += (data[j]/i-1) ;
                    else
                        add += (data[j]/i) ;
                }
            }
            _min = min(_min,add) ;
        }
		printf("Case #%d: %d\n",cases++,_min);
	}
}