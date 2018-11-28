#include <cassert>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <bitset>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <iterator>

#define FOR(i,n)   for(int i=0;i<n;i++)
#define FORA(a,i,n)   for(int i=a;i<n;i++)
using namespace std;
template<class T> string tostring(T x){
ostringstream sout;
sout<<x;
return sout.str();
}
template< class T > int toint( T s ){
int v;
istringstream sin(tostring(s));
sin>>v;
return v;
}
vector< string > split( string sentence ){
   istringstream iss( sentence );
   vector< string > tokens;
   copy( istream_iterator< string >(iss), istream_iterator< string >(), back_inserter<vector< string > >(tokens));
   return tokens;
}
string conversion(int a, int b){

       string cambio;
       int suma=0;
       int coci = a;
       while(coci>0){
                     cambio += tostring(coci%b);
                     coci = coci/b;
      }
     return string(cambio.rbegin(),cambio.rend());

       }
int GCD( int a , int b ) {
     if ( a%b==0) return b ;
      else
      return GCD( b , a % b) ;
}

string flip( string s, int i){
   int start = 0;
   bool in = (!(i%2)?false:true);
   i--;
   
   while( start < i ){
      s[start]= s[start]=='-'?'+':'-';
      s[i]= s[i]=='-'?'+':'-';
      swap(s[start++],s[i--]);
      
   }
   if(in)
    s[start]= s[start]=='-'?'+':'-';
    //cout <<s<<endl;
   //system("pause"); 
   return s;
   
}
void debug(string s, int n){
   
   cout<<"d:: "<<s<<" : "<<n<<endl;
}

int solve( string s, int res  ){
   set<string> visited;
   queue<pair<string,int> > neigh;
   int N = s.size();
   string goal = string(N,'+');
   neigh.push(make_pair(s,res));
   //cout<<neigh.size()<<endl;
   //cout<<goal<<endl;
   //system("pause");
   while(neigh.size()>0){
      pair<string,int> node = neigh.front();
      neigh.pop();
      //debug(node.first,node.second);
     // system("pause");
      visited.insert(node.first);
      if(node.first.compare(goal) == 0) {return node.second;}
      FOR(i,N){
         string tmp = flip((node.first),i+1);
         if(visited.count( tmp )==0)
            neigh.push(make_pair( tmp ,node.second+1));
      }
   }
   //cout<<"paila mi ñero"<<endl;
   return res;
}
int main(){
    freopen("input.in","r",stdin);
    freopen("out.out","w",stdout);
    int n;
    cin>>n;
    string s;
    int cases=1;
    int res;
    while(n--){
         cin>>s;
         res = solve( s, 0 );
         printf("Case #%d: %d\n",cases++, res);
    }
    //string k ="+-";
    //flip(k,2);
    //system("pause");
    return 0;

    }
