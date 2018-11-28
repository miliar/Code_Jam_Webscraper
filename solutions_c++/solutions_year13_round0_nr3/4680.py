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
void _file(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	}
LL N, M, K;
vl pal ;
bool is_pal(LL x){
	LL sum = 0, i = x;
	while(i){
		sum = (sum * 10) + i%10; i/=10;
		}
	return sum == x;
	}
void _do(){
	int i;
	FOR(i,1,10000010){
		if(is_pal((LL)(i)) && is_pal((LL)((LL)(i)*(LL)(i))))
			pal.pb((LL)((LL)(i)*(LL)(i)));
		}
	}
int main () {
	int i, j, k, t, _case = 1;
	_file();
	t = GI;
	_do();
	while(_case<=t){
		cin>>N>>M; k = 0;
		FORV(i,pal){
			if(pal[i]>=N && pal[i]<=M)
				k++;
			}
		cout<<"Case #"<<_case<<": "<<k<<endl;
		_case++;
		}
	
	return 0;
}