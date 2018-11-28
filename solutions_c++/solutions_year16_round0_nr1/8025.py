#include <iostream>
using namespace std;

int main() {
	bool digits[10] = {false};
	long long x;
	long long xx;
	long t;
	int inc;
	cin>>t;
	
	for(int i=1;i<=t;i++){
	    cin>> x;
	    inc = 1;
	    if(x != 0)
	    {
    	    while(1){
    	        xx = x*inc;
    	        
    	        while(xx != 0){
    	            int d = xx%10;
    	            digits[d] = true;
    	            xx = xx/10;
    	        }
    	        bool isDone = true;
    	        for(int k=0;k<10;k++){
    	            if(digits[k] == false){
    	                isDone = false;
    	                break;
    	            }
    	        }
    	        if(isDone){
    	            break;
    	        }
    	        
    	        inc++;
    	    }
    	    for(int k=0;k<10;k++){
    	       digits[k] = false;
    	     }
    	    cout <<"Case #"<<i<<": "<<x*inc<<endl;
	    }else{
	        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
	    }
    	    
	    
	    
	}
	return 0;
}
