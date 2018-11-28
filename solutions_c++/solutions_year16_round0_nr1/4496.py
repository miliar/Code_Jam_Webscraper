#include <iostream>
using namespace std;
int number[10]={0};
int coun = 0;
int n;
void search(int number[], int n, int& count){
	int temp=0;
	while(n!=0){
		temp=n%10;
		if(number[temp]==0) number[temp]=1;
		n/=10;
	}
	count=0;
	for(int i = 0; i < 10; i++){
		if(number[i]==1) count++;
	}	
}
void out(int i, int n){
	if(n == 0){
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
	}else{
		memset(number,0,sizeof(number));
		int k = 1;
		int temp = n;
		while(coun!=10){
			n=k*temp;
			search(number,n,coun);
			k++;
		}
		cout<<"Case #"<<i<<": "<<n<<endl;
	}
}
int main(){
	int t;
	while(cin >> t){
		int i = 1;
		while(t--){
			cin>>n;
			coun = 0;
			out(i, n);
			i++;
		}
	}
}