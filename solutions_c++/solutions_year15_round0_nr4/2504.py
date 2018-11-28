#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <fstream>

#define C fin
#define co fout
#define E fout<<endl

using namespace std;

int plt[1005];

int main() {
  ofstream fout ("D-small-attempt3.out");
  ifstream fin ("D-small-attempt3.in");
  int a,b,c,d,e,f,g,h,i;
  C>>a;
  for(b=1;b<=a;b++){
  	C>>c>>d>>e;
  	f=c/2;
  	co<<"Case #"<<b<<": ";
  	if(c==1){
  		co<<"GABRIEL";
  	}else
  	if((c==2) && ((d%2==0) || (e%2==0))){
  		co<<"GABRIEL";
  	}else
  	if((d*e)%c!=0){
  		co<<"RICHARD";
  	}else
  	if((d<c) && (e<c)){
  		co<<"RICHARD";
  	}else
	if((d<=f) || e<=f){
		co<<"RICHARD";
	}else{
  		co<<"GABRIEL";
  	}
  	E;
  }
  return 0;
}
