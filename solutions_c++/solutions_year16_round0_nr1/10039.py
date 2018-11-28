#include <bits/stdc++.h>
using namespace std;
bool arr[10];
int main(){
	int n;
	cin>>n;
	int x;
	for(int i=0;i<n;i++){
		memset(arr,false,sizeof(arr));
		cin>>x;
		int temp=0;
		int ind = 1;
		int text = 55;
		int resp;
		if(x!=0){
			while(true){
				resp = temp = x*ind;
				
				while(temp!=0){
					int aux = temp%10;
					if(arr[aux]==false){
						arr[aux]=true;
						text-=(aux+1);
					}
					if(temp>9){
						temp/=10;
					}else{
						temp=0;
					}
				}
				if(text==0){
					break;
				}
				ind++;
			}
			cout<<"Case #"<<i+1<<": "<<resp<<endl;
		}else{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
	}
	return 0;
}