#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <math.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

#define forn(i,n) for (int i=0;i<n;i++)
#define pb push_back

int main(){
  int n,t;
  //int app[10]={0};

  cin>>t;

  forn (i,t){
    cin>>n;
    int a=0;
    //int curr=n;
    int app[10]={0};
    while (n!=0&&not(app[0]==1&&app[1]==1&&app[2]==1&&app[3]==1&&app[4]==1&&app[5]==1&&app[6]==1&&app[7]==1&&app[8]==1&&app[9]==1)){
      a=a+n;
      //cout<<a;
      int curr=a;
      while (curr>0){
        int temp = curr % 10;
        //cout<<a<<endl;
        app[temp]=1;
        curr=curr/10;
      }

    }

    if (n!=0) cout<< "Case #"<<i+1<<": "<<a<<endl;
    else cout<< "Case #"<<i+1<<": INSOMNIA"<<endl;
  }
  return 0;

  }
