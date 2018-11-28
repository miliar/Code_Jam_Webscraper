#include <iostream>
#include <vector>
using namespace std;
int main(){
	long long int t,n,counter,i,value;
	cin>>t;
	for(int k=0;k<t;k++){
		counter=0;
		i=0;
		cin>>n;
		vector<int> check(10,0);
		if(n==0){
			cout<<"Case #"<<k+1<<": INSOMNIA"<<endl;
		}
		else{
			while(counter!=10){
				i++;
				counter=0;
				value=n*i;
				while(value>0){
					check[value%10]++;
					value=value/10;
				}
				for(int j=0;j<10;j++){
					if(check[j]!=0){
						counter++;
					}
				}
			}
			cout<<"Case #"<<k+1<<": "<<n*i<<endl;
		}
	}
}
