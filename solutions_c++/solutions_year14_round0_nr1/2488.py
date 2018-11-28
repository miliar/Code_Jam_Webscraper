#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
#include <stack>
#include <cctype>
#include <utility>
#include <map>
#include <string>
#include <climits>
#include <set>
#include <string>
#include <sstream>
#include <utility>
#include <ctime>
using namespace std;
typedef long int int64;
typedef long long int int64l;
typedef unsigned long long uint64l;
typedef unsigned long uint64;

int main(){
  int t,c=1,a,b,i,j,u,f,num;
  int p1[4],p2[4];
  string s;
  cin>>t;
  while(t--){
    cin>>a;
    a--;
    for(i=0;i<4;i++){
      if(i==a){
	for(j=0;j<4;j++){
	  cin>>p1[j];
	}
      }
      else{
	for(j=0;j<4;j++){
	  cin>>u;
	}
      }
    } 


    cin>>b;
    b--;
    for(i=0;i<4;i++){
      if(i==b){
	for(j=0;j<4;j++){
	  cin>>p2[j];
	}
      }
      else{
	for(j=0;j<4;j++){
	  cin>>u;
	}
      }
    }
    
    f=0;
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
	if(p1[i]==p2[j]){
	  f++;
	  num=p1[i];
	break;
	}
      }
    }
    cout<<"Case #"<<c<<": ";
    if(f==0)
      cout<<"Volunteer cheated!"<<endl;
    else if(f==1)
      cout<<num<<endl;
    else
      cout<<"Bad magician!"<<endl;
    c++;
  }
}

