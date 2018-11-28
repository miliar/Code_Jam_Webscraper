#include<iostream>
#include<fstream>
using namespace std;
bool check(int a[]){
    for(int i=0;i<=9;i++){
    	if(a[i]==0)
    	return false;
	}
	return true;
}
int main(){
	int t;
	ifstream inpt;
	inpt.open("A-large.in");
    ofstream opt("cdjam.txt");
	inpt>>t;
	int c=0;
	while(t--){
			c++;
		long long int n;
		inpt>>n;
		int a[10]={0};
		if(n==0){
			opt<<"Case #"<<c<<": INSOMNIA"<<endl;
			continue;
		}
		int k=1;
		while(k){
			long long int temp=k*n;
        	while(temp){
        		int dig=temp%10;
        		a[dig]++;
        		temp/=10;
			}
			if(check(a)){
		      break;		
			}	
			k++;
		}
		opt<<"Case #"<<c<<": "<<k*n<<endl;
	
	}
}
