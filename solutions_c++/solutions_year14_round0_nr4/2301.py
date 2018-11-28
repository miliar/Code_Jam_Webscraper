#include<iostream>
#include<algorithm>
using namespace std;


int main(){
	int T , num , i = 1;
	float K[1001] , N[1000] ,input;
	cin>>T;
	for(int t = 1 ; t <= T ; t++){
		cin>>num;
		i = 1;
		while(i<= 2*num){
			cin>> input;
			if(i<=num){
				N[i-1] = input;
			}
			else{
				K[i-num-1] = input;
			}
			i++;
		}
		sort(K , K+num);
		sort(N , N+num);
		
		//deceitful
		int x = 0 , y = 0 , deceitCount = 0;
		while(x < num && y < num){
			if(N[x] <= K[y]){
				x++;
			}
			else if(N[x] > K[y]){
				x++ ; y++;
				deceitCount++;
			}
		}
		x = 0; y =0; 
		int optimalCount = 0;
		while(x < num && y < num){
			if(N[x] < K[y]){
				x++; y++;
				optimalCount++;
			}
			else if(N[x] >= K[y]){
				y++;
			}
		}
		cout<<"Case #"<<t<<": "<<deceitCount<<" "<<(num-optimalCount)<<endl;	
	}
	return 0;
} 
