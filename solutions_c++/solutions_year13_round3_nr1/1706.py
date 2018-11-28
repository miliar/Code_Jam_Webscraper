#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
using namespace std;
typedef long long LL;
#define VI vector<int>
#define VII vector<vector<int> > 
#define SIZE(A) ((int)A.size())
#define LEN(A) ((int)A.length())
#define MS(A) memset(A,0,sizeof(A))
#define MSV(A,a) memset(A,a,sizeof(A))
#define PII pair<int,int>
#define MP make_pair
#define F first
#define S second
#define PB push_back
#define FOUND(A,x) (A.find(x)!=A.end())
#define getcx getchar_unlocked

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, a, n) for(int i = a; i < n; i++)
#define REV(i, a, n) for(int i = a; i > n; i--)

#define FORALL(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++);

#define MAX 500
#define MOD 1000000007
inline void inp( int &n )
{
        n=0;
        int ch=getcx();int sign=1;
        while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

        while(  ch >= '0' && ch <= '9' )
                n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
		n=n*sign;
}
char a[MAX];
int b[MAX];
int c[MAX];
int main(){
int t,o=0;
cin>>t;
while(o++<t){
	printf("Case #%d: ",o);
	cin>>a;
	cin.ignore();
	int n;cin>>n;
	REP(i,n+1)b[i]=0;
	int p = strlen(a);
	REP(i,p){
		if(a[i]=='a' || a[i]=='e' || a[i]=='i' || a[i]=='o' || a[i]=='u')
			b[i]=0;
		else b[i]=b[i-1]+1;
	}
int l=0,count=0;
	REP(i,p)FOR(j,i,p){
		FOR(k,i+n-1,j+1){
			if(b[k]>=n){
				count++;
				break;}
		}
		}
cout<<count<<endl;
}
return 0;
}
