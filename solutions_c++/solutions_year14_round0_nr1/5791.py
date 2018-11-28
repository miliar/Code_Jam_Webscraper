//Problem A. Magic Trick.cpp
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
  int T,ans1,ans2;
  int mat[4][4];
  cin>>T;
  for(int tc=0;tc<T;++tc){

    cin>>ans1;
    map<int, int> chk;
    for(int i=0;i<4;++i){
      for(int j=0;j<4;++j){
        cin>>mat[i][j];
      }
    }
    for(int i=0;i<4;++i){
      chk[mat[ans1-1][i]]++;
    }
    cin>>ans2;
    for(int i=0;i<4;++i){
      for(int j=0;j<4;++j){
        cin>>mat[i][j];
      }
    }

    for(int i=0;i<4;++i){
      chk[mat[ans2-1][i]]++;
    }
    int ct=0;
    int ans=0;
    tr(chk,it){
      if(it->second==2){
        ct++;
        ans=it->first;
      }

    }
    if(ct>1){
      cout<<"Case #"<<tc+1<<": "<<"Bad magician!"<<endl;
    }else if(ct==1){
      cout<<"Case #"<<tc+1<<": "<<ans<<endl;
    }else{
      cout<<"Case #"<<tc+1<<": "<<"Volunteer cheated!"<<endl;

    }

  }
  return 0;
}
