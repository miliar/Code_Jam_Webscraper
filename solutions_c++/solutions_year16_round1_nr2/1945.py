/*ckpeteryu*/
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<typeinfo>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
//#include<regex>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long int

int nt;
int a[2505];

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();	
	scanf("%d",&nt);
	FOE(k,1,nt){
		int nc,t;
		scanf("%d",&nc);
		CLR(a,0);
		int bound=2*nc-1;		
		FOR(i,0,bound){
			FOR(j,0,nc){
				scanf("%d",&t);				
				a[t]++;
			}
		}
		int x=0;
		vector<int> v;
		while(nc>0){
			if(a[x]%2==1){
				v.pb(x);
				nc--;
				
			}
			x++;
		}
				
		printf("Case #%d: %d",k,v[0]);
		int sz=v.size();
		FOR(j,1,sz){
			printf(" %d",v[j]);
		}
		puts("");
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}