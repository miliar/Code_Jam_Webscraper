#include<iostream>
using namespace std;
int isFirst(int a){
	for(int i = 2; i*i <= a; i++){
		if(a%i == 0) return i;
	}
	return -1;
}
int tab[40];
int toTwo(int number){
	for(int i = 0; i < 40; i++)tab[i]=0;
	int i = 0;
	while(number>0){
		tab[i] = number%2;
		i++;
		number/=2;
	}
	return i;		
}
long long int fromTwoToNumber(int number){
	long long int counter = 1, result = 0;
	for(int i = 0; i < 40; i++){
		result+=tab[i]*counter;
		counter*=number;
	}
	return result;
}
 		
int a, starterIter, c, t, n, j;
int main(){
	cin>>t;
	for(int m = 0;m < t; m++){
		cin>>n>>j;
		cout<<"CASE #"<<m+1<<":\n";
		starterIter = 1;
		for(int k = 1; k < n; k++){
			starterIter*=2;
		}
		int z = starterIter+1, counterOfNumbers = 0;
		while(counterOfNumbers < j){
			if(isFirst(z) != -1){
				int myNumber;
				bool isDivided = true;
				for(int i = 2; i <= 10; i++){
					myNumber = toTwo(isFirst(z));
					long long int a = fromTwoToNumber(i);
					myNumber = toTwo(z);
					long long int b = fromTwoToNumber(i);
					isDivided = isDivided && (b%a==0);
				}
				if(isDivided){
					for(int i = myNumber-1; i >= 0; i--){
						cout<<tab[i];
					}
					cout<<" ";
					myNumber = toTwo(isFirst(z));
					for(int i = 2; i <= 10; i++){
						cout<<fromTwoToNumber(i)<<" ";
					}
					counterOfNumbers++;
					cout<<endl;
				}
			}
			z+=2;
		}
	}
	return 0;
}

		
		
					 
				
		 
	
