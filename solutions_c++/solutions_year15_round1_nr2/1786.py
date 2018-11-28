#include<bits/stdc++.h>
#define ll unsigned long long
using namespace std;

int gcd(int a, int b){
	if(b==0) return a;
	return gcd(b,a%b); 
}

int main(){
	int tc;
	cin>>tc;
	for(int z=1; z<=tc;z++){
		int b,n;
		cin>>b>>n;
		int a[b], copy[b];
		int red=0;
		for(int i=0;i<b;i++){
			cin>>a[i];
			copy[i]=a[i];
			red=gcd(a[i],red);
		}
		//cout<<red<<endl;
		int count=b;
		
		bool found = false;
		while(true){
			if(n<=count){
				cout<<"Case #"<<z<<": "<<n<<endl;
				break;
			}
			int i;
			int j;
			for(i=0;i<b;i++){
				copy[i]-=red;
			}	/*if(copy[i]==0){
					copy[i]=a[i];
					count++;
					if(count==n){
						found=true;
						break;
					}	
				}*/
			bool allZero=true;
				
			for(j=0;j<b;j++){
				if(copy[j]!=0) allZero=false;
				else{
					copy[j]=a[j];
					count++;
					if(count==n){
						found=true;
						break;
					}
				}
			}	
			if(found){
				cout<<"Case #"<<z<<": "<<j+1<<endl;
				break;
			}
			if(allZero){
				count-=b;
				n=n%count;
				if(n==0){
					n=count;
					//break;
				}
				count=b;
			}			
			
			if(found){
				cout<<"Case #"<<z<<": "<<j+1<<endl;
				break;
			}
		}
	}
	return 0;
}
