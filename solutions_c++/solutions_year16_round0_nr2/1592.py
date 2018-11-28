#include <bits/stdc++.h>

using namespace std;
#define ll long long
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
int arr[110];
int temp[110];

int fin_two(int len){
	int index = -1;
	for(int i = len-1; i>=0; i--){
		if(arr[i]==0){
			index = i;
			break;
		}
	}
	return index;
}

int rev(int x){
	if(x==1)
	return 0;
	return 1;
}

int fin_one(int len){
	int index = -1;
	
	for(int i = 1;i<len;i++){
		if(arr[i]==0){
			index = i;
			break;
		}
	}
	return index;
	
}

int main(){
	
	int t;
	si(t);
	
	for(int alp = 1;alp<=t;alp++){
		int ans = 0;
		
		string s;
		cin>>s;
		
		int len = s.length();
		
		memset(arr,0,sizeof(arr));
		for(int i = 0;i<len;i++){
			if(s[i]=='+'){
				arr[i] = 1;
			}
			else{
				arr[i] = 0;
			}
		}
		
		
		while(true){
			for(int i = 0;i<len;i++){
				//cout<<arr[i]<<" ";
				temp[i] = arr[i];
			}
			//cout<<endl;
			
			int pos;
			
			if(arr[0]==1){
				
				pos = fin_one(len);
				
				if(pos==-1){
					break;
				}
				pos = pos-1;
				for(int i = 0;i<=pos;i++){
					temp[i] = rev(arr[pos-i]);
				}
				
				for(int i = 0;i<len;i++){
					arr[i] = temp[i];
				}
					
			}
			else{
				pos = fin_two(len);
				
				for(int i = 0;i<=pos;i++){
					temp[i] = rev(arr[pos-i]);
				}
				
				for(int i = 0;i<len;i++){
					arr[i] = temp[i];
				}
				
			}
			
			ans++;
			
		}
		
		cout<<"Case #"<<alp<<": "<<ans<<endl;
			
	}
	
	
	
	
	
	
	
	
	

	
}

























