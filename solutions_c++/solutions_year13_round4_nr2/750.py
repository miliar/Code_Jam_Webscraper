//Done by Mycroft Grey
//Fet per Ferran Alet

#include<iostream>
#include<cmath>
#include<iomanip>
#include<vector>
#include<map>
#include<queue>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<numeric>
#include<set>
#include<sstream>
#include<list>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl
#define FOR(x,y) for(int x=0;x<y;x++)
#define FORU(x,y) for(int x=1;x<=y;x++)
using namespace std;


typedef long long ll;
typedef pair<int,int> PII;
typedef vector<long long> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;

ifstream fin("B-large.in");
ofstream fout("B-large.out");


int main(){
 // ios_base::sync_with_stdio(false);
 int casos;
 fin>>casos;
 for(int cas=1;cas<=casos;++cas){
    long long nn,p,n=1,x;
    fin>>nn>>p;
    for(int i=0;i<nn;++i) n*=2;
    cerr<<n<<endl;
    fout<<"Case #"<<cas<<": ";
    long long xx=0;
    x=1;
    while(2*x<=p) {x*=2; ++xx;}
    xx=nn-xx;
    long long res=1;
    for(int i=0;i<xx;++i) res*=2;
    long long first=n;
    long long second=n-res;
    if(p<n){
      p=n+1-p;
      xx=0,x=1;
      while(x<p){x*=2; ++xx;} //potential error
      x=nn+1-xx;
      res=1;
      for(int i=0;i<x;++i) res*=2;
      --res;
      first=res;
    }
    fout<<first-1<<' '<<second<<endl;
 }
}
