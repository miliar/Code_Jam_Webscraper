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
string itos(int n){
stringstream ss;
ss<<n;
return ss.str();
}
int cal(int l){
	return floor(l/2)*2;
}
int main(){
	int T;
	cin>>T;
	for(int count=1;count<=T;count++){

		string data;
		cin>>data;
		cout<<"Case #"<<count<<": ";
		if(data.size()==1){
			if(data[0]=='+') cout<<"0"<<endl;
			if(data[0]=='-') cout<<"1"<<endl;
			continue;
		}
		int length=1;
		for(int i=1;i<data.size();i++){
			if(data[i]!=data[i-1]) length++;
		}
		if(data[0]=='+') cout<<cal(length)<<endl;
		if(data[0]=='-') cout<<cal(length-1)+1<<endl;
	}
    return 0;

}

