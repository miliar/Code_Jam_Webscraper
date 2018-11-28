//#include <bits/stdc++.h>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <math.h>
#define LIM         1110
#define loop(i,a,b) for(i=a;i<b;i++)
#define SET(a,b)    memset(a,b,sizeof a)
#define pb          push_back
using namespace std;
typedef vector<int> vi;

int cant[LIM];

int main(){
  int n,sm,i,casos=1,ans,sum;
  scanf("%d",&n);
  while(n--){
  	ans=sum=0;
  	SET(cant,0);
  	scanf("%d",&sm);
  	scanf("%1d",&cant[0]);
  	loop(i,1,sm+1){
  		scanf("%1d",&cant[i]);
  		sum+=cant[i-1];
  		if(sum<i) ans+=i-sum, sum+=i-sum;
  	}
  	printf("Case #%d: %d\n",casos++,ans);
  }
  return 0;
}