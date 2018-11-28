#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long tc,t,arr[10] = {0},n,num,rem,inc,flag;
	cin >> tc;
	t = tc;
	while(tc--){
	    cin >> num;
	    inc = num;
	   
	    if(num > 0){
    	    while(1){
    	        flag = 0;
    	        n = num;
    	        while(n > 0){
    	            rem = n % 10;
    	            n = n / 10;
    	            arr[rem] = 1;
    	        }
    	        for(int i = 0 ; i < 10; i++){
    	            if(arr[i] != 1)
    	                flag = 1;
    	        }
    	        
    	        if(flag == 0){
    	            break;
    	        }
    	        num += inc;
    	    }
    	    cout <<"Case #"<<t-tc<<": "<<num<<endl;
	    }
	    else{
	        cout <<"Case #"<<t-tc<<": INSOMNIA"<<endl;
	    }
	    
	    for(int i = 0; i < 10 ; i ++)
	        arr[i] = 0;
	}
	return 0;
}
