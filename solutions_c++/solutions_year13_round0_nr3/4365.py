#include <cstdio>
#include <iostream>
#include <numeric>
#include <fstream>
#include <map>
#include <algorithm>
#include <bitset>
#include <set>
#include <vector>
#include <utility>
#include <cstring>
#include <string>
#include <cctype>
#include <cmath>
#include <climits>
using namespace std;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> pi;
typedef vector< pi > vpi;
typedef vector< vpi > vvpi;
#define rep(i,a,b) for(i = a;i<=b;i++)
#define all(c) (c).begin(),(c).end()
#define present(c,x) (c).find(x)!=(c).end()
#define gpresent(c,x) find(all(c),x)
#define tr(c,it) for( typeof(c) it = (c).begin();it!=(c).end();it++ )
#define accu(c) accumulate(all(c),0)
#define scalar(c1,c2) inner_product(all(c1),(c2).begin(),0)
#define maxel(c) max_element(all(c))
#define minel(c) min_element(all(c))
#define Size(C) C.size();
#define fx first
#define sx second
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define inf -300010
#define ll long long
#define M 1000000007

ifstream in("C-large-1.in",ios::in);
ofstream out("output.out",ios::out);
  
 int T,i;
 ll a,b;
 set< ll > st;
 set< ll >::iterator it,jt;
 bool cur[1010];
 
 bool isPalin(ll num){
 	ll k = num,n=0;
 	while(k>0){
 		n = n*10 + k%10;
 		k/=10;
 	}
 	if(n==num)
 		return 1;
 	return 0;
 }
 
 void gen(){
   int d1,d2,d3,d4;
   ll num;
   // len = 1 or len = 2
   	rep(d1,1,9){
   		num = d1;
   		if(isPalin(d1*d1)){
   			st.insert(d1*d1);
   		}
   		num = d1*10 + d1;
   		if(isPalin(num*num)){
   			st.insert(num*num);
   		}
   	}
   	// len = 3 or len = 4
   	rep(d1,1,9){
   		rep(d2,0,9){
   			num = d1*100+d2*10+d1;
   			if(isPalin(num*num)){
   				st.insert(num*num);
   			}
   			num = d1*1000+d2*100+d2*10+d1;
   			if(isPalin(num*num)){
   				st.insert(num*num);
   			}
   		}
   	}
   	//len = 5 or len = 6
   	rep(d1,1,9){
   		rep(d2,0,9){
   			rep(d3,0,9){
   				num = d1*10000 + d2*1000 + d3*100 + d2*10 + d1;
   				if(isPalin(num*num)){
   					st.insert(num*num);
   				}
   				num = d1*100000 + d2*10000 + d3*1000 + d3*100 + d2*10 + d1;
   				if(isPalin(num*num)){
   					st.insert(num*num);
   				}
   			}
   		}
   	}
 	//len = 7 
 	rep(d1,1,9){
 		rep(d2,0,9){
 			rep(d3,0,9){
 				rep(d4,0,9){
 					num = d1*1000000 + d2*100000 + d3*10000 + d4*1000 + d3*100 + d2*10 + d1;
 					if(isPalin(num*num)){
 						st.insert(num*num);
 					}
 				}
 			}
 		}
 	}
 }
 
 int main(){
  int t;
  ll c = 0;
  set < ll >::iterator i;
  gen();
  in>>T;
  
  rep(t,1,T){
  	in>>a>>b;
  	c = 0;
  	it = st.lower_bound(a);
  	jt = st.upper_bound(b);
  	
  	for(i = it;i!=jt;i++)
  		c++;
  	out<<"Case #"<<t<<": "<<c<<"\n";
  }
  return 0;
 }
