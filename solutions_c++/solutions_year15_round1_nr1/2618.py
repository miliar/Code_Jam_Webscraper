#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <ctime>

#define FOR(i,a,b) for (int i(a); i < (b); i++)
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define ms0(x) memset((x),0,sizeof(x))
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define rep(i,m,n) for(int i=(m),_end=(n);i < _end;++i)
#define repe(i,m,n) for(int i=(m), _end =(n);i <= _end;++i)
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
using namespace std;

int main(){
    freopen("C:\\Users\\chmffwn1\\Downloads\\A-large.in", "r", stdin);
    freopen("C:\\Users\\chmffwn1\\Downloads\\A-large.out", "w", stdout);
    int tc;
    cin>>tc;
    FOR(cs,0,tc){
      ll y=0,z=0;
      int n;
      cin>>n;
      vector<int> m;
      FOR(i,0,n){
        int tmp;
        cin>>tmp;
        m.push_back(tmp);
      }
      int maxsb=0;
      int maxpos=0;
      FOR(i,1,n){
        int sub=m[i-1]-m[i];
        if(sub>=0){
          y+=sub;

        if(sub>maxsb){
          maxsb=sub;
          maxpos=i;
        }
        }
      }
      int sped=maxsb;

      FOR(i,0,n-1){
          if(m[i]<sped){
            z+=m[i];
          }
          else{
            z+=sped;
          }

      }

      cout<<"Case #"<<cs+1<<": "<<y<<" "<<z<<endl;
    }
	return 0;
}
