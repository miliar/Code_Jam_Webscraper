#include <iostream>
using namespace std;
typedef long long unsigned int ll;

int main() {
	
	int test,n,m[1005];
	cin>>test;
	
	for(int t=1;t<=test;t++){
		
		cin>>n;
		for(int i=0;i<n;i++){
			cin>>m[i];
		}
		
		ll first = 0,second = 0;
		ll dif = 0;
		for(int i=1;i<n;i++){
			
			if(m[i] < m[i-1]){
				
				if((m[i-1]-m[i]) > dif){
					dif = m[i-1] - m[i];
				}
				
				first += m[i-1] - m[i];
			}
			
		}
	//	cout<<dif<<"---\n";
		for(int i=0;i<n-1;i++){
			
			if(m[i] < dif){
				second += m[i];
			}else{
				second += dif;
			}
			
		}
		
		cout<<"Case #"<<t<<": "<<first<<" "<<second<<"\n";
	}
	
	return 0;
}