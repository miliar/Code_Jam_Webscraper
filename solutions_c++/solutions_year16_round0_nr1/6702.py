#include <iostream>
using namespace std;

int a[10]={0},m;
int check(int a[],int n,int m){
	//cout<<a<<" "<<n<<" "<<"\n";
	int x=m*n;
	while(x>0){
		a[x%10]++;
		x/=10;
		}
	int count=0;
	for(int i=0;i<=9;i++){
		if(a[i]>0)
		count++;
		else
		break;
	}
	if(count==10)
	return m*n;
	else{
	m+=1;
	check(a,n,m);
	}
	}
	
int main() {
	// your code goes here
	int t;
	cin>>t;
	int i=t;
	while(t--){
		m=1;
		for(int i=0;i<=9;i++)
		a[i]=0;
		int n;
		cin>>n;
		cout<<"CASE #"<<i-t<<": ";
		if(n==0)
			cout<<"INSOMNIA\n";
		else
		cout<<check(a,n,m)<<"\n";
	}
	return 0;
}