#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<cassert>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

int64 first(int N,int64 x){
	assert(0<=x&&x<(1LL<<N));
	if(N==1)return x;
	if(x+1<(1LL<<N)){
		return first(N-1,(x+1)/2);
	}else{
		return x;
	}
}

int64 last(int N,int64 x){
	assert(0<=x&&x<(1LL<<N));
	if(N==1)return x;
	if(x){
		return (1LL<<N-1)+last(N-1,(x-1)/2);
	}else{
		return x;
	}
}

void solve(){
	int N;
	int64 P;
	cin>>N>>P;
	int64 could=0;
	assert(first(N,could)<P);
	for(int i=N-1;i>=0;i--)if(first(N,could+(1LL<<i))<P)could+=1LL<<i;
	//while(could+1<(1LL<<N)&&first(N,could+1)<P)++could;
	assert(first(N,could)<P);
	if(could+1<(1LL<<N))assert(first(N,could+1)>=P);
	int64 must=(1LL<<N);
	for(int i=N-1;i>=0;i--)if(last(N,must-(1LL<<i))>=P)must-=1LL<<i;
	//while(must>=0&&last(N,must-1)>=P)--must;
	assert(last(N,must-1)<P);
	if(must<(1LL<<N))assert(last(N,must)>=P);
	assert(must);
	cout<<must-1<<" "<<could<<endl;
}

int main(){
//cout<<last(3,2)<<endl;
//return 0;
  int C;cin>>C;
  for(int c=1;c<=C;c++){ 
    cout<<"Case #"<<c<<": ";
		solve();
  }
	return 0;
}
