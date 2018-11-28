/*
*	By manrajsingh
*	Do not copy -_-
*	Question: Google CodeJam 
*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define test
#define gc getchar_unlocked
#define pc(x) putchar_unlocked(x)
#define debug(x){cout<<#x<<" = "<<x<< endl;}
//int read_i(){char c=gc();while(c<'0' || c>'9'){c = gc();}int ret = 0;while(c>='0' && c<='9'){ret=10*ret+c-48;c=gc();}return ret;}

int main(){
	#ifdef test
	freopen("input_2.txt","r",stdin);
	freopen("output_2.txt","w",stdout);
	#endif
	ll t;
	scanf("%lld",&t);
	for(ll k=1;k<=t;k++){
		ll smax;
		string s;
		scanf("%lld",&smax);
		cin>>s;
		ll len=s.length(),total=s[0]-'0',more=0;
		for(ll i=1;i<len;i++){
			if(total<i){
				more+=(i-total);
				total+=(i-total);
			}
			total+=s[i]-'0';
		}
		printf("Case #%lld: %lld\n",k,more);
	}
	return 0;
}

