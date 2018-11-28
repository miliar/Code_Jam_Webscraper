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

int main(){
	int N;
	int T=1;
	cin>>N;
	while(T<=N){
		int X,R,C;
		cin>>X>>R>>C;
		int A = R*C;
		if(X > R*C || A%X!=0){
			cout<<"Case #"<<T<<": RICHARD"<<endl;//answer here
			T++; 
			continue;
		}
		if(X==1){
			cout<<"Case #"<<T<<": GABRIEL"<<endl;//answer here
		}
		if(X==2){
			cout<<"Case #"<<T<<": GABRIEL"<<endl;//answer here
		}
		
		if(X==3){
			if(A==3) {
				cout<<"Case #"<<T<<": RICHARD"<<endl;//answer here
			}else{
				cout<<"Case #"<<T<<": GABRIEL"<<endl;//answer here
			}
			
		}
		if(X==4){
			if(A==4 || A==8){
				cout<<"Case #"<<T<<": RICHARD"<<endl;//answer here
			}else{
				cout<<"Case #"<<T<<": GABRIEL"<<endl;//answer here
			}
		}
		T++;
		
	}
	
    return 0;

}

