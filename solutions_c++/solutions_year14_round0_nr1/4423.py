#include <set>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#include <map>

int main(){
	int t;
	cin>>t;
	REP(i,t){
		int a[5][5];
		int b[17];
		int c;
		cin>>c;
		c--;
		REP(j,17){
			b[j] = 0;
		}
		REP(j,4){
			REP(k,4){
				cin>>a[j][k];
			}
		}
		REP(j,4){
			b[a[c][j]]++;
		}
		cin>>c;
		c--;
		REP(j,4){
			REP(k,4){
				cin>>a[j][k];
			}
		}

		REP(j,4){
			b[a[c][j]]++;
		}
		vector<int> d;
		REP(j,17){
			if(b[j] == 2){
				d.push_back(j);
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(d.size() == 0){
			cout<<"Volunteer cheated!";
		} else if(d.size() == 1){
			cout<<d[0];
		} else{
			cout<<"Bad magician!";
		}
		cout<<'\n';
	}
}

