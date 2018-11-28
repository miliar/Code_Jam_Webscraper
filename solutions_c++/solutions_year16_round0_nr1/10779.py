#include <bits/stdc++.h>
using namespace std ;
#define LL long long
int main(void){
    freopen("A-large.in","r",stdin) ;
    freopen("A-small-attempt_large","w",stdout) ;
	LL n ,TC,i,CT=1;
	LL val ;
	map<int,int>mp ;
	cin>>TC ;
	//TC=1 ;
	while(TC--){
		mp.clear() ;
		cin>>val;

		//val=TC ;
		i=1 ;
		while(mp.size()<10 && val!=0){
			LL t = val*i ;
			//cout<<val<<endl ;
			while(t>0){
                //cout<<t%10<<endl;
				mp[t%10]=1 ;
				t/=10 ;
			}
			i++ ;
			//val*=i ;
		}
		cout<<"Case #"<<CT++<<": " ;
		if(val==0){
            cout<<"INSOMNIA\n" ;
		}
		else cout<<val*(i-1)<<endl ;
	}

	return 0 ;
}
