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
int main( int argc, char** argv )
{
	auto result = freopen("input.txt","r",stdin);
	result = freopen("output.txt","w+",stdout);
	int t;
	S(t);
	REP(test,t){
		cout<<"Case #"<<test+1<<": ";
		int n;
		S(n);
		int first[4][4];
		REP(i,4){
			REP(j,4){
				S(first[i][j]);
			}
		}
		int m;
		S(m);
		int second[4][4];
		REP(i,4){
			REP(j,4){
				S(second[i][j]);
			}
		}
		bool found = false;
		int number = -1;
		set<int> collide;
		REP(i,4){
		collide.insert(first[n-1][i]);
		}
		int cntr = 0;
		REP(i,4){
			if(collide.find(second[m-1][i])!=collide.end()){
				cntr++;
				if(cntr>1) break;
				number = second[m-1][i];
			}
		}
		if(cntr==0){
			cout<<"Volunteer cheated!"<<endl;
		 }else if(cntr==1){
			 cout<<number<<endl;
		 }else{
			 cout<<"Bad magician!"<<endl;
		 }
	}
	return 0;
}
