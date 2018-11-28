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

bool helper(vector<int> Input,int y,ll total){
  int x=0;
  int sz=Input.size();
  for(;x<y;x++){
      if((sz+x)*(y-x)>=total){
        int ma=y-x;
        int now=x;

        int i;
        for(i=sz-1;i>=0;i--){
        // cout<<"here now i "<<Input[i]<<"ma "<<ma<<endl;
          if(Input[i]<ma|| now<0)
            break;
          if(Input[i]%ma==0){
          now-=(Input[i]/ma-1);
          }
          else{
            now-=Input[i]/ma;
          }
      //  cout<<"here now now"<<now<<endl;
        }
       // cout<<"here after now" <<now<<endl;
        //cout<<"Input"<<Input[y-x]<<endl;
        if(now>=0 )
          return true;
      }

  }
  return false;

}


int main()
{

   //freopen("B-small-attempt4.in","r+",stdin);
 // freopen("B-small-attempt4.out","w+",stdout);
    freopen("B-large.in","r+",stdin);
   freopen("B-large.out","w+",stdout);
    int tc;
    cin>>tc;
    FOR(cs,0,tc){
        int N;
        int res=0;
        cin>>N;
        vector<int> plats;
        vector<int> resl;
        ll total=0;
        FOR(i,0,N){
          int tmp;
          cin>>tmp;
          total+=tmp;
          plats.push_back(tmp);
        }
        sort(plats.begin(),plats.end());
        res=plats[plats.size()-1];
        resl.push_back(res);
        int start=0;
       // cout<<" "<<res<<endl;
        int last=res;
        while(start+1<last){
          int mid=start+(last-start)/2;
          //cout<<"here"<<mid<<endl;
          if(helper(plats,mid,total)){
            last=mid;
           // cout<<"here find"<<mid<<endl;
            resl.push_back(mid);
          }
          else{
            start=mid;
          }
        }

        if(helper(plats,start,total)){
           resl.push_back(start);
        }
        if(helper(plats,last,total)){
           resl.push_back(last);
        }
        sort(resl.begin(),resl.end());

        cout<<"Case #"<<cs+1<<": "<<resl[0]<<endl;
    }
	return 0;
}
