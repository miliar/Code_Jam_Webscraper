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
int stoi(string s){
stringstream ss;
ss<<s;
int n;ss>>n;
return n;
}
string itos(long long n){
stringstream ss;
ss<<n;
return ss.str();
}

int main(){
	int T;
	cin>>T;
	for(int count=1;count<=T;count++){
		cout<<"Case #"<<count<<": ";
		long long N;
		cin>>N;
		if(N==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		long long inc=N;
		bool ar[10];
		for(int i=0;i<10;i++) ar[i]=false;
		while(true){
			string nstring = itos(N);
			bool done;

			for(int i=0;i<nstring.size();i++){
				done=true;
				for(int j=0;j<10;j++){
					if(j==(nstring[i]-48)) ar[j]=true;
					if(ar[j]==false){
						done=false;
					}
				}
				if(done) break;
				
			}
			if(done){
				cout<<N<<endl;
				break;
			}
			N+=inc;
		}
		
	}
	
    return 0;

}

