#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<stack>
#include<vector>
using namespace std;

#define	gi(a)		scanf("%d",&a)
#define	Int(a)		int a;ri(a);
#define Pair		pair <int,int>
#define mp		make_pair
#define ll		long long
#define INF		2147483647
#define clr(a)		memset(a,0,sizeof(a))
#define dbg(x) 		cerr<<#x<<" ="<<(x)<<endl
#define max(a,b)	(a>b)?a:b
#define min(a,b)	(a<b)?a:b
#define min3(a,b,c)	(a<min(b,c))?a:min(b,c)
#define pb		push_back

template <class T>
inline void ri(T &i){
	bool minus=false;
	char c;
	for(c=getchar();(c<'0'||c>'9')&&(c!='-');
		      c=getchar());
	if(c=='-')
		      {minus=true;c='0';}
	for(i=0;c>='0'&&c<='9';c=getchar())
		      i=(i<<3)+(i<<1)+(c-48);
	if(minus)i=(~i)+1;
}
bool isPalin(int x){
	int r=x,s=0;
	while(r>0){
		s=s*10+(r%10);
		r=r/10;
	}
	return x==s;
}
int main(){
	int i,j,k;
	int m,n;
	vector<int> res;
	res.pb(-1);
	for(i=1;i<=33;i++){
		if(isPalin(i) && isPalin(i*i)){
			res.pb(i*i);
		}
	}
	Int(t);
	int C=1;
	while(t--){
		ri(m);ri(n);
		int ans=0;
		for(i=0;i<res.size();i++){
			if(res[i]>=m && res[i]<=n) ans++;
		}
		cout<<"Case #"<<C<<": "<<ans<<endl;
		C++;
	}
	return 0;
}
