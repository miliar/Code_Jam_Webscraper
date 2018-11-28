#include <iostream>
#define INT_MAX 1 << 20
using namespace std;
int c[11];

int main() {
	// your code goes here
	int t,i,j,p,f;
	long long n,k,temp;

	cin >> t;
	for(i=0;i<t;i++){
		cin >> n;
		if(n==0){
			cout << "Case #" << i+1 << ": INSOMNIA\n" ;
		}
		else{
		  for(j=0;j<=9;j++)c[j]=0;

		for(k=1; ;k++){
			
			if(k==INT_MAX){
			   cout << "Case #" << i+1 << ": INSOMNIA\n" ; 
			}
			
			temp=n*k;

			while(temp>0){
				 p=temp%10;
				c[p]++;
				temp/=10;
			}
            
            
			f=1;
			for(j=0;j<=9;j++){
				if(c[j]==0){
					f=0;
					break;
				}
			}

			if(f==1){
				cout << "Case #" << i+1 << ": " << n*k <<'\n' ;
				break;
			}
			
			
		}  
		}
		
	}

	return 0;
}

