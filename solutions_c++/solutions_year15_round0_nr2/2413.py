#include<iostream>
#include<algorithm>
using namespace std;

int t,d;
int p[1003];
int maks,ilosc,res;
	
int suf(int a, int b){
	if(a % b == 0)return (a/b - 1);
	return (a/b);
}
	
int main(){
	cin>>t;
	for(int k = 0; k < t; k++){
		cin>>d;
		for(int i = 0; i < d; i++){
			cin>>p[i];
		}
		cout<<"Case #"<<k+1<<": ";
		
		maks = p[0];
		for(int i = 1; i < d; i++){
			if(p[i] > maks)maks = p[i];
		}
		
		res = 99999999;
		
		for(int i = maks; i > 0; i--){
			ilosc = 0;
			for(int j = 0; j < d; j++){
				if(p[j] > i){
					ilosc += suf(p[j],i);
				}	
			}
			res = min(res,(ilosc + i));
		}
		cout<<res<<endl;
	}	

return 0;
}
