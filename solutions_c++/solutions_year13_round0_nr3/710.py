#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
#include <sstream>
#include <string>
using namespace std;

#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp make_pair
#define pb push_back
#define sz size()
#define F first
#define S second
#define FO(i,x) for(int i=0;i<x;i++)
#define FOR(i,s,e) for(int i = int(s); i < int(e); i++)

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

string arr[]={"1","4","9","121","484","10201","12321","14641","40804","44944","1002001","1234321","4008004","100020001","102030201","104060401","121242121","123454321","125686521","400080004","404090404","10000200001","10221412201","12102420121","12345654321","40000800004","1000002000001","1002003002001","1004006004001","1020304030201","1022325232201","1024348434201","1210024200121","1212225222121","1214428244121","1232346432321","1234567654321","4000008000004","4004009004004"};
vector <unsigned long long int> v;
unsigned long long int TOI(string s)
{
     unsigned long long int x;
     stringstream ss;
     ss<<s;
     ss>>x;
     return x;
}

int main()
{
    READ("C-large-1.in");
    WRITE("C-large-1.out"); 
   FO(i,39) v.pb( TOI(arr[i]) );
  
   int t,a=1,res;
   unsigned long long int x,y;
   cin>>t;
   while(t--)
   {
      res=0;       
      cin>>x>>y;
      FO(i,v.sz) if(v[i]>=x&&v[i]<=y) res++;   
      cout<<"Case #"<<a<<": "<<res<<endl;    
      a++;
   }
 
   return 0;    
}

