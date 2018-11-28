#include <iostream>
using namespace std;

int main() {
		int f, p, t, max;
	cin>>t;
	for(int i=0;i<t;++i){
	    f=0;p=0;
	    char s[1000];
	    cin>>max;
	    cin>>s;
	    
	    for(int k=0;k<=max;++k){
	        
	        if(p>=k)
	            p+=s[k]-'0';
	        else{
	            
	            ++f;
	            ++p;
	            p+=s[k]-'0';
	            
	        }
	    }
	    
	    cout<<"Case #"<<i+1<<": "<<f<<endl;
	    
	}


	return 0;
}