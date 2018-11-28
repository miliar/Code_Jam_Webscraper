#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ll;

//isPrime yes 1 no 0
bool isPrime(ll n){
	
	if(n < 2) return false;
	if(n == 2) return true;
	if(n % 2 == 0) return false;
	for(ll i=3; (i*i)<=n; i++){
		if(n%i==0) return false;				
	}
	return true;
}

ll divisor(ll n){
	for(ll i=2; (i*i)<=n; i++){
		if(n%i==0 && n != i)  return i; 
		}	          
	}


int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d:\n", qq);
    
    int N,J;
    scanf("%d %d", &N, &J);
    //int ans = 0;
    int base[] = {2,3,4,5,6,7,8,9,10};
    int M;
  	M = N - 2;
  	vector<bool> anslist (9);
  	vector<int> divlist(9);
    for (ll k = 0; k < ceil(pow(2,M)); k++){          
    						  
        for(int i =0; i < sizeof(base)/sizeof(*base) ; i++){
    	  
    	  	ll ans = ceil(pow(base[i],N-1));
    	
    			int v = k;
    			//cout << " value of k : " << k << endl;
    			int cnt = 0;
    			while(v != 0){
    				cnt++;
    				int d = v/2;
    		 		int r = v - d*2;
    		 		if(r != 0){
    		 			ans = ans + ceil(pow(base[i],cnt));
         	  }          
         		v = d;
    			}
    			//int f = m + r;
    			//cout << f << endl;
    		
    			ans = ans + 1;

    			//cout << ans << endl;
    			anslist[i] = isPrime(ans);
    			//cout << anslist[i] << endl;
    			divlist[i] = divisor(ans);

    			//if(i == 8) cout << ans << endl;
    			bool allTrue = true;
    			
			    for( int j=0 ; j < sizeof(base)/sizeof(*base) ; j++){
        		if(anslist[j])
        			allTrue = false;
        	}
        	
        	if(allTrue && i == 8 &&  J > 0){
        	  	cout << ans << " ";
        	  	for(int x= 0; x < sizeof(base)/sizeof(*base) ; x++){
        	  	printf("%lu ", divlist[x]);
        	  	}
        	  	cout << endl;
        	  	J--;
        	}
        	if (J <= 0) break;
                               
					//cout << base[i] << ", isPrime :" << isPrime(ans) << " non-trivial divisor : "  << endl; 
				}
		     	   		  
     }
                                   	  
  	  
  	
  }
  return 0;
}
