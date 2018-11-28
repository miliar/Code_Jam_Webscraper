
#include <iostream>
#include <cmath>

using namespace std;

bool check_palindrome(long int a){
	int c=0,b=a;
	while(a!=0){
		c=c*10+a%10;
		a=a/10;
	}
	if(b==c) return 1;
	else return 0;
}
	
bool check_square(long int a){
	long int sroot = pow(a,0.5);
	double long s =   pow(a,0.5);
	float r = s - sroot;
	if((sroot*sroot)==a && r == 0.0){
		if(check_palindrome(sroot)){
			return 1;
		}
		else{
			return 0;
		}
	}
	else
	return 0;
}		

int main(){
	long int number_of_testcases;
	cin>>number_of_testcases;
	long int A[number_of_testcases],B[number_of_testcases],count=0;
	for(long int i=0;i<number_of_testcases;i++){
		cin>>A[i];
		cin>>B[i];
	}
	
	for(long int i=0;i<number_of_testcases;i++){
		for(long int j=A[i];j<=B[i];j++){
			if(check_palindrome(j)&&check_square(j)){
				count++;
			}
		}
		cout<<"Case #"<<i+1<<":"<<" "<<count<<endl;
		count=0;
	}
			
	return 0;
}	
