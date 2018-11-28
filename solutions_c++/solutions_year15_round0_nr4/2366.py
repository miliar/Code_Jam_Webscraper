/*******************
  	Rahul Bhati
	CHARUSAT UNIVERSITY
	***********************/

#include <bits/stdc++.h>

using namespace std;

/* Time saving techniques :D */

typedef long long ll;
typedef unsigned long long ull;
typedef vector <int> vi;
typedef pair< int ,int > pii;
typedef istringstream iss;
typedef ostringstream oss;

#define pb              push_back
#define mp              make_pair
#define ff              first
#define ss              second
#define sz              size()
#define ln              length()
#define rep(i,n)        for(int i=0;i<n;i++)
#define fu(i,a,n)       for(int i=a;i<=n;i++)
#define fd(i,n,a)       for(int i=n;i>=a;i--)
#define foreach(it,v)   for( __typeof((v).begin())it = (v).begin() ; it != (v).end() ; it++ )
#define all(a)          a.begin(),a.end()
#define INF             (int)1e9
#define EPS             (1e-9)
#define INF_MAX         2147483647
#define INF_MIN         -2147483647
#define pi              acos(-1.0)
#define N               1000000
#define si(n)           scanf("%d",&n)
#define sll(n)          scanf("%lld",&n)
#define dbg(x)          { cout<< #x << ": " << (x) << endl; }
#define dbg2(x,y)       { cout<< #x << ": " << (x) << " , " << #y << ": " << (y) << endl; }
#define mset(a, s)      memset(a, s, sizeof (a))
#define FI              freopen("in.txt", "r", stdin);
#define FO              freopen("out.txt", "w", stdout);

int main(){ FI FO
	int t, x, r, c, pro;
	cin>>t;
	for(int cse = 1; cse <= t; cse++){

		bool ok = false;

		cin>>x>>r>>c;

		pro = r*c;

		if(x == 1)	ok = true;
		else if(x == 2){
			if((pro%x) == 0)	ok = true;
		}
		else if(x == 3){
			if((pro%x) == 0 && min(r, c) >= 2)	ok = true;
		}
		else if(x == 4){
			if((pro%x) == 0 && min(r, c) >= 3 && max(r, c) >= 4)	ok = true;
		}
		else if(x == 5){
			if((pro%x) == 0 && min(r, c) >= 4 && max(r, c) >= 5)	ok = true;
		}
		else if(x == 6){
			if((pro%x) == 0 && min(r, c) >= 4 && max(r, c) >= 6)	ok = true;
		}

		cout<<"Case #"<<cse<<": ";
		if(ok)	cout<<"GABRIEL"<<endl;
		else cout<<"RICHARD"<<endl;

	}

	return 0;
}

