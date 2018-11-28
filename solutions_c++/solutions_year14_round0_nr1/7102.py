#include <iostream>
using namespace std;
int main(){
	int t;
	int a[16],b[16],a1,b1,count,ans;
	cin>>t;
	for(int i=0; i<t; i++){
		count = 0;
		cin>> a1;
		for(int j=0; j<16; j++){
			cin>>a[j];
		}
		
		cin>> b1;
		for(int k=0; k<16; k++){
			cin>>b[k];
		}
		
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if(a[(a1-1)*4 + j] == b[(b1-1)*4 +k]){
					count ++;
					ans = a[(a1-1)*4 + j]; 
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(count == 1)cout<<ans<<"\n";
		if(count == 0)cout<<"Volunteer cheated!"<<"\n";
		if(count > 1)cout<<"Bad magician!"<<"\n";
	}
}
