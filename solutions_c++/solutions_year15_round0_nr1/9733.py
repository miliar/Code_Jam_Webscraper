#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<set>
#include<map>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<iomanip>
#include<queue>
#include<stack>
#include<string.h>

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))

#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define RREPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define RFOR(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define RFOREACH(it,c) for(VAR(it,(c).rbegin());it!=(c).rend();++it)
#define CLEAR(x) memset(x,0,sizeof x);

#define MP make_pair
#define MAPI(t1,t2) map<t1,t2>::iterator
#define RMAPI(t1,t2) map<t1,t2>::reverse_iterator
#define eps 1.0e-11
#define PAUSE system("Pause");
#define LL long long
using namespace std;
#define DEBUG false

int main(){
	int N;
	int T=1;
	cin>>N;
	while(T<=N){
		int Si;
		string SS;
		cin>>Si;
		cin>>SS;
		int stood=SS[0]-48;
		int p=0;
		for(int i=1;i<Si+1;i++){
			if( (SS[i]-48)==0) continue;
			if(stood>=i){
				stood+= SS[i]-48;
			}else{
				p+=(i-stood);
				stood+=p;
				stood+= SS[i]-48;
			}
		}
		cout<<"Case #"<<T<<": "<<p<<endl;//answer here
		T++;
	}
	
	return 0;
}
