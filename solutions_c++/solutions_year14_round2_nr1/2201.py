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

int main(int argc, char **argv){
		
	#ifndef GCJ		
		freopen("a1.txt","w",stdout);
		//freopen("a2.txt","w",stdout);
	#endif
	
	ios_base::sync_with_stdio(false);
	
	int T;
	int N;
	vector<string> v;
	vector< pair<char,int> > vp[2];
	string s;	
	cin>>T;
	FOR(k,0,T){		
		cin>>N;
		FOR(i,0,N){
			cin>>s;
			v.pb(s);			
		}
		FOR(z,0,2){
			int len = (v.at(z)).length();
			char st = (v.at(z)).at(0);
			int cnt=1;		
			FOR(i,1,len){
				if(st==(v.at(z)).at(i)){
					cnt++;
				}else{
						vp[z].pb(mp(st,cnt));
						st = v[z].at(i);
						cnt=1;
				}
			}
			vp[z].pb(mp(st,cnt));
		}		
		
		int cost=0;
		int bad=0;
		if(vp[0].size()==vp[1].size()){
			FOR(i,0,vp[0].size()){
				if((vp[0].at(i)).first==(vp[1].at(i)).first)
					cost+=abs((vp[0].at(i)).second-(vp[1].at(i)).second);				
				else{
					printf("Case #%d: Fegla Won\n", k+1);
					bad=1;
					break;
				}					
			}
			if(!bad)printf("Case #%d: %d\n", k+1,cost);
		}else printf("Case #%d: Fegla Won\n", k+1);
		
		FOR(i,0,2)vp[i].clear();
		v.clear();
	}
	





		
	return 0;
}

//printf("Case #%d: No\n", i+1);