// Vishal Gupta IIIT-H

#include <bits/stdc++.h>
using namespace std;

#define sz(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traversing a container..works for any type of container
#define present(container, element) (container.find(element) != container.end())    //used for set...return 1 if el is ps 0 otherwise
#define cpresent(container, element) (find(all(container),element) != container.end())  //same as present...but is for vectors
#define INF		INT_MAX
#define FOR(i,a,b) 	for(int  i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define FORD(i,a,b) for( i = (a); i>= (int) b; i--)
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d ",n)
#define pil(n) printf("%d\n",n)
#define piL(n) printf("%lld ",n)
#define piLL(n) printf("%lld\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define PB push_back
#define MP make_pair
#define scan(v,n)	vector<int> v;rep(i,n){ int j;si(j);v.PB(j);}
#define fill(a,b) memset(a,b,sizeof(a))
#define mod (int)(1e9 + 7)
#define pn printf("\n")
#define F first
#define S second
typedef long long int LL;
typedef vector <int> VI;
typedef pair < int ,int > PII;
typedef vector < PII > VPII;
template<class T>inline T gcd(T a,T b){return b?gcd(b,a%b):a;}
template<class T> inline T LCM(T a,T b){if(a<0)return LCM(-a,b);if(b<0)return LCM(a,-b);return a*(b/gcd(a,b));}
int a[5][5],b[5][5];
int main()
{
       int testit,test,row;
       si(test);
       rep(testit,test){
       	 si(row);
       	 set <int > s,t;
       	 	rep(i,4) rep(j,4){
       	 		si(a[i][j]);
       	 		if(i==row-1) s.insert(a[i][j]);	
       	 	}
      		si(row);
      		rep(i,4) rep(j,4){
      			 si(b[i][j]);
      			 if(i==row-1 && present(s,b[i][j])) t.insert(b[i][j]);
      		} 
       		if(sz(t)==1) printf("Case #%d: %d\n",testit+1,*(t.begin()));
       		else if(sz(t)>1)  printf("Case #%d: Bad magician!\n",testit+1);
       		else  printf("Case #%d: Volunteer cheated!\n",testit+1);
       }
       return 0;
}

