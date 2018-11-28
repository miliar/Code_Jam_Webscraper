//Problem B. Cookie Clicker Alpha.cpp
//SmartCoder
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

const double pi=acos(-1.0);
const double eps=1e-11;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int main(){
  std::ios_base::sync_with_stdio(0);
  freopen("output.txt","w",stdout);
  freopen("input.txt","r",stdin);
  double C,F,X,FC,mn=inf;
  int tc;
  cin>>tc;
  for(int T=1;T<=tc;++T){
    double tot=0.0;
    mn=inf;
    cin>>C>>F>>X;
    FC=2;
    double preMin=inf-1;
    while(true){
      mn=min(mn,tot+(X/FC));
      if(fabs(preMin-mn)<eps)break;
      preMin=mn;
      tot+=(C/FC);
      FC+=F;
    }
    cout<<fixed;
    cout<<setprecision(7);
    cout<<"Case #"<<T<<": "<<mn<<endl;

  }
  return 0;
}
