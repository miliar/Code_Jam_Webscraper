#include <iostream>
#include <string.h>

int a,left,right,mid;
std::string s;

void binarySearch(){
	int number=0;
	int cnt=0;

	mid=(left+right)/2;

	number+=mid;

	for(int i=0; i<=a; i++){
		if(number>=i){
			number+=s[i]-'0';
			cnt++;
		}

	}

	
	if(cnt==a+1)right=mid;
	else left=mid;

	




}



int main(void){

	
	int b;
	int t;
	int number=0;
	


	std::cin>>t;

	for(int i=0; i<t; i++){
		std::cin>>a;
		std::cin>>s;
		left=-1;
		right=1000;

		while(right-left>1){
			
	
			binarySearch();

				
		}

		for(int k=0; k<=a; k++){
			number+=s[i]-'0';
		}

		if(number==1)std::cout<<"Case #"<<i+1<<": "<<0<<std::endl;
		else std::cout<<"Case #"<<i+1<<": "<<right<<std::endl;
		
		number=0;
		
	}
			
	




}