#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<climits>
#include<vector>
#include<iterator>
#include<set>

#define fr(i,a,b) for(int i=a; i<b; i++)
#define s(a) scanf("%d", &a)
#define p(a) printf("%d\n", a)
#define w(t) while(t--)
#define pb push_back
#define CLR(a) memset(a, 0, sizeof(a))

using namespace std;

typedef long long int lli;
typedef vector<int> VI;
typedef vector<string> VS;
const lli MAX = 1000LL;


int main() {
	int test;
	s(test);
	fr(ts,1,test+1) {
		lli r, t;
		scanf("%lld %lld", &r, &t);
		lli ans=0LL, paintused=0LL, circles=0LL;
		for(lli i=r; i<=MAX; i+=2) {
			paintused += 2*i+1;
			if(paintused<=t) {
				//cout<<paintused<<" "<<i<<endl;
				++circles;
				//r += r+2;
			}
			else
				break;
		}
		cout<<"Case #"<<ts<<": "<<circles<<endl;
	}
	return 0;
}
