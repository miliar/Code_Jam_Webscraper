#include <cassert>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <utility>
#include <iomanip>
#define PR(x) cout<<#x<<"="<<x<<endl
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a) for(int i=0;i<a;i++)
#define RP(i,init,a) for(int i=init;i<a;i++)
#define S(x) cin>>x
#define PRARR(x,n) for(int i=0;i<n;i++)printf(#x"[%d]=\t%d\n",i,x[i])
#define rd(arr,i,n) for(int i=0;i<n;i++) cin>>arr[i]
#define PB push_back
#define SUM(arr,n,sum) {sum=0;for(int i=0;i<n;i++) sum+=arr[i]; }
#define VC vector
#define CLR(arr) memset(arr,0,sizeof(arr))
#define FILL(arr,val) memset(arr,val,sizeof(arr))
#define TR(iter, container) for(auto iter = container.begin();iter!=container.end();iter++ )
using namespace std;
int main()
{
int t;
freopen("input.txt","r",stdin);
freopen("output.txt","w+",stdout);

S(t);
REP(test,t){
 cout<<"Case #"<<test+1<<": ";
 int blocks;
 S(blocks);
 float N[blocks];
 float K[blocks];
 REP(i,blocks) S(N[i]);
 REP(i,blocks) S(K[i]);
 sort(N, N + blocks);sort(K, K + blocks);
 int cnt1=0,cnt2=0;
 int cntr=blocks-1;
for(int i=blocks-1;i>=0;i--){
	if(N[i]>K[cntr]){
	   cnt2++;
	}else{
		cntr--;
	}
	
}
	
   cntr=0;
   REP(i,blocks){
   if(N[i]>K[cntr]){
		cnt1++;
		cntr++;
	}
}
   
cout<<cnt1<<" "<<cnt2<<endl;
}
return 0;
}