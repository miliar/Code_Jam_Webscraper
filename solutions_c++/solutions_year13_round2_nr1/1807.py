#include<stdio.h>
#include<stdlib.h>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

long memo[100][1000000];

long M;

long solve(long i,long a,vector<long> motes){
  if(i>=motes.size())
    return 0;
  else{
    long m;
    if(a<1000000 && memo[i][a]>=0){
      return memo[i][a];
    }
    if(motes[i]<a){
      int add = solve(i+1,a+motes[i],motes);
      m = add;
    }else{
      int add_val = (a-1);
      if(add_val>0){
        int add = 1+solve(i,a+add_val,motes);
        int remove = 1+solve(i+1,a,motes);
        m = min(add,remove);
      }else
        m = 1+solve(i+1,a,motes);
    }
    if(a<1000000)
      memo[i][a]=m;
    return m;
  }
}

int main(){
  long T,n,a,k;
  cin >> T;
  for(long t=1;t<=T;++t){
      cout << "Case #"<<t<<": ";
      cin >> a;
      cin >> n;
      vector<long> motes;
      for(long i=0;i<n;++i){
        cin >> k;
        motes.push_back(k);
      }
      for(long i=0;i<100;++i)
        fill_n(memo[i],1000000,-1);
      sort(motes.begin(),motes.end());
      cout << solve(0,a,motes) << endl;
  }
  return 0;
}
