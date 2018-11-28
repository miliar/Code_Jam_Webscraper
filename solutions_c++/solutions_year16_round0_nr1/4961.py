#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	int i;
	for(i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		int n;
		bool arr[10] = {0,0,0,0,0,0,0,0,0,0};
		cin>>n;
		if(n==0) {cout<<"INSOMNIA\n";}
		else
		{	
			int k = 0;
			int m = n;
			int j = 1;
			while(j){
				m = n*j;
				while(m){
					if(arr[m%10] == 0){
						arr[m%10] = 1; k++;
				//		cout<<arr[m%10]<<" "<<k<<endl;
						
					}
					m = m/10;
					
				}
				if(k == 10){
					cout<<n*j<<endl; break;
				}
				j++;
			}
		}
	}

}