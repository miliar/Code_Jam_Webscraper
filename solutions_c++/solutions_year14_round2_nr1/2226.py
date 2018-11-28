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

vector<vector<int> > table(101,vector<int>(26,0));
string strs[101];

int solve(int N){
  /*
  for(int i=1;i<N;++i){
    for(int j=0;j<26;++j){
      if( (table[0][j] == 0 && table[i][j]>0) ||
	  (table[0][j] > 0 && table[i][j]==0) ){
	return -1;
      }
    }
  }
  */
  //cout<<"0 :"<<strs[0]<<endl;
  for(int i=1;i<N;++i){
    //cout<<i<<" :"<<strs[i]<<endl;
    if( strs[0].compare(strs[i]) != 0 )
      return -1;
  }

  vector<int> avg(26,0);
  for(int i=0;i<N;++i)
    for(int j=0;j<26;++j)
      avg[j] += table[i][j];

  for(int i=0;i<26;++i){
    avg[i] = ((double)avg[i]/(double)N) + 0.5;
  }
   
  
  int sum = 0;
  for(int i=0;i<N;++i)
    for(int j=0;j<26;++j){
      sum += fabs(avg[j] - table[i][j]);
    }
  return sum;
}

int main(){
  int T,n;
  cin>>T;
  for(int i=0;i<T;++i){
    cin>>n;
    
    for(int j=0;j<n;++j){
      fill(table[j].begin(),table[j].end(),0);
      cin>>strs[j];
      for(int k=0;k<strs[j].length();++k){
	table[j][strs[j][k]-'a']++;
      }
      int _size = unique(strs[j].begin(),strs[j].end()) - strs[j].begin();
      strs[j].resize(_size);
    }

    cout<<"Case #"<<i+1<<": ";

    int ret = solve(n);
    if( ret==-1){
      cout<<"Fegla Won"<<endl;
    }
    else
      cout<<ret<<endl;
  }
  return 0;
}
