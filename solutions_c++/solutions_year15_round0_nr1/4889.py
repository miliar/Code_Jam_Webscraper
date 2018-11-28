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
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <ctime>
#include "time.h"
#include "stdio.h"
#include "stdlib.h"
#include <iomanip>
using namespace std;

#define FOR(i,a,b) for (int i(a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;



int main()
{

   freopen("A-small-attempt1.in","r+",stdin);
   freopen("A-small-attempt1.out","w+",stdout);
     // freopen("A-large.in","r+",stdin);
   //freopen("A-large.out","w+",stdout);
     int tc;
    cin>>tc;
    FOR(cs,0,tc){
        int N;
        int res=0;
        cin>>N;
        string shy;
        cin>>shy;
        int sumnow=shy[0]-'0';

        FOR(i, 1, N+1){
          int need=0;
          if(shy[i]-'0'==0)
            continue;
          need=i-sumnow;
         // cout<<i<<" "<<sumnow<<" "<<need<<endl;
          if(need>0){
            res+=need;
            sumnow+=res;
          }
          sumnow+=shy[i]-'0';

        }



        cout<<"Case #"<<cs+1<<": "<<res<<endl;
    }
	return 0;
}
