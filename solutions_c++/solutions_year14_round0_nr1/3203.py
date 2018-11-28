#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>

using namespace std;

typedef int		 			I;
typedef vector<int> VI;

#define SZ(v) 					((int)(v).size())
#define F(i,a,b) 				for(int i=(a);i<(b);++i)
#define R(i,n) 					F(i,0,n)
#define Fe(i,a,b)				for(int i=(a);i<=(b);++i)
#define S(x)					scanf("%d",&x);
#define FSZ(i,a,v) 				F(i,a,SZ(v))
#define RSZ(i,v) 				R(i,SZ(v))
#define pb						push_back

I main() {
	I k, a, x;
	VI r1, r2;

	S(k);
	Fe(t,1,k) {
		S(a);
		R(i,4) {
			R(j,4) {
				S(x);
				if(i+1==a) r1.pb(x);
			}
		}
		S(a);
		R(i,4) {
			R(j,4) {
				S(x);
				if(i+1==a) r1.pb(x);
			}
		}
		sort(r1.begin(),r1.end());

		FSZ(i,1,r1) {if(r1[i]==r1[i-1]) r2.pb(r1[i]);}

		if(SZ(r2)==0) printf("Case #%d: Volunteer cheated!\n",t);
		else if(SZ(r2)==1) printf("Case #%d: %d\n",t,r2[0]);
		else printf("Case #%d: Bad magician!\n",t);

		r1.clear();
		r2.clear();
	}
}
