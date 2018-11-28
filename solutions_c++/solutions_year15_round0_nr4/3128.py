//    Author : Nishanth Vijayan IIT Ropar,India.
//
//	  Spoj 		  : http://www.spoj.com/users/nishanth_v/
//	  HackerEarth : http://www.hackerearth.com/users/nishanththegr8/
//	  Facebook	  : https://www.facebook.com/NishanthTheGr8
//    Motto       : The Less You Give A Fuck, The Happier You'll Be. :)


#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <list>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
#include <cstring>


#define ABS(x) ((x)<0?-(x):(x))
#define pnl printf("\n");
#define REP(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FOR(i,a,b) for(__typeof(b) i=(a);i<(b);++i)
#define FORE(i,a,b) for(__typeof(b) i=(a);i<=(b);++i)
#define FOREACH(i,s) for(__typeof((s).begin()) i=(s).begin();i!=(s).end();i++)
#define UNIQUE(v) sort(ALL(v)),v.erase(unique(ALL(v)),v.end())
#define FILL(a,b) memset(a,b,sizeof(a))

#define pi acos(-1)
#define INF 0x3f3f3f3f
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
#define LLI long long 
#define gc getchar_unlocked
#define pc putchar_unlocked
#define MAX 100000

using namespace std;

typedef pair<LLI, LLI> ii;
typedef vector<LLI, LLI> vi;



int main(){

LLI T,x,r,c,product;
cin>>T;
FOR(t,1,T+1){
 cin>>x>>r>>c;
 product=r*c;
 if(x==1){
 	cout<<"Case #"<<t<<": GABRIEL"<<endl;
 }
 else if(x==2){
 	if(product%2==0)cout<<"Case #"<<t<<": GABRIEL"<<endl;		
 	else 			cout<<"Case #"<<t<<": RICHARD"<<endl;
 }
 else if(x==3){
 	if(product%3==0 && product!=3)cout<<"Case #"<<t<<": GABRIEL"<<endl;	
 	else						  cout<<"Case #"<<t<<": RICHARD"<<endl;
 }
 else if(x==4){
 	if(product%4==0 && product>8)cout<<"Case #"<<t<<": GABRIEL"<<endl;	
 	else						  cout<<"Case #"<<t<<": RICHARD"<<endl;	
 }
}

return 0;
}