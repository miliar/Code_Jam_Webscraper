#pragma comment(linker, "/STACK:1024000000,1024000000")  
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;
template<class T> T gcd(T x,T y){while(T t=x%y)x=y,y=t;return y;}
const double eps = 1e-9;
const double PI = acos(-1.);
const int INF = 1000000000;
const int MOD = 1000000007;
const double E = 2.7182818284590452353602874713527;

#define pmul(x1,y1,x2,y2) ((x1)*(x2)+(y1)*(y2))
#define xmul(x1,y1,x2,y2) ((x1)*(y2)-(x2)*(y1))
#define sqr(x) ((x)*(x))

#define FR(i,N) for(int i=0;i<N;i++)
#define FRS(i,S,E) for(int i=S;i<=E;i++)
#define FRD(i,S,E) for(int i=S;i>=E;i--)
#define SZ(x) ((int)(x).size())
#define fill(a,b) memset(a,b,sizeof(a))
#define PII pair<int,int>
#define MP(a,b) make_pair(a,b)
#define fi first
#define se second
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define lowbit(x) ((x)&(-(x)))

bool isdig(char x){return x>='0'&&x<='9';}
bool isup(char x){return x>='A'&&x<='Z';}
bool isdown(char x){return x>='a'&&x<='z';}
bool islet(char x){return isup(x)||isdown(x);}

//--------CODE----------
int N, M;
string str[1005];
void get_data(){
	cin>>N>>M;
	FR(i, N)cin>>str[i];
}
vector<int> tot[105];
int maxA, maxN;

struct Node{
	int next[26];
};
Node nd[10000];
int ndn;
void InitNd(int x){
	fill(nd[x].next, -1);
}
int CalNum(vector<int>& vec){
	ndn = 0;
	InitNd(ndn++);
	int n = vec.size();
	FR(i, n){
		int now = 0;
		int ind = vec[i];
		string& s = str[ind];
		int l = s.size();
		FR(j, l){
			if(nd[now].next[s[j] - 'A'] == -1){
				nd[now].next[s[j] - 'A'] = ndn;
				InitNd(ndn++);
			}
			now = nd[now].next[s[j] - 'A'];
		}
	}
/*	
	FR(i, vec.size()){
		cout<<str[vec[i]]<<' ';
	}
	cout<<ndn<<endl;
	*/
	return ndn;
}
void Cal(){
	int r = 0;
	FR(i, M){
		r += CalNum(tot[i]);
	//	cout<<r<<endl;
	}
	if(r > maxA){
		maxA = r;
		maxN = 0;
	}
	if(r == maxA)maxN++;
}
void Put(int ind, int fl){
	if(ind == N){
		if(fl != M)return;
		Cal();
		return;
	}
	if(M - fl > N - ind)return;
	FR(i, M){
		tot[i].PB(ind);
		Put(ind + 1, fl + (tot[i].size() == 1));
		tot[i].pop_back();
	}
}
void run(){
	FR(i, M)tot[i].clear();
	tot[0].PB(0);
	maxA = 0; maxN = 1;
	Put(1, 1);
	cout<<maxA<<' '<<maxN * M<<endl;
}
int main(){
//	get_prime();
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int t, i = 0;
	cin>>t;
	while(t--)
	{
	get_data();
	printf("Case #%d: ", ++i);
	run();
	}
	return 0;
}
