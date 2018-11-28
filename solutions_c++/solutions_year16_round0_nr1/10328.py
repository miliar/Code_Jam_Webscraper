#include <iostream>
using namespace std;

bool arr[10];
void initialise(){
for(int i=0;i<10;i++){
arr[i]=0;
}
}

bool isComplete(){
for(int i=0;i<10;i++){
if(arr[i]==0){
return 0;}
}
return 1;
}

int main() {
	// your code goes here
	int t;
	long long int n;
	long long int ans;
	cin>>t;
	int q=1;
	while(t--){
	cin>>n;
	long long int j=1;
	cout<<"Case #"<<q<<": ";
	initialise();
	if(n==0){
	cout<<"INSOMNIA"<<endl;q++;
	continue;}
	bool t  = isComplete();
	while(!t){
	     long long int temp=n*j;
	     while(temp!= 0){
	     int i = temp % 10;
	     arr[i] = 1;
	     temp=temp/10;
	     }

	     ans = n*j;
	     j++;
	     t  = isComplete();
	}
	cout<<ans<<endl;
	q++;
	}
	return 0;
}
