#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ull unsigned long long
#define si(X) scanf("%d", &(X))
#define sll(X) scanf("%lld",&(X))
ll gcd(ll a,ll b){
	if(b==0)
	return a;
	return gcd(b,a%b);
}
const int mod = 1e9+7;
ll expo(ll base,ll pow){
    ll ans = 1;
    
    while(pow!=0){
        if(pow&1==1){
            ans = ans*base;
            ans = ans%mod;
        }
        base *= base;
        base%=mod;
        pow/=2;
        
    }
    return ans;
}
double pi = 3.141592653589793238462643;
double error = 0.0000001;
/* -------Template ends here-------- */ 

const int M = 100001;
set<int> se;

void fin(ull num){
	while(num>0){
		se.insert(num%10);
		num = num/10;
	}
}



int main(){
	
	int t;
	si(t);
	
	for(int alp = 1;alp<=t;alp++){
		ll ans = 0;
		se.clear();
		ull n;
		
		cin>>n;
		ll mul = 1;
		if(n==0){
			ans = 0;
		}
		else{
		
		while(true){
			if(se.size()==10)
			break;
			
			fin(n*mul);
			//cout<<n*mul<<"     "<<se.size()<<endl;
			ans = n*mul;
			mul++;
		}
	}
		
		
		
		
		
		
		
		
		if(ans!=0)
		cout<<"Case #"<<alp<<": "<<ans<<endl;
			else{
				cout<<"Case #"<<alp<<": "<<"INSOMNIA"<<endl;
			}
	}
	
	
	
	
	
	
	
	
	

	
}
























