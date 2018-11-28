/*ckpeteryu*/
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cfloat>
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
#define LL long long double
#define L long double

int main(int argc, char **argv){
		
	ios_base::sync_with_stdio(false);	
	
	#ifndef GCJ		
		//freopen("b1.txt","w",stdout);
		freopen("b2.txt","w",stdout);
	#endif
	
	int T;
	long double C,F,X;
	cin>>T;
	cout<<setprecision(7)<<fixed;
	FOR(k,0,T){		
		cin>>C>>F>>X;		
		if(X>C){
			long double denom=2,ans=0;
			int cnt=0;			
			for(;;){
				//cout<<((X-C)/denom)<<" "<<(X/(denom+F))<<endl;				
				//if(((X-C)/denom)>(X/(denom+F))){ denom+=F;} else break;
				//cout<<(X-C)*(denom+F)<<X*denom<<endl;
				if(((X-C)*(denom+F))>(X*denom)){denom+=F;} else break;
				cnt++;				
			}
			ans+=(X/denom);
			denom=2;
			FOR(i,0,cnt){				
				ans+=C/denom;
				denom+=F;
			}
			cout<<"Case #"<<(k+1)<<": "<<ans<<endl;
			//cout<<denom<<endl;
		}else{			
			cout<<"Case #"<<(k+1)<<": "<<(X/2)<<endl;
		}
		//cout<<C<<" "<<F<<" "<<X<<endl;
	}	  
   	
	return 0;
}

//printf("Case #%d: No\n", i+1);