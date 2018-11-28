#include <bits/stdc++.h>

using namespace std;

int occured;
bool num[10];

void checkDigits(int number){
	while(number){
		int temp = number%10;
		if(!num[temp]){
			num[temp] = true;
			occured++;
		}
		number /= 10;
	}
}

int main(){
	int T,N;
	cin>>T;


	for(int K=1; K<=T; K++){
		long long ans;
		cin>>N;
		
		if(N==0){
			printf("Case #%d: INSOMNIA\n", K);
			continue;
		}
		else{
			for(int i=0; i<10; i++)
				num[i] = false;

			occured = 0;
			long long a = N;
			while(occured != 10){
				checkDigits(a);
				a += N;
			}
			ans = a - N;
		}

		printf("Case #%d: %ld\n", K, ans); 
	}

	return 0;
}