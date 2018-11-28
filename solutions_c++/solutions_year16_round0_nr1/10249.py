#include <iostream>
using namespace std;
typedef long long ll;
bool digit[12];

void resetDigits(){
	for(int i=0;i<=9;i++)
		digit[i] = false;
}
bool allMarked(){
	for(int i=0;i<=9;i++)
		if(digit[i] == false)
			return false;
	return true;	
}
void markDigits(int n){
	while(n!=0){
		digit[n%10] = true;
		n /= 10;
	}
}

int main(){

	int t,i,n;
	cin>>t;
	for(int p=1;p<=t;p++){

		cin>>n;
		if(n==0){
			cout<<"Case #"<<p<<": INSOMNIA\n";
			continue;
		}
		resetDigits();
		i=1;
		while(1){
			markDigits(i*n);
			if(allMarked()){
				cout<<"Case #"<<p<<": "<<i*n<<"\n";
				break;
			}
			i++;
		}
	}
}