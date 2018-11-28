#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cassert>

#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <numeric>
#include <bitset>

#include <cstdio>
#include <cstring>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define fch(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define sz(x) (int((x).size()))
#define pb push_back
#define mkp make_pair
#define all(X) (X).begin(),(X).end()

#define X first
#define Y second

template<class T> inline void smin(T &a, T b){if(b<a)a=b;}
template<class T> inline void smax(T &a, T b){if(a<b)a=b;}

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;


typedef vector<char> VC;
typedef vector<string> VS;
typedef vector<ll> VL;
typedef vector<double> VD;
typedef set<int> SI;
typedef set<string> SS;
typedef map<int, int> MII;
typedef map<string, int> MSI;

template<class T> inline void RST(T &A){memset(A, 0, sizeof(A));}
template<class T> inline void FLC(T &A, int x){memset(A, x, sizeof(A));}
template<class T> inline void CLR(T &A){A.clear();}

/** Constant List .. **/ //{
const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};
const int dx8[] = {-1, 0, 1, 0 , -1 , -1 , 1 , 1};
const int dy8[] = {0, 1, 0, -1 , -1 , 1 , -1 , 1};
const int mod = 1000000007;
//}

template<class T> inline T min(T a, T b, T c){return min(min(a, b), c);}
template<class T> inline T max(T a, T b, T c){return max(max(a, b), c);}
template<class T> inline T min(T a, T b, T c, T d){return min(min(a, b), min(c, d));}
template<class T> inline T max(T a, T b, T c, T d){return max(max(a, b), max(c, d));}
template<class T> inline T sqr(T a){return a*a;}
template<class T> inline T cub(T a){return a*a*a;}

////////////////////////////////////////////////////////////////////////////////
int T,t,n;
char s[109],b[109];
int a[109][109];
/*
int convert(char s1[],char s2[]){
	int l1 = strlen(s1), l2=strlen(s2),i=0,j=0,ret=0;
	while(i<l1 && j<l2){
		if(s1[i]==s2[j]) { i++,j++; continue; }
		else{
			if(j==0) return -1;
			if(s2[j]==s1[i-1]) {	ret++,j++; continue; }
			else return -1;
		}
	}
	printf(" ## ");
	if(i==l1 && j==l2) return ret;
	else if(i<l1){
		while(i<l1){
			if(s1[i]==s2[j-1]) ret++,i++;
			else return -1;
		}
	}else{
		while(j<l2){
			if(s1[i-1]==s2[j]) ret++,j++;
			else return -1;
		}
	}
	return ret;
}

int f(int k){
	int ret = 0;
	rep(i,n){
		int tmp = convert(s[i],s[k]);
		if(tmp<0) return -1;
		else ret+=tmp;
	}

	return ret;
}

int work(){
	int ret = mod;
	rep(i,n){
		int tmp = f(i);
		if(tmp>=0) smin(ret,tmp); printf("%d ", tmp);
	}
	return ret;
}
int main()
{
	freopen("in.txt","r",stdin);
	ios_base::sync_with_stdio(0);
	scanf("%d",&T);
	fer(t,1,T+1){
		printf("Case #%d: ", t);
		scanf("%d",&n);
		rep(i,n) scanf("%s",s[i]);
		int tmp = work();
		if(tmp!=mod) printf("%d\n", tmp);
		else puts("Fegla Won");
	}
	return 0;
}*/
int shrink(char s1[],char s2[]){
	int l = strlen(s1),j=0;
	char c='-';
	rep(i,l){
		if(s1[i]!=c) s2[j++] = c = s1[i];
	}
	s2[j]=0;
	return j;
}

void f(char s[],int h,int l){
	char c = '-';
	int j=0,tmp=0;
	rep(i,strlen(s)+1){
		if(s[i]!=c){
			if(tmp!=0) a[j++][h]=tmp;
			c=s[i]; tmp=1;
		}else tmp++;
	}
}
bool ok(char s1[],char s2[]){
	int l1=strlen(s1),l2 = strlen(s2),j=0;
	rep(i,l2){
		if(s1[j]!=s2[i]) return false;
		while(j<l1 && s1[j]==s2[i]) j++;
	}
	return j==l1;
}

int work(){
	scanf("%s",b);
	int l = shrink(b,s);
	//printf("s: %s ",s );
	f(b,0,l); 
	fer(i,1,n) {
		scanf("%s",b);
		if(!ok(b,s)) return -1;
		f(b,i,l);
	}
	int k = n/2,ret=0;
	rep(i,l){
		sort(a[i],a[i]+n);
		rep(j,n) ret += abs(a[i][j]-a[i][k]);
	}
	return ret;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("a.txt","w",stdout);
	ios_base::sync_with_stdio(0);
	scanf("%d",&T);
	fer(t,1,T+1){
		printf("Case #%d: ", t);
		scanf("%d",&n);
		int tmp = work();
		if(tmp>=0) printf("%d\n", tmp);
		else puts("Fegla Won");
	}
	return 0;
}