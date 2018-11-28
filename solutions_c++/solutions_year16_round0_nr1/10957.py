#include<iostream>
using namespace std;
int s(int ar[]){
	int x = 0;
	for(int i = 0;i<10;i++){
		if(ar[i]==1){
			x++;
		}
	}
	
	return x;
}
void check(int n,int ar[]){
	//cout<<"check	"<<n<<endl;
	while(n!=0){
		
		int dig = n%10;
	//	cout<<dig<<"<--dig\n";
		n = n/10;
		ar[dig] = 1;
		 
	}
	
}
int fun(int n){
	int ar[10];
	for(int i = 0;i<10;i++){
		ar[i] = 0;
	}
	int sum = 0;
	int i = 1;
	int ans = n;
	while( sum != 10){
		ans = n*i;
		check(ans,ar);
		sum = s(ar);
		i++;
	}
	//cout<<"ans:	"<<ans<<endl;
	return ans;
}
int main(){
	int t, n;
	
	cin>>t;
	
	for(int i = 0;i<t;i++){
		cin>>n;
		if(n == 0){
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
		else{
		
		int ans = fun(n);
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	}
	
	return 0;
}
