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
	freopen("input_3.txt","r",stdin);
	freopen("output_3.txt","w",stdout);
	#endif
	ll t;
	scanf("%lld",&t);
	for(ll k=1;k<=t;k++){
		ll x,r,c;
		scanf("%lld%lld%lld",&x,&r,&c);
		string R="RICHARD", G="GABRIEL",ans;
		if(x==1){
			ans=G;
		}
		else if(x==2){
			if(r==1){
				if(c==1||c==3){
					ans=R;
				}
				else{
					ans=G;
				}
			}
			else if(r==2){
				ans=G;
			}
			else if(r==3){
				if(c==1||c==3){
					ans=R;
				}
				else{
					ans=G;
				}
			}
			else if(r==4){
				ans=G;
			}
		}
		else if(x==3){
			if(r==1){
				ans=R;
			}
			else if(r==2){
				if(c==3){
					ans=G;
				}
				else{
					ans=R;
				}
			}
			else if(r==3){
				if(c==1){
					ans=R;
				}
				else{
					ans=G;
				}
			}
			else if(r==4){
				if(c==3){
					ans=G;
				}
				else{
					ans=R;
				}
			}
		}
		else if(x==4){
			if(r==1||r==2){
				ans=R;
			}
			else if(r==3){
				if(c==1||c==2||c==3){
					ans=R;
				}
				else{
					ans=G;
				}
			}
			else if(r==4){
				if(c==1||c==2){
					ans=R;
				}
				else{
					ans=G;
				}
			}
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
