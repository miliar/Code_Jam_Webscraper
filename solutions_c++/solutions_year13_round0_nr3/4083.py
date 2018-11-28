/*
ID: prodigyaj
LANG: C++
TASK:
*/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cstring>

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)
#define pb push_back
#define C(x) cout<<x<<" "
#define CE(x) cout<<#x<<" : "<<x<<endl

using namespace std;
using namespace __gnu_cxx;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;



bool check(ll n)
{
     string s;
     while(n!=0)
     {
                s.pb(n%10+48);
                n/=10;
     }
     int i=0,j=s.size()-1;
     while(i<j)     
         if(s[i++]!=s[j--])
             return false;
     
     return true;
}

vector <ll> len;

void precal()
{
     for(ll i=1;i<=2001003;i++)
          if(i%10!=0)
          if(check(i) && check(i*i))
          { 
                      len.pb((i*i));
                      //cout<<i<<"\t\t"<<i*i<<endl;
          }
}

int main()
{
    int t;  
    precal();
    //cout<<len.size();
    S(t);
    FORE(test,t)
    {
                ll a,b;cin>>a>>b;
                int cnt=0;
                for(int i=0;i<len.size();i++)
                    if(len[i]>=a && len[i]<=b)
                       cnt++;
                printf("Case #%d: %d\n",test,cnt);
    }
return 0;
}
