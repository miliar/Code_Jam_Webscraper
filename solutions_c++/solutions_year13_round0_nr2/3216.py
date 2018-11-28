#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include<cstring>
using namespace std;
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,a,b) for(int (i)=a;(i)<(b);(i)++)
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define _mp make_pair
#define MOD 1000000007
#define MAXN 200020
bool checkPossibility(vector<vector<int> >v,int num,int row,int col,int n,int m){
   bool temp=true;
   for(int i=0;i<n;i++)
    if(v[i][col]>num){
      temp=false;
      break;
    }
   if(temp)return true;
   temp=true;
   for(int i=0;i<m;i++)
    if(v[row][i]>num){
      temp=false;
      break;
    }
   return temp;
}

bool findNumber(vector<vector<int> >v,int num,int n,int m){

  for(int i=0;i<n;i++)
    for(int j=0;j<m;j++){
      if(v[i][j]==num){
        if(!checkPossibility(v,num,i,j,n,m))
            return false;
      }
    }
   return true;
}

int main()
{
  //freopen("B.in","r",stdin);
  //freopen("out.txt","w",stdout);
  int T,n,m,x,number=0;
  cin>>T;
  while(T--){
       n=SS,m=SS;
       vector<vector<int> >v(n);
       number++;
       for(int i=0;i<n;i++)
        for(int j=0;j<m;j++){
          x=SS;
          v[i].push_back(x);
       }
       cout<<"Case #"<<number<<": ";
       int no=99;
       bool possible=true;
       while(no>=1){
         possible=findNumber(v,no,n,m);
         no--;
         if(!possible)break;
       }
       if(possible){
        cout<<"YES"<<endl;
       }else{
        cout<<"NO"<<endl;
       }
  }

  return 0;
}
