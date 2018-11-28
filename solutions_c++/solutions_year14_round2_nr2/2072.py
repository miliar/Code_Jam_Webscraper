#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <math.h>

using namespace std;

int T,A,B,K;
int main(){
  cin>>T;
  for(int caseNo = 1;caseNo<=T;++caseNo){
    cin>>A>>B>>K;
    int sum = 0;
    for(int i=0;i<A;++i)
      for(int j=0;j<B;++j){
	if( (i&j)<K )
	  sum++;
      }
    cout<<"Case #"<<caseNo<<": "<<sum<<endl;
  }
  return 0;
}
