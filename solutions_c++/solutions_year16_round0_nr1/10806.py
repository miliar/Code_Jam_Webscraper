#include <iostream>
#include <cstdlib>

using namespace std;

bool digits[11]={false, false, false, false, false, false, false, false, false, false};

void setmap(unsigned long long int input){
	while(input>0){
		if(input>=10){
			digits[input%10]=true;
			input=input/10;
		}
		else{
			digits[input]=true;
			input=0;
		}
	}
}

bool isdone(){
	unsigned int i=0;
	while(i<=9){
		if(digits[i]==false){
			return false;
		}
		i++;
	}
	return true;
}

void resetmap(){
	unsigned int i=0;
	while(i<=9){
		digits[i]=false;
		i++;
	}
}

int main(){
	unsigned long long int input;
	unsigned int i=1, T, caseing=1;
	cin>>T;
	while(caseing<=T){
		cin>>input;
		if(input==0){
			cout<<"Case #"<<caseing<<": "<<"INSOMNIA"<<endl;
			goto next;
		}
		i=1;
		resetmap();
		while(isdone()==false){
			setmap(i*input);
			i++;
		}
		i--;
		cout<<"Case #"<<caseing<<": "<<input*i<<endl;
		next:
		caseing++;
	}
}
