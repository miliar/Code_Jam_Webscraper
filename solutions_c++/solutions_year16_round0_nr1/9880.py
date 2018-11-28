#include<iostream>
using namespace std;

int main(){
	int t, n, j, tmp, ans, cpyN, s;
	bool a[10];
	
	cin>>t;
	for(int i = 1; i <= t; i++){
		cin>>n;
		j = 1;
		
		if(n == 0){
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		for(int k = 0; k < 10; k++){	//set all to not found
			a[k] = false;
		}
		while(1){
			ans = n * j;
			cpyN = ans;
			while(cpyN != 0){
				a[cpyN % 10] = true;
				cpyN = cpyN / 10;
			}
			for(s = 0; s < 10; s++){
				if(!a[s]){
					break;
				}
			}
			if(s == 10){
				cout<<"Case #"<<i<<": "<<ans<<endl;
				break;
			}
			j++;
		}
	}
}
