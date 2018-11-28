/*
 * a.cpp
 *
 *  Created on: 2017/04/08
 *      Author: DO
 */

#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<functional>
#include<utility>
#include<bitset>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstdio>

using namespace std;

#define REP(i,n) for(int i=0;i<int(n);i++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long ll;
typedef pair<int,int> P;

int face[1010],t[1010];

int main(void){
	          int i;

	      	  int T;
	      	  cin >> T;
	      	  REP(tc,T){

	      		  string s;
	      		  int k;
	      		  cin >> s >> k;
	      		  int n=s.size();
	      		  for(i=0;i<n;i++) t[i]=0;
	      		  for(i=0;i<n;i++){
	      			  if(s[i]=='+') face[i]=0;
	      			  else face[i]=1;
	      		  }

	      		  int ans=0,sum=0;
	      		  for(i=0;i<=n-k;i++){
	      			  if((face[i]+sum)%2==1){
	      				  ans++;
	      				  t[i]=1;
	      			  }
	      			  sum+=t[i];
	      			  if(i-k+1>=0){
	      				  sum-=t[i-k+1];
	      			  }
	      		  }

	      		  cout << "Case #" << tc+1 << ": ";

	      		  bool g=true;
	      		  for(i=n-k+1;i<n;i++){
	      			  if((face[i]+sum)%2==1){
	      				  g=false;
	      				  break;
	      			  }
	      			  if(i-k+1>=0){
	      				  sum-=t[i-k+1];
	      		      }
	      		  }

	      		  if(g) cout << ans << endl;
	      		  else cout << "IMPOSSIBLE" << endl;

	      	}

	          return 0;
}



