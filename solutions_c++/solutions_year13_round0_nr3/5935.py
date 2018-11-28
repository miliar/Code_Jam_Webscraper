#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

bool palindrome(int n){
	int temp=0,num;
	num=n;
	while(n>0){
		temp=(temp*10)+(n%10);
		n=n/10;
	}
	if(temp==num)
		return true;
	return false;
}

bool fairAndSquare(int n){
	bool fair,square;
	if(int(sqrt(n))==sqrt(n)){
		if(palindrome(n) && palindrome(sqrt(n)))
			return true;
	}
	return false;
}

int main(){
	int notc,a=1,b=1000,count=0,i,caseno=1;
	ifstream pin("pin.txt");
	ofstream pout("pout.txt");
	pin>>notc;
	while(caseno<=notc){
		count=0;
		pin>>a>>b;
		for(i=a;i<=b;i++){
			if(fairAndSquare(i)){
				count++;
			}
		}
		pout<<"Case #"<<caseno<<": "<<count<<endl;
		caseno++;
	}
	return 0;
}
