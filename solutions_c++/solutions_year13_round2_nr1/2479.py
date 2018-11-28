#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>
#include <math.h>
#define debug(x) cerr<<#x<<" = "<<(x)<<endl;

using namespace std;
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define VAR(a,b) __typeof(b) a=(b)
#define REVERSE(c) reverse(ALL(c))
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define MINN(X,Y) ((X) > (Y) ? (Y) : (X))
#define MAXX(X,Y) ((X) < (Y) ? (Y) : (X))
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<unsigned long long> VULL;
typedef vector<VI> VVI;
typedef unsigned long long ULL;
typedef long long LL;

#define dbv(x)   {for(int i=0;i<x.size();i++)  cerr<<x[i]; cerr<<endl;}

int a[1000], b[1000];
long double PI;
ULL cnt( ULL nowCnt, ULL nowSum, ULL index,  const VULL & input)
{
  //cout<<__LINE__<<" "<< nowCnt<<" "<<nowSum<<" " <<index <<endl;
  ULL rslt;
  if( index >= input.size())
    { 
      rslt = nowCnt;
      return rslt;
    }
  if( index == input.size() -1 ) 
    {
      if( nowSum > input[index] ) 
	return nowCnt;
      else 
	return nowCnt+1;
    }
  
  if(nowSum>input[index])
    {
      rslt= cnt(nowCnt, nowSum+input[index], index+1, input);
      return rslt;
    }
  else 
    {

      
ULL a2 = cnt(nowCnt+1, nowSum, index+1, input);
 rslt = a2;
 ULL tmpSum=nowSum;
 
 for( int kk=1; kk<= input.size() && tmpSum>1; kk++)
   {
     
     tmpSum += (tmpSum-1);
     //cout<<__LINE__<<" "<<kk<<"  "<<tmpSum<<endl;
     ULL a1 = cnt(nowCnt+kk, tmpSum, index, input);
     rslt = MINN( a1, rslt);
   }

      // if( nowSum*2 -1 > input[index] )
  // 	{ 	
  //        ULL a1 = cnt(nowCnt+1, nowSum*2-1, index, input);
  // 	 //cout<<__LINE__<<" "<< nowCnt+1<<" "<<nowSum*2-1<<" " <<index<<" "<< a1 <<endl; 
  // rslt = MINN(a1,a2);
  // 	}

     
       
      //cout<<__LINE__<<" "<< nowCnt+1<<" "<<nowSum <<" " <<index+1<<" "<< a2 <<endl;
      //cout<<__LINE__<<" "<< nowCnt<<" "<<nowSum<<" " <<index<<" "<< rslt <<endl;
  return rslt;
    }
 
}

void solve()
{
   unsigned long long A, N;
  cin >> A>>N;
  VULL motes; 
  for(int i=0; i< N ; i++)
    {
      LL a;
      cin >> a;
      motes.push_back(a);
    }
  SORT(motes);
  ULL index=0;
  ULL sum =A; 
  
  for( index=0; index<motes.size(); index++)
    {
      if( motes[index] < sum )
	{
	  sum+=motes[index];
	}
      else 
	{
	  break;
	}
    }
  //cout<<"Begin"<<endl;
  //cout<< A<<" >>";
  //for(int k=0; k< motes.size(); k++)
  // cout<< motes[k] << "  ";
  //cout<<endl;
  cout<< cnt(0, A, 0, motes)<<endl;

}


int main()
{
  PI=atan(1)*4;
  int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ", t);
        solve();
    }
  return 0;
}
