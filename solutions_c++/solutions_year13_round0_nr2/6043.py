#include<iostream>
#include<stdio.h>
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<sstream>
using namespace std;

ifstream fh("B-small-attempt6.in");
ofstream fho("B-small.out");
//ifstream fh("C-large.in");
//ofstream fho("C-large-output.in");

int main(){
  int n,p,q,a[100][100],i,j,t=0;
  string s;
  fh>>n;
      //fh>>s;
      //istringstream iss(s);
  while(t<n){
    fh>>p>>q;
    i=0;
    while(i<p){
      j=0;
      while(j<q){
        fh >> a[i][j++];
      }
      ++i;
    }
    int flag,sma;
    for(i=0;i<p;++i){
      flag=sma=0;
      for(j=0;j<q;++j)if(a[i][sma] > a[i][j])sma = j;
      cout<<"i= "<<i<<" sma = "<<sma<<endl;
      
      int tem = a[i][sma],k;
      for(sma=0;sma<q;++sma){
        if(a[i][sma]==tem){
          for(j=0;j<q;++j){
            if(tem != a[i][j]){
              for(k=0;k<p;++k){
                cout<<"in flag=1 "<<k<<" "<<sma<<" "<<a[i][sma]<<" "<<a[k][sma]<<endl;
                if(a[i][sma] != a[k][sma]){
                  flag = 1;
                  fho<<"Case #"<<t+1<<": NO"<<endl;
                  break;
                }
              }
              break;
            }
          }
          if(flag==1)break;
        }
      }
      if(flag==1)break;
    }
    if(flag!=1)fho<<"Case #"<<t+1<<": YES"<<endl;
    ++t;
  }
  fho<<endl;
  return 0;
}
