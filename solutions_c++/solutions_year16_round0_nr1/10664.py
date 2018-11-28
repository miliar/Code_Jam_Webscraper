#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
	    int n,rem;
	    cin>>n;
	    set<int> a;
	    long long temp,temp1,count=0;
	  	    while(a.size()!=10 & count<100){
	        count++;
	        temp=count*n;
	        temp1=temp;
	        while(temp>0){
	             rem=temp%10;
	            a.insert(rem);
	           temp=temp/10;
	        }
            	        
	        
	        
	    }
	    if(a.size()!=10)cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
	    else cout<<"Case #"<<i<<": "<<temp1<<endl;
	}
	return 0;
}
