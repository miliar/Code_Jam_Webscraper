#include <iostream>
using namespace std;

int main() {
	int i, j, k, l, n, p, s[26], max, count;
	char chr;
	cin>>n;
	for(i=0; i<n; i++){
	    cin>>p;
	    count = 0;
	    for(j=0; j<p; j++){
	        cin>>s[j];
	        count += s[j];
	    }
	    cout<<"Case #"<<i+1<< " ";
	    max = 0;
	    while(count>0){
	        for(l=0;l<2;l++){
	            for(j=0; j<p; j++){
	                if(s[max]<s[j]){
	                    max = j;
	                }
	            }
	            chr = 64+max+1;
	            s[max]--; 
	            if(count>0)
	                cout<<chr;
	            count--;
	            if(count == 2) {
	                l++;
	            }
	        }
	        cout<<" ";
	    }
	    cout<<"\n";
	    
	}
	return 0;
}