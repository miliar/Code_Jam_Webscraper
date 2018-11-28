#include<iostream>
#include<string>
 
using namespace std;
int main(){
	int test,j=0;
	cin>>test;
	while(j<test){
		int a;
		cin>>a;
		string input;
		cin>>input;
		int i=1,sum=0,count=0;
		sum += input[0] - '0';
		while(i< a+1){
			if(sum >= i){
				sum += input[i] - '0';
				i++;
			}
			else{
				count += i-sum;
				sum += i-sum;
			}

		}
		cout <<"Case #"<<j+1<<": "<<count<<endl;
		j++;
	}
	return 0;

}