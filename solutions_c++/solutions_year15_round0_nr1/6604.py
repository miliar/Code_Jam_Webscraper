#include <iostream>
using namespace std;

int main() {
	
	int t, n, sum, r, tt;
	cin>>t;
	tt=t;
	while(t--){
	    sum=r=0;
	    cin>>n;
	    char in[n+1];
	    cin>>in;
	    for(int j=0;j<=n;++j){
	        
	        if(sum>=j){
	            sum+=in[j]-'0';
	        }else{
	        	++r;
	        	++sum;
	        	sum+=in[j]-'0';
	        }
	        
	    }
	    cout<<"Case #"<<tt-t<<": "<<r<<endl;
	    
	}
	
	return 0;
}