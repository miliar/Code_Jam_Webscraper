 #include <bits/stdc++.h>
 using namespace std;
 
 typedef long long ll;
 
 int main(){
 	ll t,n;cin>>t;
 	for(ll tc=1;tc<=t;tc++){
 		cin>>n;
 		if(n){
 			ll c=0,i=1;
 			vector<int> v(10,0);
 			while(c<10){
 				int m=n*i;
 				while(m!=0){
 					if(v[m%10]==0){
 						c++;
 						v[m%10]=1;
 					}
 					m/=10;
 				}
 				i++;
 			}
 			printf("Case #%lld: %lld\n",tc,(i-1)*n);
 		}else{
	 		printf("Case #%lld: INSOMNIA\n",tc);
 		}
 	}
 }
