#include <iostream>
#include <cmath>
#include <stdint.h>
using namespace std;

int64_t prime(int64_t x){
	long double k;
	long double lim = sqrt(x);
	long double div=2;
	while(div<=lim){
		k = x/div;

		if(floor(k) == k){
			break;
		}
		div++;
	}
	if(div>lim)
		return -1;
	return div;
}

int main() {
	//get number of cases
    int cases;
    cin>>cases;
    
    int n;
    int j;
    int count;
    
    //array to hold the values
    int64_t vals[9];
    int64_t div[9];
    int64_t temp;
    bool comp;

    for(int z = 0; z< cases; z++){
    	cin>>n>>j;
    	count=0;
    	bool num[n];
    	cout<<"Case #"<< z+1<<": ";
    	for(int i = 0; i < n; i++){
    		num[i]=false;
    	}
    	num[0] = true;
    	num[n-1]= true;
    	while(count<j){
			//calculate the values
			comp=true;
			for(int i=0;i<9;i++){
				vals[i]=0;
			}
			for(int i=0; i< n; i++){
				//check if we need to add to the values
				if(num[i]){
					for(int k=0; k<9; k++)
						vals[k] += pow(k+2,i); 
				}
			}
		//	cout<<endl<<vals[8]<<endl;
			for(int i =0; i<9; i++){
			//	cout<<vals[i]<<endl;
				temp=prime(vals[i]);
			//	cout<<temp<<endl;
				if(temp!=-1)
					div[i]=temp;
				else{ 
					comp=false;
					break;
				}
			}
			

			if(comp){
				cout<<endl;
				for(int i=n-1; i>=0; i--){
					cout<<num[i];
				}
				for(int i=0;i<9;i++){
					cout<<" "<<div[i];
				}
				count++;
			}
			//update value
			for(int i=1; i<(n-2);i++){
				if(num[i])
					num[i] = false;
				else{
					num[i]=true;
					break;
				}
			}
    	}   	
    }
    //cout<<x<<endl<<y;
    return 0;
}
