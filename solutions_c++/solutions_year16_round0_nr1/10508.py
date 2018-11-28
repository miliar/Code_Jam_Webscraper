#include <iostream>
using namespace std;
int arr[10];

void setArr(){
	for (int i=0;i<10;i++)arr[i] = 0;
}

void checkDigits(long a){
	long x=a;
	while(x>0){
		arr[x%10]=1;
		x=x/10;
	}
}
bool checkArr(){
	bool allDigits=true;
	for (int i=0;i<10;i++){
		if(arr[i] == 0) allDigits = false;
	}
	return allDigits;
}

int main() {
	int T;
	long N;
	cin>>T;
	for(int i=1;i<=T;i++){
		cin>>N;
		if(N<=0){
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}else{
			setArr();
			long j=0;
			while(!checkArr()){
				j++;
				checkDigits(j*N);
			}
			cout<<"Case #"<<i<<": "<<N*j<<endl;
		}
	}
	return 0;
}