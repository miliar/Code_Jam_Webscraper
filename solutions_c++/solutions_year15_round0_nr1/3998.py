//I_HAVE_A_DREAM
//Standing_Ovation_Small.cpp
//DreamBig
//Apr 11, 2015
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minei(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxei(x)  max_element(x.begin(),x.end())-(x).begin()

#define uns(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acusum(x)  accumulate(x.begin(),x.end(),0)
#define acumul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>()); 
#define bits(x)     __builtin_popcount( x )
#define oo INT_MAX
#define inf 1000000000

const double pi = acos(-1.0);
const double eps = 1e-11;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main() {
std::ios_base::sync_with_stdio(0);
freopen("A-large.out","w",stdout);
freopen("A-large.in","r",stdin);
int T,tc,res,n=0;
cin>>T;
string s;
for(tc=1;tc<=T;tc++){
	res=0;
	cin>>n>>s;
	int cr=0;
	for(int i=0;i<=n;i++){
		if(i>cr){
			res++;
			cr++;
		}
		cr+=(s[i]-'0');
	}
	cout<<"Case #"<<tc<<": "<<res<<'\n';

}
	return 0;
}
