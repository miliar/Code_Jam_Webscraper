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

int n;
LL p;

bool ok1(LL x){
	LL now=1, len=(1LL<<n);
	Rep(i,1,n){
		if (x%2==1){
			x=x/2;
			len/=2;
			now+=len;
			continue;
		}
		if (x && x%2==0){
			x=x/2-1;
			len/=2;
			now+=len;
			continue;
		}
		break;
	}
	return now<=p;
}

void doit1(){
	LL l=0, r=(1LL<<n)-1;
	while(l<r){
		LL mid=(l+r)/2+1;
		if (ok1(mid))
			l=mid;
		else
			r=mid-1;
	}
	cout<<l<<" ";
}

bool ok2(LL x){
	LL now=0, len=1LL<<n;
	Rep(i,1,n){
		if (x==len-1){
			now+=len;
			break;
		}
		if (x%2==0){
			x/=2;
			len/=2;
			continue;
		}
		if (x%2==1){
			x=x/2+1;
			len/=2;
			now+=len;
			continue;
		}
	}
	return now<=p;
}

void doit2(){
	LL l=0, r=(1LL<<n)-1;
	while(l<r){
		LL mid=(l+r)/2+1;
		if (ok2(mid))
			l=mid;
		else
			r=mid-1;
	}
	cout<<l;

}

int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    int TC;
    cin>>TC;
    Rep(tc,1,TC){
		printf("Case #%d: ",tc);

		cin>>n>>p;

		doit1();

		doit2();

		cout<<endl;
    }

    return 0;
}
