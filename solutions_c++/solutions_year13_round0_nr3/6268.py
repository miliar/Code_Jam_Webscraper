#include<iostream>
#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstring>
#include<vector>
#define REP(i,m) for(int i=0;i<m;++i)
#define REPN(i,m,in) for(int i=in;i<m;++i)
#define ALL(t) (t).begin(),(t).end()
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
using namespace std;
static const int INF =500000000; 
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
typedef long long int lint;
typedef pair<int,int> pi;

lint all[100];
int m;
stringstream ss;
bool isPalin(lint a){
	ss.clear();ss.str("");
	ss<<a;
	string rev=ss.str();reverse(ALL(rev));
	return (rev==ss.str());
}
int main(){
	for(lint i=1;i<=10000005;++i) if(isPalin(i) && isPalin(i*i)) all[m++]=i*i;

	int t;
	scanf("%d",&t);
	for(int setn=1;setn<=t;++setn){
		printf("Case #%d: ",setn);
		int a,b;scanf("%d%d",&a,&b);++b;
		printf("%d\n",lower_bound(all,all+m,b)-lower_bound(all,all+m,a));
	}

	return 0;
}



