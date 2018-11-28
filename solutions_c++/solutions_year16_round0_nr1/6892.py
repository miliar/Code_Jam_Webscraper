#include<iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int test=1;test<=t;test++){
		int sleep[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1};
		long int n;
		int top=0;
		cin>>n;
		cout<<"Case #"<<test<<": ";
		if(n==0)
			cout<<"INSOMNIA"<<endl;
		else{
			for(int i=1;i<100;i++){
				long int x= i*n;
				while(x){
					int temp= x%10;
					bool found= false;
					x=x/10;
					for(int i=0;i<top;i++)
						if(temp==sleep[i]){
							found=true;
							break;
						}
					if(!found){
						sleep[top]=temp;
						top++;
						if(top==10)
							break;
						}
					}
				if(top==10){
					cout<<i*n<<endl;
					break;
				}		
			}
		}
	}
	return 0;
}
