#include <iostream>
#include <math.h>

using namespace std;

int all_digits(long long digits[]){
	int flag = 1;
	for(int i=0;i<10;i++){
		if(digits[i]==0){
			flag = 0;
			break;
		}	
	}
	return flag;
}

int main(){
	long long N,cases;
	cin>>cases;
	for(long long z=0;z<cases;z++){
		cin>>N;

		long long digits[10];
		for(int j=0;j<10;j++)
			digits[j] = 0;

		if(N==0)
			cout<<"Case #"<<z+1<<": INSOMNIA\n";
		else{
			long long temp = N, mult = 1;
			while(all_digits(digits)==0){
				N = temp*mult;
				mult++;

				while (N)
			    {
			        int digit = N % 10;
			     	digits[digit]++;   
			        N /= 10;
			    }
			}
			cout<<"Case #"<<z+1<<": "<<temp*(mult-1)<<"\n";
		}
	}
	return 0;
}