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

int shy[1005];

int main() {
  ofstream fout ("A-large.out");
  ifstream fin ("A-large.in");
  string s,t,u;
  int a,b,c,d,e,f,g,h,i;
  C>>a;
  for(b=1;b<=a;b++){
  	C>>c>>s;
  	for(d=0;d<=c;d++){
  		t=s[d];
  		stringstream(t)>>e;
  		shy[d]=e;
  	}
  	i=0; h=0;
  	for(d=0;d<=c;d++){
  		if(shy[d]>0)
  		{
  		
  		if(i>=d){
  			i+=shy[d];
  		}else{
  			h+=d-i;
  			i=d+shy[d];
  		}
  		
  		}
  	}
  	co<<"Case #"<<b<<": "<<h;
  	E;
  }
  return 0;
}
