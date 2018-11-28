#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#define lli long long int
#define ii pair<int,int>
#define mp make_pair
#define mod 1000000007
#define inf 999999999

using namespace std;

inline void inp(int &n ) {//fast input function
	n=0;
	int ch=getchar_unlocked(),sign=1;
	while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getchar_unlocked();}
	while( ch >= '0' && ch <= '9' )
		n=(n<<3)+(n<<1)+ ch-'0', ch=getchar_unlocked();
	n=n*sign;
}

int t,r1,r2,A[4][4],B[4][4],num;

set<int> s1,s2,s;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	inp(t);

	for(int a=1;a<=t;a++) {
		inp(r1);
		r1--;

		s1.clear();
		s2.clear();

		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				inp(num);
				if(i==r1)
					s1.insert(num);
			}
		}


		inp(r2);
		r2--;

		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				inp(num);
				if(i==r2)
					s2.insert(num);
			}
		}

		int ans=0,val;

		for(set<int>::iterator it=s2.begin();it!=s2.end();it++) {
			if(s1.find(*it)!=s1.end()) {
				val=*it;
				ans++;
			}
		}

		if(ans>1)
			printf("Case #%d: Bad magician!\n",a );
		else if(ans==0)
			printf("Case #%d: Volunteer cheated!\n",a);
		else
			printf("Case #%d: %d\n",a,val);
	}




	return 0;
}