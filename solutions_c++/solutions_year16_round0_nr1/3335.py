#include <iostream>
using namespace std;
 
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, j, flag, n, tempo, c, num;
	bool a[10];
	cin>>t;
    for(int i=1;i<=t;i++){
    	
        for(int i=0;i<10;i++)
            a[i]=false;
	    
	    cin>>n;
	    flag=0;
	    if(n==0){
	        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
	        continue; 
	    }
	    
	    tempo=n;
	    
	    for(j=2;flag!=1;j++){
	    	
	    	c=0;
			
			while(tempo>0){
            	num=tempo%10;
	            a[num]=true;
	            tempo=tempo/10;
	        }
	        
	        for(int k=0;k<10;k++){
	        	if(a[k]==false)
                	break;
                else
                    c++; 
            }
           	
           	if(c==10)
    	        flag=1;
	        
	        tempo=j*n;
	    }
	    
	    cout<<"Case #"<<i<<": "<<(j-2)*n<<"\n";
	}
	return 0;
}
