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
		//freopen("d1.txt","w",stdout);
		freopen("d2.txt","w",stdout);
	#endif
	
	//ios_base::sync_with_stdio(false);
	
	int T,n;	
	double t;
	vector<double> v1;
	vector<double> v2;	
	scanf("%d",&T);
	FOR(k,0,T){
		scanf("%d",&n);		
		FOR(i,0,n){
			scanf("%lf",&t);
			v1.pb(t);			
		}		
		FOR(i,0,n){
			scanf("%lf",&t);
			v2.pb(t);
		}
		
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		
		vector<double> v3(v1.begin(),v1.end());
		vector<double> v4(v2.begin(),v2.end());			
		int ans1=0,ans2=0;
		
		FOR(i,0,n){			
			if(v1.front()<v2.front()){				
				v1.erase(v1.begin(),v1.begin()+1);
				v2.pop_back();				
			}else{				
				v1.erase(v1.begin(),v1.begin()+1);
				v2.erase(v2.begin(),v2.begin()+1);
				ans1++;
			}		
		}
		
		vector<double>::iterator it;
		//FOR(i,0,n){
		FOD(i,n,1){
			if(v3.front()<v4.back()){
					it = upper_bound(v4.begin(),v4.end(),v3.front());
					v4.erase(it,it+1);
					v3.erase(v3.begin(),v3.begin()+1);
			}else{
					//ans2 = v3.size();
					ans2 = i;
					break;
			}
		}
		
		printf("Case #%d: %d %d\n", k+1,ans1,ans2);			
		
		v1.clear();
		v2.clear();
		v3.clear();
		v4.clear();
	}		
	return 0;
}

//printf("Case #%d: No\n", i+1);