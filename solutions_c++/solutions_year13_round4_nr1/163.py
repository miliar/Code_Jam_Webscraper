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
typedef long long LL;\

const int MOD=1000002013;

int n, m;
struct T{
	int num, pos, id, next;
} a[2100];

bool operator<(const T &a, const T &b){
	if (a.pos!=b.pos) return a.pos<b.pos;
	return a.id>b.id;
}

LL calc(int len){
					if (len%2==0)
						return (LL) len / 2 * (2*n+1-len) % MOD;
					else
						return (LL) (2*n+1-len) / 2 * len % MOD;
}

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    int TC;
    cin>>TC;
    Rep(tc,1,TC){
		printf("Case #%d: ",tc);

		cin>>n>>m;

		int ans=0;

		Rep(i,1,m){
			int beg,en,num;
			cin>>beg>>en>>num;

			ans=(ans+calc(en-beg)*num)%MOD;

			a[i*2-1].num=num,
			a[i*2-1].pos=beg,
			a[i*2-1].id=1;

			a[i*2].num=num,
			a[i*2].pos=en,
			a[i*2].id=-1;
		}

		sort(a+1,a+2*m+1);

		while(1){
			bool found=0;
			Repd(i,m*2,1)
				if (a[i].num && a[i].id==1)
					Rep(j,i+1,m*2)
						if (a[j].num && a[j].id==-1){
							int num=min(a[i].num, a[j].num);
							found=1;
							a[i].num-=num,
							a[j].num-=num;
							ans=(ans-calc(a[j].pos-a[i].pos)*num)%MOD;
						}
			if (!found)
				break;
		}

		cout<<(ans+MOD)%MOD<<endl;
    }

    return 0;
}
