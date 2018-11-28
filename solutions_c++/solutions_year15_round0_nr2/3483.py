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
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
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
#define L long int

int nt,D,t,numCuts,totCuts,rm,ret;
int cnt[1005];
vector<int> v;
vector<int>::iterator it;

bool comp(int i,int j){return i>j;}

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);	
	#ifndef GCJ		
		//freopen("b1.txt","w",stdout);
		//freopen("b2.txt","w",stdout);
		//freopen("b3.txt","w",stdout);
		freopen("b4.txt","w",stdout);
	#endif

	scanf("%d",&nt);	
	FOE(k,1,nt){
		//fill(cnt,cnt+1005,0);
		//totCuts=0;
		scanf("%d",&D);			
		FOR(i,0,D){
			scanf("%d",&t);
			//if(!cnt[t]){
				v.pb(t);
			//}
			//cnt[t]++;			
		}
		sort(v.begin(),v.end(),comp);		
		ret=v[0];
		int sz=v.size();
		FOR(rm,1,v[0]){
			totCuts=0;
			FOR(j,0,sz){
				if(v[j]<rm)break;				
				totCuts+=ceil(1.0*v[j]/rm)-1;
			}
			ret=min(ret,totCuts+rm);
		}
		/*while(1){
			numCuts=cnt[v[0]];			
			if(v[0]<=2 || v[0]<=numCuts){
				rm=v[0];
				ret=min(ret,totCuts+rm);
				break;
			}else{
				int a=v[0]/2;
				int b=v[0]/2+v[0]%2;
				cnt[v[0]]=0;
				v.erase(v.begin());
				if(!cnt[a]){
					it=lower_bound(v.begin(),v.end(),a,comp);
					v.insert(it,a);
				}
				cnt[a]+=numCuts;
				if(!cnt[b]){
					it=lower_bound(v.begin(),v.end(),b,comp);
					v.insert(it,b);
				}
				cnt[b]+=numCuts;				
				totCuts+=numCuts;				
				rm=v[0];
				ret=min(ret,totCuts+rm);
			}
		}*/
		printf("Case #%d: %d\n",k,ret);
		v.clear();
	}
	return 0;
}