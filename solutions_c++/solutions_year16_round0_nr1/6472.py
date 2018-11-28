#include <iostream>
using namespace std;

int a[10];

void cleararr(){
	int i;
	for(i=0;i<10;i++)	a[i]=0;
}

int allticked(){
	int i;
	for(i=0;i<10;i++){
		if(a[i]==0){
			return 0;
		}
	}
	return 1;
}

void mark(long long n){
	long long x=n;
	while(x){
		a[x%10]=1;
		x/=10;
	}
}

int main() {
	// your code goes here
	long long n,t,i,x;
	cin>>t;
	x=t;
	while(t--){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<x-t<<": INSOMNIA"<<endl;
			continue;
		}
		cleararr();
		i=1;
		while(!allticked()){
			mark(i*n);
			i++;
		}
		cout<<"Case #"<<x-t<<": "<<(i-1)*n<<endl;
	}
	return 0;
}