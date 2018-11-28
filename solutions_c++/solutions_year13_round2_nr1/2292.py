/* @author
 * bond, s_bond, sidhs
*/
#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <bitset>
#include <set>
#include <cmath>
#include <time.h>
#include <string.h>
#include <stdio.h>
#include <cstdio>
#include <assert.h>
#include <functional>
/////////////////
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({long long int t;scanf("%I64d",&t);t;})
#define PInt(a) printf("%d\n",(a))
#define PLng(a) printf("%I64d\n",(a))
#define FOR(i,a,b) for((i)=(a);(i)<(b);i++)
#define FORR(i,b,a) for((i)=(b);(i)>=(a);(i)--)
#define FORV(i,v) for((i)=0;(i)<v.size();i++)
#define FORI(it,v) for( typeof(v.begin()) it=v.begin();it!=v.end();it++)
#define All(v) v.begin(),v.end()
#define BS(v,val) (lower_bound(All(v),val)-v.begin())
#define pb(a) push_back((a))
#define Clear(a) memset((a),0,sizeof(a))
#define SV(v) sort((v).begin(),(v).end())
#define SA(a,n) sort((a),(a)+(n))
#define mp make_pair
#define IT ::iterator
using namespace std;
typedef long long int LL;
typedef unsigned long long int ULL;
typedef vector<int> vi;
typedef vector<LL> vl;
typedef vector<char> vc;
typedef vector<string> vs;
typedef map<int,int> mii;
typedef map<char,int> mci;
typedef map<string,int> msi;
typedef pair<int,int> pii;
typedef vector<pii> vp;
typedef vector< vector<int> > vvi;
typedef pair <int, long > pil;
typedef pair <long, long > pll;
typedef set <int> si;
typedef set <LL> sl;
typedef priority_queue <int> PQ;
/////////////////
int N, M, K,ans;
LL w[1000001], A;
void sfile(){
	freopen("inupt.in","r",stdin);
	freopen("output.out","w",stdout);
	}
int main () {
	int i, j, k, t, _case = 1;
	LL x, y;
	LL two=2;
	//sfile();
	ifstream sfin; ofstream sfout;
	sfin.open("input.in"); sfout.open("output.out");
	sfin >> t;
	while(_case<=t){
		//cin >> A >> N;
		sfin >> A >> N;
		FOR(i,0,N) sfin >> w[i];
		if(A==1) ans=N;
		else{
		SA(w,N);
		ans = 0;
		FOR(i,0,N){
			if( A>w[i] ) A+=w[i];
			else{
				LL dum = A;
				j = 0;
				while(dum<=w[i]){
					dum*=two;dum--;
					j ++;
					}
				if(j<N-i){
					ans += j;
					A = dum; A+=w[i];
					}
				else{
					ans += (N-i);
					break;
					}
				  }
				}
			}
		sfout<<"Case #"<<_case<<": "<<ans<<endl;
		_case++;
		}
	sfout.close();
	sfin.close();
	return EXIT_SUCCESS;
}