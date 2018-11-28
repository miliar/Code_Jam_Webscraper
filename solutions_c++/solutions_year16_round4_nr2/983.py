#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000007

int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);
		int n,k;
		cin>>n>>k;
		vector<long double> p(n);
		fore(i,0,n)
            cin>>p[i];
		string s = "";
		fore(i,0,n-k)
            s+='0';
        fore(i,0,k)
            s+='1';
        long double fa = 0;
        do {
            string s2 = "";
            vi ind;
            fore(i,0,n) {
                if(s[i] == '1')
                    ind.pb(i);
            }
            fore(i,0,k/2)
                s2+='0';
            fore(i,0,k/2)
                s2+='1';
            long double ans = 0;
            do {
                long double now = 1;
                fore(i,0,k) {
                    if(s2[i] == '1') {
                        now*=p[ind[i]];
                    }
                    else {
                        now*=(1-p[ind[i]]);
                    }
                }
                ans+=now;
            }while(next_permutation(all(s2)));
            fa = max(fa,ans);
        }while(next_permutation(all(s)));
        cout<<fixed<<setprecision(10)<<fa<<endl;
	}
	return 0;
}
