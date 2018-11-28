#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cassert>
#include<vector>
#include<string>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<bitset>
#include<cstdio>
#include<cmath>
#include<climits>
#include<ctime>
#include<string>
#include<fstream>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#define ip(x) scanf("%d",&x)
#define ipLL(x) scanf("%lld",&x)
#define ForInc(var,beg,end) for(int var=beg;var<=end;++var)
#define advForInc(var,beg,end,inc) for(int var=beg;var<=end;var+=inc)
#define ForDec(var,end,beg) for(int var=end;var>=beg;--var)
#define ipArray(arr,size) ForInc(i,0,size-1) ip(arr[i]);
#define print(x) printf("%d\n",x)
#define printLL(x) printf("%lld\n",x)
#define ss(str) scanf("%s",str)
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#include<ctime>
template<typename T> T gcd(T a, T b) { return (b == 0) ? abs(a) : gcd(b, a % b); }
template<typename T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> inline T mod(T a, T b) { return (a % b + b) % b; }
template<typename T> inline T sqr(T x) { return x * x; }
typedef long long LL;
using namespace std;
/* Main Code starts here :) */

int arr[110][110];
int n,m;
int C[110];
void initializeCmatrix(){
	ForInc(j,1,m)C[j]=-1;
}
bool solve(){
	initializeCmatrix();
	bool allEqual;
	int mx=arr[1][1];ForInc(j,2,m)if(arr[1][j]>mx){mx=arr[1][j];}
	ForInc(j,1,m){
		if(arr[1][j]<mx){
			C[j]=arr[1][j];
			ForInc(i,1,n)if(arr[i][j]>C[j]){return false;}
		}
	}
	ForInc(i,2,n){
		allEqual=true;int mx=arr[i][1];
		ForInc(j,2,m)
			if(arr[i][j]>mx){mx=arr[i][j];allEqual=false;}
			else if(arr[i][j]<mx)allEqual=false;
		if(allEqual==true){continue;}
		ForInc(j,1,m){
			if(arr[i][j]<mx){
				if(C[j]!=-1){
					if(arr[i][j]>C[j])return false;
				}
				else{
					C[j]=arr[i][j];
					ForInc(ti,1,n){
						if(arr[ti][j]>C[j])return false;
					}
				}
			}
		}
		
	}
	return true;
}
int main(){
	int t;ip(t);
	ForInc(cs,1,t){
		ip(n);ip(m);
		ForInc(i,1,n)ForInc(j,1,m)ip(arr[i][j]);
		printf("Case #%d: ",cs);
		if(solve()==true)printf("YES\n");
		else printf("NO\n");
	}
return 0;	
}
