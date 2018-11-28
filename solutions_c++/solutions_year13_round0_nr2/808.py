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
int arr[105][105];
int n,m;
bool check()
{
     FO(i,n) FO(j,m)
     {
          bool c=1,r=1;
          int cur=arr[i][j];
          for( int k=0 ; k<m && r ; k++ ) if(arr[i][k]>cur) r=0; 
          for( int k=0 ; k<n && c && !r ;k++) if(arr[k][j]>cur) c=0;
          
          if(c==0&&r==0) return 0; 
     }
     return 1;
}


int main()
{
   READ("B-large.in");
   WRITE("B-large.out");
   
   
   int t,a=1;
   cin>>t;
   while(t--)
   {
       cin>>n>>m;
       FO(i,n) FO(j,m) cin>>arr[i][j];
       if(check()) cout<<"Case #"<<a<<": YES"<<endl;
       else   cout<<"Case #"<<a<<": NO"<<endl;  
       a++;
   }
   
   return 0;    
}

