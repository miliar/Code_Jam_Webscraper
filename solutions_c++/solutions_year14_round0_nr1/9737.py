/*
 this code was written by Zanaty
 problem Name: A.cpp
 */
#include <bits/stdc++.h>

//#ifdef _MSC_VER
//#include <hash_set>
//#include <hash_map>
//using namespace stdext;
//#else
//#include <ext/hash_set>
//#include <ext/hash_map>
//using namespace __gnu_cxx;
//#endif

using namespace std;

#define rep(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define reps(i,x,n) for((i)=(x);(i)<(int)(n);(i)++)
#define repi(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define SZ(v) (int)v.size()
#define LEN(s) (int)s.length()
#define mp(x,y) make_pair(x,y)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define iter(it,s) for(__typeof(s.begin())it=s.begin();it!=s.end();it++)

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef long long ll;

#define EPS 1e-4
const int INF = (int) 1e8;
const int MAX = 1000;

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.txt", "r", stdin);
	freopen("out.txt","w",stdout);
#endif

	int test;
	cin >> test;
	int tt;
	reps(tt,1,test+1) {
		int ans1, ans2;
		vvi a(4, vi(4)), b(4, vi(4));
		cin >> ans1;
		int i, j;
		rep(i,4)
			rep(j,4)
				cin >> a[i][j];
		cin >> ans2;
		rep(i,4)
			rep(j,4)
				cin >> b[i][j];

		set<int> s1,s2;
		for(int i=0;i<4;i++)
			s1.insert(a[ans1-1][i]);


		for(int i=0;i<4;i++)
			s2.insert(b[ans2-1][i]);

//		cout<<"here"<<endl;
		vi res(8);
		vi::iterator it;
		it = set_intersection(all(s1),all(s2),res.begin());
		res.resize(it-res.begin());
//		cout<<"here "<<SZ(res)<<endl;
		if(SZ(res) == 0){
			printf("Case #%d: Volunteer cheated!\n",tt);
		}
		else if(SZ(res) == 1){
			printf("Case #%d: %d\n",tt,res[0]);
		}
		else {
			printf("Case #%d: Bad magician!\n",tt);
		}

	}

	return 0;
}
